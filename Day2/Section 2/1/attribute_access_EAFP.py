class User:
    def __init__(self, name: str, age: int = None):
        self.name = name
        self.age = age

def get_user_age_eafp(user: User) -> int:
    return getattr(user, "age", -1)

user1 = User(name="Alice", age=25)
user2 = User(name="Bob")

print(get_user_age_eafp(user1))
print(get_user_age_eafp(user2))