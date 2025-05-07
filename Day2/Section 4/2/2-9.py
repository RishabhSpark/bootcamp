def validate_args(func):
    def wrapper(self, *args, **kwargs):
        if len(args) != 2:
            print(f"Error: {func.__name__} requires exactly 2 arguments.")
            return
        return func(self, *args, **kwargs)
    return wrapper

class Calculator:
    @validate_args
    def add(self, a, b):
        return a + b

calc = Calculator()
print(calc.add(5, 3))
print(calc.add(5))