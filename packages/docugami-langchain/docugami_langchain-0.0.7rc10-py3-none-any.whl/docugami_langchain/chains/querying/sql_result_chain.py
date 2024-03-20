import logging
from operator import itemgetter
from typing import Any, AsyncIterator, Optional

from langchain_community.utilities.sql_database import SQLDatabase
from langchain_core.runnables import Runnable, RunnableConfig, RunnableLambda

from docugami_langchain.base_runnable import TracedResponse
from docugami_langchain.chains.base import BaseDocugamiChain
from docugami_langchain.chains.helpers import (
    replace_table_name_in_select,
    table_name_from_sql_create,
)
from docugami_langchain.chains.querying.sql_fixup_chain import SQLFixupChain
from docugami_langchain.output_parsers.sql_finding import SQLFindingOutputParser
from docugami_langchain.params import RunnableParameters, RunnableSingleParameter

logger = logging.getLogger(__name__)


class SQLResultChain(BaseDocugamiChain[dict]):
    db: SQLDatabase
    sql_fixup_chain: Optional[SQLFixupChain] = None

    fix_only_syntax_errors = False  # Set to true to be more efficient and only try to fix SQL in case of errors

    def runnable(self) -> Runnable:
        """
        Custom runnable for this chain.
        """

        def table_info(_: Any) -> str:
            """
            Return the table info for the database connection for this chain.
            """
            return self.db.get_table_info()

        def fix_table_name(sql_query: str) -> str:
            """
            Attempt to update the table name in the given query, to match the table in the
            database connection for this chain.
            """
            if self.db:
                try:
                    table_name = table_name_from_sql_create(self.db.get_table_info())
                    return replace_table_name_in_select(sql_query, table_name)
                except Exception as exc:
                    # Only warn, but continue, since this is best effort
                    logger.warning(
                        f"Ignored exception in table name cleanup: {str(exc)}"
                    )
                    pass  # nosec

            # Just echo back the input if unable to fix
            return sql_query

        def run_sql_query(inputs: dict, config: Optional[RunnableConfig]) -> dict:
            """
            Runs the given query against the database connection for this chain, and returns the result.
            """

            question = inputs.get("question")
            sql_query = inputs.get("sql_query")

            if not question or not sql_query:
                raise Exception("Inputs required: question, sql_query")

            try:
                if not self.fix_only_syntax_errors and self.sql_fixup_chain:
                    # Pre-emptively try to fix the SQL query to increase chances that it will be valid
                    # This is not very efficient (so you can set fix_only_syntax_errors to True), however
                    # not all invalid sql statements (e.g. with invalid column names) are raising exceptions
                    # when called via the SQLDatabase implementation in LangChain.
                    fixed_sql_response = self.sql_fixup_chain.run(
                        table_info=table_info(self),
                        sql_query=sql_query,
                        config=config,  # Pass the config down to link traces in langsmith
                    )
                    sql_query = fixed_sql_response.value

                # Run
                return {
                    "question": question,
                    "sql_query": sql_query,
                    "sql_result": str(self.db.run(sql_query)).strip(),
                }
            except Exception as exc:
                is_syntax_error = "syntax error" in str(exc)
                is_syntax_error = is_syntax_error or ".OperationalError" in str(exc)

                if is_syntax_error and self.sql_fixup_chain:
                    # If syntax error in Raw SQL, try to fix up the SQL
                    # giving the LLM context on the exception to aid fixup
                    fixed_sql_response = self.sql_fixup_chain.run(
                        table_info=table_info(self),
                        sql_query=sql_query,
                        exception=str(exc),
                        config=config,  # Pass the config down to link traces in langsmith
                    )

                    # Run Fixed-up SQL
                    fixed_sql = fixed_sql_response.value
                    return {
                        "question": question,
                        "sql_query": fixed_sql,
                        "sql_result": str(self.db.run(fixed_sql)).strip(),
                    }
                else:
                    raise exc

        return {
            "question": itemgetter("question"),
            "sql_query": {
                "question": itemgetter("question"),
                "table_info": RunnableLambda(table_info),
            }
            | super().runnable()
            | SQLFindingOutputParser()
            | RunnableLambda(fix_table_name),  # type: ignore
        } | RunnableLambda(
            run_sql_query  # type: ignore
        )

    def params(self) -> RunnableParameters:
        return RunnableParameters(
            inputs=[
                RunnableSingleParameter(
                    "question",
                    "QUESTION",
                    "Question asked by the user.",
                ),
                RunnableSingleParameter(
                    "table_info",
                    "TABLE DESCRIPTION",
                    "Description of the table to be queried via SQL.",
                ),
            ],
            output=RunnableSingleParameter(
                "sql_query",
                "SQL QUERY",
                "SQL Query that should be run against the table to answer the question, considering the rules and examples provided. Do NOT generate a direct non-SQL answer, even if you know it."
                + " Always produce only SQL as output.",
            ),
            task_description="only generates SQL as output. Given an input SQL table description and a question, you generate an equivalent syntactically correct SQLite query against the given table",
            additional_instructions=[
                "- Only generate SQL as output, don't generate any other language e.g. do not try to directly answer the question asked.",
                '- If the question is ambiguous or you don\'t know how to answer it in the form of a SQL QUERY, just dump the first row of the table i.e. SELECT * FROM "Table Name" LIMIT 1.',
                "- Unless the user specifies in the question a specific number of examples to obtain, query for at most 5 results using the LIMIT clause as per SQLite.",
                "- If needed, order the results to return the most informative data in the database.",
                "- Never query for all columns from a table. You must query only the columns that are needed to answer the question.",
                '- Wrap each column name in the query in double quotes (") to denote them as delimited identifiers.',
                "- Pay attention to use only the column names you can see in the given tables. Be careful to not query for columns that do not exist.",
                "- Pay attention to use the date('now') function to get the current date, if the question involves \"today\".",
                """- When matching strings in WHERE clauses, always use LIKE with LOWER rather than exact string match with "=" in case the user did not fully specify complete input with the right """
                + """casing, for example generate SELECT * from "athletes" WHERE LOWER("last name") LIKE '%jones%' instead of SELECT * from "athletes" WHERE "last name" = 'Jones'""",
                "- Never provide any additional explanation or discussion, only output the SQLite query requested, which answers the question against the given table description.",
                "- Always pay attention to the table name in your query, making sure it exactly matches the table description.",
            ],
            stop_sequences=[
                "\n",
                ";",
                "|",
            ],
        )

    def run(  # type: ignore[override]
        self,
        question: str,
        config: Optional[RunnableConfig] = None,
    ) -> TracedResponse[dict]:
        if not question:
            raise Exception("Input required: question")

        return super().run(
            question=question,
            config=config,
        )

    async def run_stream(  # type: ignore[override]
        self,
        question: str,
        config: Optional[RunnableConfig] = None,
    ) -> AsyncIterator[TracedResponse[dict]]:
        if not question:
            raise Exception("Input required: question")

        async for item in super().run_stream(
            question=question,
            config=config,
        ):
            yield item

    def run_batch(  # type: ignore[override]
        self,
        inputs: list[str],
        config: Optional[RunnableConfig] = None,
    ) -> list[dict]:
        return super().run_batch(
            inputs=[{"question": i} for i in inputs],
            config=config,
        )
