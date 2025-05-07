from functools import wraps

def decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__}...")
        return func(*args, **kwargs)
    return wrapper

@decorator
def my_function(x, y):
    """This function adds two numbers."""
    return x + y

print(my_function(3, 4))
print(my_function.__name__)
print(my_function.__doc__)