# Exercise 9: OOP Exercise
# Create a Temperature class.

# Attributes:
# • celsius (private)

# Tasks:
# 1. Constructor receives Celsius.
# 2. Implement to_fahrenheit().

# Formula:
# F = C * 9/5 + 32

# Goal: expose useful methods while protecting internal data.


class Temperature:
    def __init__(self, celsius: float) -> None:
        self.celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, new_celsius: float) -> None:
        self._celsius = new_celsius

    def to_fahrenheit(self):
        f = self.celsius * 9 / 5 + 32
        return round(f, 2)


if __name__ == "__main__":
    ionel = Temperature(100)
    print(ionel.celsius)
    print(ionel.to_fahrenheit())
