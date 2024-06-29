import os, time
from pprint import pprint
from lib.supabase_client import SupabaseClient

# * Import own modules
from repositories import FilterRepository, ThreadRepository, UserRepository

from config.logging_config import configure_logging
from models import User

# Configure logging

# * Importing the required libraries
from dotenv import load_dotenv

# * Load environment variables from .env file
load_dotenv()

# * Configure logging
configure_logging()


def main():
    supabase_client = SupabaseClient(
        os.getenv("SUPABASE_URL"), os.getenv("SUPABASE_KEY")
    )
    repo_u = UserRepository(supabase_client=supabase_client)
    repo_t = ThreadRepository(supabase_client=supabase_client)
    repo_f = FilterRepository(supabase_client=supabase_client)

    # Create a test user
    user = repo_u.create_user(user_data={})
    user2 = repo_u.create_user(user_data={})
    # pprint(user)
    thread = repo_t.create_thread(
        thread_data={
            "thread_id": "thread_4hIKWeW286_1223",
            "user_id": user["user_id"],
            "status": "Update this Thread",
        }
    )
    updated_thread = repo_t.update_thread(
        thread_id=thread["thread_id"],
        updated_data={"name": "Updated Thread", "status": "Updated Thread"},
    )
    repo_u.delete_user(user["user_id"])


if __name__ == "__main__":
    main()
