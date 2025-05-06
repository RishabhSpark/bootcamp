def get_user_age_lbyl(user_data: dict) -> int:
    if "age" in user_data:
        return user_data["age"]
    else:
        return -1

user = {"name": "Alice"}
print(get_user_age_lbyl(user))