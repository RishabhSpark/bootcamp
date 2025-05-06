def get_user_age_eafp(user_data: dict) -> int:
    try:
        return user_data["age"]
    except KeyError:
        return -1

user = {"name": "Alice"}
print(get_user_age_eafp(user))  