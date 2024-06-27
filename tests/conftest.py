import pytest, os
from dotenv import load_dotenv
from src.lib.supabase_client import SupabaseClient
from src.repositories import ThreadRepository, UserRepository
from src.models import User

load_dotenv()


@pytest.fixture(scope="session")
def supabase_client():
    return SupabaseClient(
        url=os.getenv("SUPABASE_URL"), key=os.getenv("SUPABASE_SERIVCE_KEY")
    )


@pytest.fixture(scope="session")
def test_session(supabase_client):
    # Setup: Sign in and create test user
    supabase = supabase_client.get_client
    auth_user = supabase.auth.sign_in_with_password(
        {"email": "testuser@example.com", "password": "testpassword123"}
    ).user

    user_repo = UserRepository(supabase_client)
    user_data = {
        "name": "Test User",
        "email": auth_user.email,
        "id": auth_user.id,
        "login": "testuser",
        "phone_number": "1234567890",
    }
    test_user = User(**user_data)
    created_user = user_repo.create_user(test_user)

    yield created_user  # This will be accessible in tests

    # Teardown: Delete the test user
    try:
        user_repo.delete_user(created_user.id)
        print(f"Successfully deleted test user with ID: {created_user.id}")
    except Exception as e:
        print(f"Failed to delete test user: {e}")

    # Sign out the user
    supabase.auth.sign_out()


@pytest.fixture(scope="function")
def test_user(test_session):
    return test_session


@pytest.fixture(scope="function")
def user_repository(supabase_client):
    return UserRepository(supabase_client)


@pytest.fixture(scope="function")
def thread_repository(supabase_client):
    return ThreadRepository(supabase_client)


# @pytest.fixture(scope="module")
# def test_user(supabase_client: SupabaseClient):
#     supabase = supabase_client.get_client
#     # Sign in with the pre-existing test user
#     user = supabase.auth.sign_in_with_password(
#         {"email": "testuser@example.com", "password": "testpassword123"}
#     )
#     return user.user


# @pytest.fixture(scope="module")
# def test_user_data():
#     return {
#         "name": "Test User",
#         "email": "testuser@example.com",
#         # "user_id": str(uuid4()),
#         "login": "testuser",
#         "phone_number": "1234567890",
#     }


# @pytest.fixture(scope="module")
# def create_test_user(user_repository, test_user):
#     user_data = {
#         "name": "Test User",
#         "email": test_user.email,
#         "id": test_user.id,
#         "login": "testuser",
#         "phone_number": "1234567890",
#     }
#     user = User(**user_data)
#     created_user = user_repository.create_user(user)
#     return created_user


# @pytest.fixture(scope="module")
# def user_repository(supabase_client):
#     return UserRepository(supabase_client)


# @pytest.fixture(scope="module")
# def thread_repository(supabase_client: SupabaseClient):
#     return ThreadRepository(supabase_client)
