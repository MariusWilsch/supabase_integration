# src/repositories/user_repository.py

from .base_repository import BaseRepository
from ..models.user import User
from ..lib.supabase_client import SupabaseClient


class UserRepository(BaseRepository):
    def __init__(self, supabase_client: SupabaseClient):
        super().__init__(supabase_client, "users")

    def create_user(self, user: User) -> User:
        response = self._create(user.model_dump())
        # Process the response and return a User object
        return User(**response.data[0])

    def get_user(self, user_id: str) -> User:
        response = self._read(user_id)
        # Process the response and return a User object
        return User(**response.data[0])

    def update_user(self, user_id: str, updated_data: dict) -> User:
        response = self._update(user_id, updated_data)
        # Process the response and return a User object
        return User(**response.data[0])

    def delete_user(self, user_id: str) -> None:
        self._delete(user_id)


# Implement similar classes for FilterRepository and ThreadRepository
