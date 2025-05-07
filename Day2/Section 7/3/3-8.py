import logging

logger = logging.getLogger(__name__)

def process_data(data):
    try:
        result = 1 / 0
    except Exception as e:
        logger.error(f"Error processing data: {e}")
        raise  # Re-raise the exception after logging

process_data("some data")
