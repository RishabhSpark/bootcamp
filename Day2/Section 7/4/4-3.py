import logging

logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

def process_data(data):
    try:
        if data == "bad":
            raise ValueError("Invalid data")
        return "processed data"
    except Exception as e:
        logger.error(f"Error ID 1234: {str(e)}")
        raise

process_data("bad")