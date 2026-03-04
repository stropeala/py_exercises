# 1) Greeting Bot
# Create a class Greeter with:
# - instance attribute: name
# - method: greet() -> returns "Hi, I'm <name>!"


class Greeting_bot:
    def __init__(self, name: str) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    def greet(self):
        return f"Hi, I'm {self._name}"


if __name__ == "__main__":
    student1 = Greeting_bot("Ion")
    print(student1.greet())
