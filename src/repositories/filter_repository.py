from typing import Literal, Union
from .base_repository import BaseRepository
from ..models import Filter
from ..lib.supabase_client import SupabaseClient


class FilterRepository(BaseRepository):
    def __init__(self, supabase_client: SupabaseClient):
        super().__init__(supabase_client, table_name="filters")

    def create_filter(self, filter: Filter) -> Filter:
        response = self._create(filter.model_dump())
        # Process the response and return a Filter object
        return Filter(**response.data[0])

    def get_filters_by_id(
        self, value: str, id: Literal["id", "thread_id", "user_id"] = "id"
    ) -> list[Filter]:
        response = self._read(value, id)
        # Process the response and return a list of Filter objects or a single Filter object
        return [Filter(**filter) for filter in response.data]

    def update_filter(self, filter_id: str, updated_data: dict) -> Filter:
        response = self._update(filter_id, updated_data)
        # Process the response and return a Filter object
        return Filter(**response.data[0])

    def delete_filter(self, filter_id: str) -> None:
        self._delete(filter_id)
