# * Import own modules
from repositories import FilterRepository, ThreadRepository, UserRepository

# from services.user_service import UserService

from src.config.logging_config import configure_logging

# Configure logging

# * Importing the required libraries
from dotenv import load_dotenv

# * Load environment variables from .env file
load_dotenv()

# * Configure logging
configure_logging()


def main():
    # user_service = UserService()

    user_repo = UserRepository()
