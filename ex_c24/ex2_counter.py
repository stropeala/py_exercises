# 2) Counter with Instance State
# Create a class Counter with:
# - instance attribute: value (starts at 0)
# - methods: inc(step=1), dec(step=1)


class Counter:
    def __init__(self, value: int = 0) -> None:
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if new_value < 0:
            raise ValueError("Value below zero!")
        self._value = new_value

    def inc(self, step: int = 1) -> None:
        self.value = self._value + step

    def dec(self, step: int = 1) -> None:
        self.value = self._value - step


if __name__ == "__main__":
    c = Counter()
    c.inc()
    c.inc(5)
    c.dec(2)
    # c.dec(10)
