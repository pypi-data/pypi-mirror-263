import logging

from ..integration.database import DatabaseConnection, get_parameters
from .base import Arguments, CommandRegistrar

logger = logging.getLogger("dap")


class AbstractDbCommandRegistrar(CommandRegistrar):
    async def _before_execute(self, args: Arguments) -> None:
        if not args.connection_string:
            raise ValueError("missing database connection string")

        logger.debug("Checking for valid database connection string")
        try:
            _, _ = get_parameters(args.connection_string)
        except ValueError:
            logger.error(
                "Invalid database connection string, please check its format and URL-encoding of special characters"
            )
            raise

        logger.debug("Checking connection to database")
        connection = DatabaseConnection(args.connection_string)
        async with connection.connection as _:
            # simply open and close connection to check validity
            pass
