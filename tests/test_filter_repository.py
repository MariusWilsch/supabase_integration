import pytest
from src.models import Filter


def test_create_filter(filter_repository, test_filter_data):
    filter = Filter(**test_filter_data)
    created_filter = filter_repository.create_filter(filter)

    assert created_filter.id == test_filter_data["id"]
    assert created_filter.name == test_filter_data["name"]
    assert created_filter.user_id == test_filter_data["user_id"]
    assert created_filter.thread_id == test_filter_data["thread_id"]

    # Clean up
    filter_repository.delete_filter(str(created_filter.id))


def test_get_filters_by_id(filter_repository, test_filter_data):
    filter = Filter(**test_filter_data)
    created_filter = filter_repository.create_filter(filter)

    # Test get by id
    fetched_filters = filter_repository.get_filters_by_id(str(created_filter.id))
    assert len(fetched_filters) == 1
    assert fetched_filters[0].id == created_filter.id

    # Test get by thread_id
    thread_filters = filter_repository.get_filters_by_id(
        created_filter.thread_id, "thread_id"
    )
    assert len(thread_filters) >= 1
    assert any(f.id == created_filter.id for f in thread_filters)

    # Test get by user_id
    user_filters = filter_repository.get_filters_by_id(
        created_filter.user_id, "user_id"
    )
    assert len(user_filters) >= 1
    assert any(f.id == created_filter.id for f in user_filters)

    # Clean up
    filter_repository.delete_filter(str(created_filter.id))


def test_update_filter(filter_repository, test_filter_data):
    filter = Filter(**test_filter_data)
    created_filter = filter_repository.create_filter(filter)

    updated_data = {
        "name": "Updated Test Filter",
        "status": "Done",
    }
    updated_filter = filter_repository.update_filter(
        str(created_filter.id), updated_data
    )

    assert updated_filter.name == updated_data["name"]
    assert updated_filter.status == updated_data["status"]

    # Clean up
    filter_repository.delete_filter(str(created_filter.id))


def test_delete_filter(filter_repository, test_filter_data):
    filter = Filter(**test_filter_data)
    created_filter = filter_repository.create_filter(filter)

    filter_repository.delete_filter(str(created_filter.id))

    # Check if the filter is deleted
    with pytest.raises(Exception):
        filter_repository.get_filters_by_id(str(created_filter.id))
