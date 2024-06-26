import pytest, os
from dotenv import load_dotenv
from src.lib.supabase_client import SupabaseClient
from src.repositories.user_repository import UserRepository

load_dotenv()


@pytest.fixture(scope="session")
def supabase_client():
    return SupabaseClient(
        url=os.getenv("SUPABASE_URL"), key=os.getenv("SUPABASE_SERIVCE_KEY")
    )


@pytest.fixture
def user_repository(supabase_client):
    return UserRepository(supabase_client)
