# 11) Temperature Converter
# Create Temperature with:
# - attribute: celsius
# - methods: to_fahrenheit(), set_celsius()


class Temperature:
    def __init__(self, name: str = "Celsius", degree: float = 0) -> None:
        self._name = name
        self._degree = degree

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str) -> None:
        self._name = new_name

    @property
    def degree(self):
        return self._degree

    @degree.setter
    def degree(self, new_degree: float) -> None:
        self._degree = new_degree

    def to_fahrenheit(self):
        fahrenheit = (self._degree * 9 / 5) + 32
        return f"Fahrenheit: {fahrenheit}"
