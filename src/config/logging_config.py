import logging


def configure_logging():
    logging.basicConfig(
        level=logging.ERROR,  # Set the logging level
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",  # Log message format
        handlers=[
            logging.FileHandler("app.log"),  # Log to a file
            logging.StreamHandler(),  # Also log to the console
        ],
    )
