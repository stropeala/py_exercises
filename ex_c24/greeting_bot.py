class Greeting_bot:
    def __init__(self, name: str) -> None:
        self._name = name

    def greet(self):
        return f"Hi, I'm {self._name}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name


if __name__ == "__main__":
    student1 = Greeting_bot("Ion")
    print(student1.greet())
