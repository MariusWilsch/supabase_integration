from .repository_exception import RepositoryException
from lib.supabase_client import SupabaseClient
import logging


class BaseRepository:
    def __init__(self, supabase_client: SupabaseClient, table_name: str):
        self.supabase = supabase_client.get_client
        self.table = table_name

    def _handle_error(self, operation: str, error: Exception):
        """Handle and log errors, then raise a RepositoryException."""
        logging.error(f"Error during {operation}: {str(error)}")
        raise RepositoryException(f"Error during {operation}: {str(error)}")

    def _execute_operation(self, operation: str, query):
        """Execute a database operation with error handling.

        Description:
        -----------
        This method is a wrapper around the Supabase client's execute method. It handles errors by logging them and raising a RepositoryException.
        """
        try:
            return query.execute()
        except Exception as e:
            self._handle_error(operation, e)

    # Template methods for CRUD operations
    def _create(self, data: dict):
        return self._execute_operation(
            "create", self.supabase.table(self.table).insert(data)
        )

    def _read(self, filterValue: str, column: str = "id"):
        return self._execute_operation(
            "read", self.supabase.table(self.table).select("*").eq(column, filterValue)
        )

    def _update(self, value: str, data: dict, column: str = "id"):
        return self._execute_operation(
            "update", self.supabase.table(self.table).update(data).eq(column, value)
        )

    def _delete(self, value: str, column: str = "id"):
        return self._execute_operation(
            "delete", self.supabase.table(self.table).delete().eq(column, value)
        )
