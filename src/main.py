# * Import own modules
from repositories import FilterRepository, ThreadRepository, UserRepository

# from services.user_service import UserService

from src.config.logging_config import configure_logging
from src.models import User

# Configure logging

# * Importing the required libraries
from dotenv import load_dotenv

# * Load environment variables from .env file
load_dotenv()

# * Configure logging
configure_logging()


def main():
    user_repo = UserRepository()
    thread_repo = ThreadRepository()

    thread_repo.get_thread_by_id("63a1d0d1-c0a0-4f9c-b0e3-a3a2e0f1c5e6", id="user_id")
