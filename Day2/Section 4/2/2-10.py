# Simple Logger Decorator
def simple_logger(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function ended")
        return result
    return wrapper

# Timer Decorator
import time
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

# Debug Info Decorator
def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@simple_logger
@timer
@debug_info
def some_function(a, b):
    return a + b

some_function(3, 4)
