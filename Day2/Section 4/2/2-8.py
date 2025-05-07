def custom_logger(log_message):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"Log Message: {log_message}")
            print(f"Function {func.__name__} is about to execute.")
            result = func(*args, **kwargs)
            print(f"Function {func.__name__} executed. Returning: {result}")
            return result
        return wrapper
    return decorator

@custom_logger("Starting the function")
def add(a, b):
    return a + b

# Test
print(add(5, 3))