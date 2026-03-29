# Exercise 8: OOP Exercise
# Create a PasswordManager class.

# Attributes:
# • password (private)

# Tasks:
# 1. Store the password privately.
# 2. Implement check_password(input_password).
# 3. Return True or False.

# Goal: simulate a simple login system.


class PasswordManager:
    def __init__(self, password: str) -> None:
        self.password = password

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, new_password: str) -> None:
        if new_password == "":
            raise ValueError("Password cannot be empty")
        self._password = new_password

    def check_password(self, input_password):
        if input_password == "":
            raise ValueError("Password cannot be empty")
        if input_password != self.password:
            raise ValueError(f"Wrong Password!: {False}")
        return f"Password is correct!: {True}"


if __name__ == "__main__":
    ionel = PasswordManager("secret123")

    try:
        ionel.check_password("wrong")
    except ValueError as error:
        print(f"Error: {error}")

    user_input = input("Enter password: ")
    try:
        ionel.check_password(user_input)
    except ValueError as error:
        print(f"Error: {error}")
        
