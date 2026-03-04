# 3) Rectangle Area + Perimeter
# Create a class Rectangle with:
# - attributes: width, height
# - methods: area(), perimeter()


class Rectangle:
    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, new_width: int):
        if new_width < 0:
            raise ValueError("Value below zero!")
        self._width = new_width

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, new_height: int):
        if new_height < 0:
            raise ValueError("Value below zero!")
        self._height = new_height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


if __name__ == "__main__":
    r1 = Rectangle(10, 5)
    print(r1.area())
    print(r1.perimeter())
