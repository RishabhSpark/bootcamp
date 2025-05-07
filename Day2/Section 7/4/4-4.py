import logging
import os

DEBUG = os.getenv('DEBUG', 'False') == 'True'

if DEBUG:
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.WARNING)

logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug("Processing data in verbose mode.")
    # Function logic here

process_data("input data")
