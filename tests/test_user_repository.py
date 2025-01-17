import pytest, uuid
from src.models import User

def test_get_user(user_repository, test_user):
    fetched_user = user_repository.get_user(str(test_user.id))

    assert fetched_user.id == test_user.id
    assert fetched_user.name == test_user.name
    assert fetched_user.email == test_user.email


def test_update_user(user_repository, test_user):
    updated_data = {"name": "Updated Test User", "phone_number": "9876543210"}
    updated_user = user_repository.update_user(test_user.id, updated_data)

    assert updated_user.name == updated_data["name"]
    assert updated_user.phone_number == updated_data["phone_number"]

    # Reset the user data
    user_repository.update_user(
        test_user.id, {"name": test_user.name, "phone_number": test_user.phone_number}
    )


def test_delete_user(user_repository, test_user):
    # Test delete
    user_repository.delete_user(test_user.id)

    with pytest.raises(Exception):
        user_repository.get_user(test_user.id)


# import pytest
# from uuid import uuid4
# from src.models.user import User
# from src.lib.supabase_client import SupabaseClient
# from src.repositories import UserRepository, ThreadRepository


# @pytest.fixture(scope="module")
# def test_user(supabase_client: SupabaseClient):
#     supabase = supabase_client.get_client
#     # Sign in with the pre-existing test user
#     user = supabase.auth.sign_in_with_password(
#         {"email": "testuser@example.com", "password": "testpassword123"}
#     )
#     return user.user


# @pytest.fixture
# def test_user_data():
#     return {
#         "name": "Test User",
#         "email": "testuser@example.com",
#         # "user_id": str(uuid4()),
#         "login": "testuser",
#         "phone_number": "1234567890",
#     }


# def test_create_user(user_repository, test_user, test_user_data):
#     # Create a temporary user
#     user_data = {**test_user_data, "id": test_user.id}
#     user = User(**user_data)
#     created_user = user_repository.create_user(user)

#     assert created_user.id == test_user.id
#     assert created_user.name == test_user_data["name"]
#     assert created_user.email == test_user.email

#     # We need to clean up the user after the test
#     user_repository.delete_user(test_user.id)


# def test_get_user(user_repository, test_user, test_user_data):
#     # Create a temporary user
#     user_data = {**test_user_data, "id": test_user.id}
#     user = User(**user_data)
#     user_repository.create_user(user)

#     # Now test the get_user function
#     fetched_user = user_repository.get_user(str(test_user.id))

#     assert fetched_user.id == test_user.id
#     assert fetched_user.name == test_user_data["name"]
#     assert fetched_user.email == test_user.email

#     user_repository.delete_user(test_user.id)


# def test_update_user(user_repository, test_user, test_user_data):
#     # Create a temporary user
#     user = {**test_user_data, "id": test_user.id}
#     user = User(**user)
#     user_repository.create_user(user)

#     # Update the user
#     updated_data = {"name": "Updated Test User", "phone_number": "9876543210"}
#     updated_user = user_repository.update_user(test_user.id, updated_data)

#     assert updated_user.name == updated_data["name"]
#     assert updated_user.phone_number == updated_data["phone_number"]

#     # Clean up
#     user_repository.delete_user(test_user.id)


# def test_delete_user(user_repository, test_user, test_user_data):
#     # Create a temporary user
#     user = {**test_user_data, "id": test_user.id}
#     user = User(**user)
#     user_repository.create_user(user)

#     # Delete the user
#     user_repository.delete_user(test_user.id)

#     # Check if the user is deleted
#     with pytest.raises(Exception):
#         user_repository.get_user(test_user.id)
