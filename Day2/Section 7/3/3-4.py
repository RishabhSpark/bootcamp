import logging

# Setup logger
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(data):
    logger.debug("Entering process_data function.")

    logger.debug("Exiting process_data function.")

process_data("input data")
