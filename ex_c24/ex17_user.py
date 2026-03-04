# 17) User Profile
# Create User with:
# - attributes: username, email
# - method: display() -> "username <email>"


class User:
    def __init__(self, username: str, email: str) -> None:
        self._username = username
        self._email = email

    @property
    def username(self):
        return self._username

    @username.setter
    def username(self, new_username: str):
        if new_username == "":
            raise ValueError("Username cannot be empty!")

        self._username = new_username

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, new_email: str):
        if new_email == "":
            raise ValueError("Email cannot be empty!")

        self._email = new_email

    def display(self):
        user_info = f"{self.username} <{self.email}>"
        return user_info


if __name__ == "__main__":
    user1 = User("salut", "test@g.com")
    print(user1.display())
