import logging
from typing import List, Tuple, Union, overload
from urllib.parse import urlparse

import clickhouse_driver as chdr
import polars as pl
from clickhouse_driver.dbapi import DatabaseError, InterfaceError
from clickhouse_driver.dbapi.extras import Cursor, DictCursor, NamedTupleCursor
from pypika.queries import Selectable
from typing_extensions import Literal

from tesseract_olap.backend import Backend, ParamManager, Result, Session
from tesseract_olap.backend.exceptions import UpstreamInternalError, UpstreamNotPrepared
from tesseract_olap.common import AnyDict, AnyTuple
from tesseract_olap.query import AnyQuery, DataQuery, MembersQuery
from tesseract_olap.schema import InlineTable, SchemaTraverser

from .dialect import ClickhouseDataType
from .sqlbuild import dataquery_sql, membersquery_sql

logger = logging.getLogger("tesseract_olap.backend.clickhouse")


class ClickhouseBackend(Backend):
    """Clickhouse Backend class

    This is the main implementation for Clickhouse of the core :class:`Backend`
    class.

    Must be initialized with a connection string with the parameters for the
    Clickhouse database. Then must be connected before used to execute queries,
    and must be closed after finishing use.
    """

    dsn: str

    def __init__(self, dsn: str) -> None:
        self.dsn = dsn

    def new_session(self):
        return ClickhouseSession(self.dsn)

    def ping(self) -> bool:
        """Checks if the current connection is working correctly."""
        with self.new_session() as session:
            with session.cursor() as cursor:
                cursor.execute("SELECT 1")
                result = cursor.fetchone()
        return result == (1,)

    def validate_schema(self, schema: "SchemaTraverser"):
        """Checks all the tables and columns referenced in the schema exist in
        the backend.
        """
        logger.debug("Validating schema '%s' against backend", schema)

        tables = schema.unwrap_tables()

        query_template = """
SELECT
    '{table_name}' AS "table",
    arrayMap(x -> x.1, columns) AS "columns",
    (SELECT count(*) FROM {table_name}) AS "count"
FROM system.columns
WHERE table = '{table_name}'
""".strip()
        query = " UNION ALL ".join(
            query_template.format(table_name=table_name) for table_name in tables.keys()
        )

        with self.new_session() as session:
            with session.cursor() as cursor:
                cursor.execute(query)
                result = cursor.fetchall() or []

        observed: dict[str, set[str]] = {item[0]: set(item[1]) for item in result}

        assert tables == observed


class ClickhouseSession(Session):
    def __init__(self, dsn: str) -> None:
        self.dsn = dsn

    def __repr__(self) -> str:
        dsn = urlparse(self.dsn)
        if dsn.password is not None:
            dsn = dsn._replace(password="***")
        return f"{type(self).__name__}(dsn='{dsn.geturl()}')"

    def __exit__(self, exc_type, exc_val, exc_tb):
        result = super().__exit__(exc_type, exc_val, exc_tb)

        if exc_type is InterfaceError:
            raise UpstreamNotPrepared(*exc_val.args).with_traceback(exc_tb)
        if exc_type is DatabaseError:
            raise UpstreamInternalError(*exc_val.args).with_traceback(exc_tb)

        return result

    def connect(self):
        self._connection = chdr.connect(dsn=self.dsn, compression="lz4")

    def close(self):
        self._connection.close()

    def fetch(self, query: AnyQuery, **kwargs) -> Result[List[AnyTuple]]:
        qbuilder, meta = _query_to_builder(query)

        with self.cursor() as cursor:
            _tables_into_cursor(cursor, meta.tables)
            cursor.execute(qbuilder.get_sql(), parameters=meta.params)
            data = cursor.fetchall()
            columns = tuple(cursor.columns_with_types or [])

        return Result(data or [], columns)

    def fetch_dataframe(self, query: AnyQuery, **kwargs) -> Result[pl.DataFrame]:
        qbuilder, meta = _query_to_builder(query)

        with self.cursor() as cursor:
            _tables_into_cursor(cursor, meta.tables)
            data = pl.read_database(
                query=qbuilder.get_sql(),
                connection=cursor,
                execute_options={"parameters": meta.params},
            )
            columns = tuple(cursor.columns_with_types or [])

        return Result(data, columns)

    def fetch_records(self, query: AnyQuery, **kwargs) -> Result[List[AnyDict]]:
        qbuilder, meta = _query_to_builder(query)

        with self.cursor("Dict") as cursor:
            _tables_into_cursor(cursor, meta.tables)
            cursor.execute(qbuilder.get_sql(), parameters=meta.params)
            data = cursor.fetchall()
            columns = tuple(cursor.columns_with_types or [])

        return Result(data, columns)

    @overload
    def cursor(self) -> "TypedCursor": ...
    @overload
    def cursor(self, format_: Literal["Tuple"]) -> "TypedCursor": ...
    @overload
    def cursor(self, format_: Literal["Dict"]) -> "TypedDictCursor": ...
    @overload
    def cursor(self, format_: Literal["NamedTuple"]) -> "NamedTupleCursor": ...

    def cursor(
        self, format_: Literal["Dict", "Tuple", "NamedTuple"] = "Tuple"
    ) -> Union["Cursor", "DictCursor", "NamedTupleCursor"]:
        if format_ == "Dict":
            cls = DictCursor
        elif format_ == "Tuple":
            cls = Cursor
        elif format_ == "NamedTuple":
            cls = NamedTupleCursor
        else:
            raise ValueError(f"Invalid cursor result format: '{format_}'")

        return self._connection.cursor(cls)


def _query_to_builder(query: AnyQuery) -> Tuple[Selectable, ParamManager]:
    if isinstance(query, DataQuery):
        return dataquery_sql(query)

    if isinstance(query, MembersQuery):
        return membersquery_sql(query)


def _tables_into_cursor(cursor: Cursor, tables: List["InlineTable"]):
    for table in tables:
        tblmeta_gen = (ClickhouseDataType[item.name].value for item in table.types)
        structure = zip(table.headers, tblmeta_gen)
        cursor.set_external_table(table.name, list(structure), table.rows)


class TypedCursor(Cursor):
    columns_with_types: List[Tuple[str, str]]


class TypedDictCursor(DictCursor):
    columns_with_types: List[Tuple[str, str]]
