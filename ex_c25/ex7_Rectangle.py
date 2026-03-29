# Exercise 7: OOP Exercise
# Create a Rectangle class.

# Attributes:
# • width
# • height (private)

# Tasks:
# 1. Validate that width and height are positive.
# 2. Use setter methods.
# 3. Implement area().

# Goal: ensure correct data before using it.


class Rectangle:
    def __init__(self, width: float, height: float) -> None:
        self.width = width
        self.height = height

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height: float) -> None:
        if new_height <= 0:
            raise ValueError("<=0")
        self._height = new_height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width: float) -> None:
        if new_width <= 0:
            raise ValueError("<=0")
        self._width = new_width

    def area(self):
        area = self.height * self.width
        return area


if __name__ == "__main__":
    ionel = Rectangle(5, 3)
    print(ionel.area())

    ionel.width = 10
    print(ionel.area())

    try:
        ionel.width = -5
    except ValueError as error:
        print(f"Error: {error}")

    try:
        ionel.height = 0
    except ValueError as error:
        print(f"Error: {error}")
