import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

user_name = "Alice"
user_age = 30

logger.debug(f"User: {user_name}, Age: {user_age}")