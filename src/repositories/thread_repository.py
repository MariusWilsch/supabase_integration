from typing import Literal
from .base_repository import BaseRepository
from lib.supabase_client import SupabaseClient
# from models import Thread


class ThreadRepository(BaseRepository):
    def __init__(self, supabase_client: SupabaseClient):
        super().__init__(supabase_client, table_name="threads")

    def create_thread(self, thread_data: dict) -> dict:
        response = self._create(thread_data)
        # Process the response and return a Thread object
        return response.data[0]

    def get_thread_by_id(
        self, value: str, id: Literal["thread_id", "user_id"]
    ) -> list[dict]:
        response = self._read(value, id)
        return [thread_data for thread_data in response.data]

    def update_thread(self, thread_id: str, updated_data: dict) -> dict:
        response = self._update(thread_id, updated_data, "thread_id")
        # Process the response and return a Thread object
        return response.data[0]

    def delete_thread(self, thread_id: str) -> None:
        self._delete(thread_id, "thread_id")
