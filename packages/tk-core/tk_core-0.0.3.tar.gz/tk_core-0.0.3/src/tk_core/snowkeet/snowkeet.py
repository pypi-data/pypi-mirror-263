from __future__ import annotations

import os
from datetime import datetime
from types import TracebackType
from typing import Any

import numpy as np
import pandas as pd
import snowflake.snowpark as sp
import snowflake.snowpark.functions as F
from snowflake.snowpark import DataFrame, Session

from tk_core.snowkeet.error_wrapper import sf_schema_checker

# TODO: Investigate better defaults and potential wrapper for sane configs.


class Snowkeet:
    """
    A class for interacting with Snowflake databases. Include common helper patterns

    Args:
        database (str, optional): The name of the database to connect to. Defaults to None.
        schema (str, optional): The name of the schema to connect to. Defaults to None.
        role (str, optional): The name of the role to use. Defaults to None.
        warehouse (str, optional): The name of the warehouse to use. Defaults to None.

    Methods:
        session(): Returns the current session object.
        get_schema(table: str) -> sp.types.StructType: Returns the schema for a given table.
    """

    def __init__(
        self,
        database: str | None = None,
        schema: str | None = None,
        role: str | None = None,
        warehouse: str | None = None,
    ) -> None:
        self.database = database or os.environ["SNOWFLAKE_DB"]
        if self.database is None:
            raise ValueError("Database name is required as an argument or in the environment variable SNOWFLAKE_DB.")
        self.schema = schema or os.environ["SNOWFLAKE_SCHEMA"]
        if self.schema is None:
            raise ValueError("Schema name is required as an argument or in the environment variable SNOWFLAKE_SCHEMA.")
        self.role = role or os.environ["SNOWFLAKE_ROLE"]
        if self.role is None:
            raise ValueError("Role name is required as an argument or in the environment variable SNOWFLAKE_ROLE.")
        self.warehouse = warehouse or os.environ["SNOWFLAKE_WAREHOUSE"]
        if self.warehouse is None:
            raise ValueError("Warehouse name is required as an argument or in the environment variable SNOWFLAKE_WAREHOUSE.")
        self._conn_params = {
            "account": os.environ["SNOWFLAKE_ACCOUNT"],
            "user": os.environ["SNOWFLAKE_USERNAME"],
            "password": os.environ["SNOWFLAKE_PASSWORD"],
            "role": self.role,
            "warehouse": self.warehouse,
            "database": self.database,
            "schema": self.schema,
        }
        self._session = None

    def __enter__(
        self,
        schema: str | None = None,
        database: str | None = None,
    ) -> Snowkeet:
        """
        Enter the context manager and return the session object.
        Offer option to change schema and database
        """
        if schema:
            self._conn_params["schema"] = schema
        if database:
            self._conn_params["database"] = database
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        traceback: TracebackType | None,
    ) -> bool | None:
        """
        Close the session when exiting the context manager.
        """
        self._close_session()

    def __str__(self) -> str:
        cloned_params = {k: v for k, v in self._conn_params.items() if k != "password"}
        return str(cloned_params)

    def _create_session(self) -> None:
        """Creates a new session object."""
        self._session = Session.builder.configs(self._conn_params).create()

    def _close_session(self) -> None:
        """Closes the current session object."""
        self._session.close()

    @property
    def session(self) -> Session:
        """Returns the current session object."""
        if not self._session:
            self._create_session()
        return self._session

    def set_schema(self, schema: str) -> None:
        """Sets the schema for the session."""
        if schema != self._conn_params["schema"]:
            self._conn_params["schema"] = schema
            self._close_session()
            self._create_session()

    def set_database(self, database: str) -> None:
        """Sets the database for the session."""
        if database != self._conn_params["database"]:
            self._conn_params["database"] = database
            self._close_session()
            self._create_session()

    def get_schema(self, table: str) -> sp.types.StructType:
        """Returns table schema from Snowflake for an sp.DataFrame"""
        return self.session.table(table).schema

    def create_df_with_schema(self, data: list | dict, table_name: str, drop_duplicates: bool = False) -> DataFrame:
        """Create a DataFrame with selected data and a particular schema from Snowflake"""
        schema = self.get_schema(table_name)
        df = self.session.createDataFrame(data, schema)
        if drop_duplicates:
            return df.drop_duplicates()
        else:
            return df

    def merge_table_single_key(
        self, obj: list | dict | pd.DataFrame, table_name: str, key: str, drop_duplicates: bool = False
    ) -> tuple:
        """
        Merge a single-key table in Snowflake with incoming data.

        Args:
            obj (Any): The incoming data to merge.
            table_name (str): The name of the table to merge.
            key (str): The name of the key to use for merging.
            drop_duplicates (bool, optional): Whether to drop duplicates. Defaults to False.

        Returns:
            Tuple: A tuple containing the merge result and the merged DataFrame.
        """
        if "UPDATE_TIME" in obj.columns:
            obj["UPDATE_TIME"] = pd.Timestamp.now()
        df = self.create_df_with_schema(obj, table_name, drop_duplicates)

        target_table = self.session.table(table_name)
        merge_result = target_table.merge(df, (target_table[key] == df[key]), [F.when_not_matched().insert(df)])
        return (merge_result, df)

    def merge_table_dual_key(
        self, obj: list | dict | pd.DataFrame, table_name: str, key1: str, key2: str, drop_duplicates: bool = False
    ) -> tuple:
        """
        Merge a single-key table in Snowflake with incoming data.

        Args:
            obj (Any): The incoming data to merge.
            table_name (str): The name of the table to merge.
            key (str): The name of the key to use for merging.
            drop_duplicates (bool, optional): Whether to drop duplicates. Defaults to False.

        Returns:
            Tuple: A tuple containing the merge result and the merged DataFrame.
        """
        if "UPDATE_TIME" in obj.columns:
            obj["UPDATE_TIME"] = pd.Timestamp.now()
        df = self.create_df_with_schema(obj, table_name, drop_duplicates)
        target_table = self.session.table(table_name)
        merge_result = target_table.merge(
            df,
            (target_table[key1] == df[key1]) & (target_table[key2] == df[key2]),
            [F.when_not_matched().insert(df)],
        )
        return (merge_result, df)

    def update_table_one_condition(
        self,
        table_name: str,
        column_to_update: str,
        new_value: Any,
        condition_column: str | None = None,
        condition_value: Any | None = None,
    ) -> tuple:
        """
        Update a table in Snowflake with incoming data.

        Args:
            table_name (str): The name of the table to update.
            column_to_update (str): The name of the column to update.
            new_value (Any): The new value to insert into the column.
            condition (dict): The condition to use for updating.
                should be formatted as the column name as the key and the value to match as the value
        """
        target_table = self.session.table(table_name)
        update_dictionary = {
            column_to_update: new_value,
            "UPDATE_TIME": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        }
        if condition_column is None or condition_value is None:
            update_result = target_table.update(update_dictionary)

        update_result = target_table.update(
            update_dictionary,
            target_table[condition_column] == condition_value,
        )
        return update_result

    def remove_ts(self, df: sp.DataFrame) -> sp.DataFrame:
        """Remove the timestamp columns from a DataFrame"""
        return df.drop("created_at").drop("updated_at")

    @sf_schema_checker
    def write_to_snowflake(self, dataframe: pd.DataFrame, table_name: str, mode: str = "append") -> None:
        """
        Writes a table to Snowflake using the schema from Snowpark.

        Args:
            snow (Snowkeet): _description_
            dataframe (list): A list of dictionaries with columns that match the schema we're writing to
            table_name (str): Name of table
            mode (str, optional): Append or overwrite the table. Defaults to 'append'. Use caution with 'overwrite'.
        """
        # convert NaNs to None
        dataframe = dataframe.replace(np.nan, None)
        schema = self.get_schema(table_name)

        # write the dataframe to snowflake using th
        sf_df = self.session.create_dataframe(data=dataframe, schema=schema)
        sf_df.write.mode(mode).save_as_table(table_name)

    def create_snowflake_schema(self, schema_name: str) -> None:
        try:
            self.session.sql(f"CREATE SCHEMA IF NOT EXISTS {schema_name}").collect()
            print(f"Schema {schema_name} created")
        except Exception as e:
            print(f"Error creating schema {schema_name}: {e}")

    def count_table(self, table_name: str) -> int:
        """Count the number of rows in a table in Snowflake.
        Returns: int: The number of rows in the table."""
        count_sql = f"""
            SELECT
            (SELECT COUNT(*) FROM {table_name}) AS COUNT
            """  # noqa: S608
        counts_dct = self.session.sql(count_sql).collect()
        return counts_dct[0]["COUNT"]

    def output_config(self) -> None:
        """Output the current configuration for the session."""
        print(self._conn_params)
