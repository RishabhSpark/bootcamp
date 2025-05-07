def prefix_printer(prefix):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f"{prefix} {func.__name__} is called")
            return func(*args, **kwargs)
        return wrapper
    return decorator

@prefix_printer("LOG:")
def greet(name):
    print(f"Greetings, {name}!")

greet("Bob")