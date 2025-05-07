import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(user_id, data):
    logger.debug(f"User {user_id} called process_data function with data: {data}")
    # Function logic here

process_data(123, "input data")
