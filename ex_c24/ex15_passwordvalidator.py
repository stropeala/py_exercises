# 15) Password Validator
# Create PasswordValidator with:
# - attribute: min_len
# - method: is_valid(pw) (length + at least one digit)


class PasswordValidator:
    def __init__(self, min_len: int) -> None:
        self._min_len = min_len

    @property
    def min_len(self):
        return self._min_len

    @min_len.setter
    def min_len(self, new_min):
        self._min_len = new_min

    def is_valid(self, password: str):
        if password == "":
            raise ValueError("Password cannot be empty!")

        if len(password) < self._min_len:
            raise ValueError("Password length invalid!")

        return "Password is valid!"
