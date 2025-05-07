def debug_info(func):
    def wrapper(*args, **kwargs):
        print(f"Function: {func.__name__}")
        print(f"Arguments: {args}, {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value: {result}")
        return result
    return wrapper

@debug_info
def add(a, b):
    return a + b

add(2, 3)