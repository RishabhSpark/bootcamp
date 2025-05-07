import logging
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def process_data(data):
    start_time = time.time()
    # Simulate data processing
    time.sleep(2)
    end_time = time.time()
    logger.debug(f"process_data took {end_time - start_time:.4f} seconds to complete")
    return "processed data"

process_data("input data")
