from typing import Literal
from .base_repository import BaseRepository
from ..models import Thread
from ..lib.supabase_client import SupabaseClient


class ThreadRepository(BaseRepository):
    def __init__(self, supabase_client: SupabaseClient):
        super().__init__(supabase_client, table_name="threads")
        # self.filter_repo = FilterRepository(supabase_client)

    def create_thread(self, thread: Thread) -> Thread:
        response = self._create(thread.model_dump())
        # Process the response and return a Thread object
        return Thread(**response.data[0])

    def get_thread_by_id(
        self, value: str, id: Literal["id", "user_id"] = "id"
    ) -> list[Thread]:
        response = self._read(value, id)
        return [Thread(**thread) for thread in response.data]

    def update_thread(self, thread_id: str, updated_data: dict) -> Thread:
        response = self._update(thread_id, updated_data)
        # Process the response and return a Thread object
        return Thread(**response.data[0])

    def delete_thread(self, thread_id: str) -> None:
        self._delete(thread_id)
