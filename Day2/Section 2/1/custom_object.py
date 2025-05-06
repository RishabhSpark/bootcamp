class CustomObject:
    def __init__(self, name: str):
        self.name = name

    def __getattr__(self, attr):
        return f"Attribute '{attr}' not found."

obj = CustomObject("Sample")
print(obj.name)
print(obj.age)