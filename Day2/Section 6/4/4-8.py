import logging

def setup_logger(debug=False):
    level = logging.DEBUG if debug else logging.INFO
    logging.basicConfig(level=level, format='%(asctime)s - %(levelname)s - %(message)s')
    return logging.getLogger(__name__)

logger = setup_logger(debug=True)

logger.debug("This is a debug message.")

logger.info("This is an info message.")
