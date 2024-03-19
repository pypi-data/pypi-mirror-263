"""
Use Snowflake Connector Class
"""
import os
import warnings

import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
from snowflake.connector.pandas_tools import write_pandas

from tk_core.snowkeet.error_wrapper import sf_schema_checker

load_dotenv()


class SnowkeetNew:
    def __init__(self) -> None:
        self._connection = None
        self.database = os.environ.get("SNOWFLAKE_DB")
        if self.database is None:
            warnings.warn(
                "No database provided. Please set the SNOWFLAKE_DB "
                "environment variable or use the SnowkeetNew.set_database() method.",
                UserWarning,
                stacklevel=2,
            )
        self.schema = os.environ.get("SNOWFLAKE_SCHEMA")
        if self.schema is None:
            warnings.warn(
                "No schema provided. Please set the SNOWFLAKE_SCHEMA "
                "environment variable or use the SnowkeetNew.set_schema() method.",
                UserWarning,
                stacklevel=2,
            )

    def __str__(self) -> str:
        return str(self.connection)

    def establish_connection(self) -> snowflake.connector:
        self._connection = snowflake.connector.connect(
            user=os.environ["SNOWFLAKE_USERNAME"],
            password=os.environ["SNOWFLAKE_PASSWORD"],
            account=os.environ["SNOWFLAKE_ACCOUNT"],
            database=self.database,
            schema=self.schema,
            # TODO: What session params do we want from tk_core?
            session_parameters={},
        )
        self._cursor = self._connection.cursor()

    @property
    def connection(self) -> snowflake.connector:
        """
        Return the connection to Snowflake
        Maintains the same connection if used multiple times
        """
        if self._connection is None:
            self.establish_connection()
        return self._connection

    def close_connection(self) -> None:
        """
        Close the cursor and connection to Snowflake
        """
        self._cursor.close()
        self.connection.close()

    def set_database(self, database: str) -> None:
        """
        Set the database to use for the connection
        Reset the connection
        """
        self.database = database
        if self.connection:
            self.close_connection()
            self.establish_connection()

    def set_schema(self, schema: str) -> None:
        """
        Set the schema to use for the connection
        Reset the connection
        """
        self.schema = schema
        if self.connection:
            self.close_connection()
            self.establish_connection()

    @sf_schema_checker
    def query_snowflake(self, query: str) -> pd.DataFrame:
        """
        Execute a query against Snowflake and return the results as a pandas dataframe
        """
        return pd.read_sql(query, self.connection)

    @sf_schema_checker
    def write_pandas_to_snowflake(
        self, df: pd.DataFrame, table_name: str, create_if_not_exist: bool = True, overwrite_table: bool = False
    ) -> bool:
        """
        Write a pandas dataframe to snowflake

        Default functionality is to APPEND

        Common Errors:
        - ProgrammingError: 090106 (22000): Cannot perform CREATE TEMPSTAGE
            - The schema/database aren't set (either in env or via set_database/set_schema)
            - The schema/database you're trying to write to don't exist

        SF Docs:
            https://docs.snowflake.com/en/developer-guide/python-connector/python-connector-api#write_pandas
        """
        result, chuck_count, rows_written, _output = write_pandas(
            conn=self.connection,
            df=df,
            table_name=table_name,
            database=self.database,
            schema=self.schema,
            auto_create_table=create_if_not_exist,
            overwrite=overwrite_table,
        )

        return result, rows_written
