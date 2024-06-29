import os
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
    user = repo_u.create_user(user_data={"user_id": "123456", "name": "Test User"})
    pprint(user)
    repo_t.create_thread(thread_data={"user_id": user["id"], "name": "Test Thread"})
    repo_f.create_filter(filter_data={"user_id": user["id"], "name": "Test Filter"})
    repo_f.create_filter(filter_data={"user_id": user["id"], "name": "Test Filter 2"})


if __name__ == "__main__":
    main()
