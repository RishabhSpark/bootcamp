import logging

logger = logging.getLogger(__name__)

def trace_function_calls(func):
    def wrapper(*args, **kwargs):
        logger.debug(f"Calling {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        logger.debug(f"{func.__name__} returned: {result}")
        return result
    return wrapper

@trace_function_calls
def process_data(data):
    return f"Processed {data}"

process_data("input data")
