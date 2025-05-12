import json

class User:
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = password  # Sensitive data

    def to_dict(self):
        return {
            "username": self.username,
            "email": self.email
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)

if __name__ == "__main__":
    user = User(
        username="test_user",
        email="test.user@example.com",
        password="testuserpassword123"
    )

    print(user.to_json())
