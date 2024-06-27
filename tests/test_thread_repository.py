import pytest
from uuid import uuid4
from src.models import Thread, User


@pytest.fixture(scope="function")
def test_thread_data(test_user):
    return {
        "id": str(uuid4()),
        "user_id": test_user.id,
        "name": "Test Thread",
        "status": "active",
        "meeting_booked": False,
        "conversation": {"assistant": "This is a test conversation", "user": "Hi"},
        "costs": 0.0,
        "time_spent_in_conversation": 0.0,
    }


def test_create_thread(thread_repository, test_thread_data):
    thread = Thread(**test_thread_data)
    created_thread = thread_repository.create_thread(thread)

    assert created_thread.id == test_thread_data["id"]
    assert created_thread.name == test_thread_data["name"]
    assert created_thread.user_id == test_thread_data["user_id"]

    # Clean up
    thread_repository.delete_thread(str(created_thread.id))

def test_get_thread_by_id(thread_repository, test_thread_data):
    thread = Thread(**test_thread_data)
    created_thread = thread_repository.create_thread(thread)

    fetched_thread = thread_repository.get_thread_by_id(str(created_thread.id))[0]

    assert fetched_thread.id == created_thread.id
    assert fetched_thread.name == created_thread.name
    assert fetched_thread.user_id == created_thread.user_id

    # Clean up
    thread_repository.delete_thread(str(created_thread.id))


def test_update_thread(thread_repository, test_thread_data):
    thread = Thread(**test_thread_data)
    created_thread = thread_repository.create_thread(thread)

    updated_data = {"name": "Updated Test Thread", "status": "completed"}
    updated_thread = thread_repository.update_thread(
        str(created_thread.id), updated_data
    )

    assert updated_thread.name == updated_data["name"]
    assert updated_thread.status == updated_data["status"]

    # Clean up
    thread_repository.delete_thread(str(created_thread.id))


def test_delete_thread(thread_repository, test_thread_data):
    thread = Thread(**test_thread_data)
    created_thread = thread_repository.create_thread(thread)

    thread_repository.delete_thread(str(created_thread.id))

    # Check if the thread is deleted
    fetched_threads = thread_repository.get_thread_by_id(str(created_thread.id))
    assert len(fetched_threads) == 0


def test_get_threads_by_user_id(thread_repository, test_thread_data, test_user):
    # Create multiple threads for the user
    thread1 = Thread(**test_thread_data)
    thread2 = Thread(
        **{**test_thread_data, "name": "Test Thread 2", "id": str(uuid4())}
    )

    created_thread1 = thread_repository.create_thread(thread1)
    created_thread2 = thread_repository.create_thread(thread2)

    # Fetch threads by user_id
    user_threads = thread_repository.get_thread_by_id(test_user.id, "user_id")

    assert len(user_threads) >= 2  # There should be at least 2 threads
    assert any(t.id == created_thread1.id for t in user_threads)
    assert any(t.id == created_thread2.id for t in user_threads)

    # Clean up
    thread_repository.delete_thread(str(created_thread1.id))
    thread_repository.delete_thread(str(created_thread2.id))
