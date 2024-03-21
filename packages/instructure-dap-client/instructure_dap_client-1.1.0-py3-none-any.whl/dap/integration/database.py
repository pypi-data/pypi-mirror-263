import os
from typing import Optional
from urllib.parse import unquote, urlparse

from pysqlsync.base import (
    BaseConnection,
    BaseEngine,
    ConnectionParameters,
    GeneratorOptions,
)
from pysqlsync.factory import get_dialect
from pysqlsync.formation.mutation import MutatorOptions
from pysqlsync.formation.py_to_sql import StructMode

from ..replicator import canvas, meta_schema, canvas_logs, catalog
from .database_errors import DatabaseConnectionError


class DatabaseConnection:
    _params: ConnectionParameters
    engine: BaseEngine
    connection: BaseConnection
    dialect: str

    def __init__(self, connection_string: Optional[str] = None) -> None:
        if connection_string is None:
            connection_string = os.getenv("DAP_CONNECTION_STRING")
            if not connection_string:
                raise DatabaseConnectionError("missing database connection string")
        dialect, self._params = get_parameters(connection_string)
        self.dialect = dialect
        self.engine = get_dialect(dialect)
        self.connection = self.engine.create_connection(
            self._params,
            GeneratorOptions(
                struct_mode=StructMode.JSON,
                foreign_constraints=False,
                namespaces={
                    meta_schema: "instructure_dap",
                    canvas: "canvas",
                    canvas_logs: "canvas_logs",
                    catalog: "catalog",
                },
                synchronization=MutatorOptions(
                    allow_drop_enum=False,
                    allow_drop_struct=False,
                    allow_drop_table=False,
                    allow_drop_namespace=False,
                ),
            ),
        )


def get_parameters(connection_string: str) -> tuple[str, ConnectionParameters]:
    parts = urlparse(connection_string, allow_fragments=False)
    return parts.scheme, ConnectionParameters(
        host=parts.hostname,
        port=parts.port,
        username=unquote(parts.username) if parts.username else None,
        password=unquote(parts.password) if parts.password else None,
        database=parts.path.lstrip("/") if parts.path else None,
    )
