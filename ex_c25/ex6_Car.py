# Exercise 6: OOP Exercise
# Create a Car class.

# Attributes:
# • brand
# • speed (private)

# Tasks:
# 1. accelerate(value)
# 2. brake(value)
# 3. Speed should never go below 0.
# 4. get_speed()

# Goal: maintain valid object state.


class Car:
    def __init__(self, brand: str, speed: float) -> None:
        self.brand = brand
        self.speed = speed

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, new_speed: float):
        if new_speed < 0:
            raise ValueError("Speed cannot be negative")
        self._speed = new_speed

    def accelerate(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Value cannot be zero or below")
        self.speed += value

    def decelerate(self, value: float) -> None:
        if value <= 0:
            raise ValueError("Value cannot be zero or below")
        self.speed = max(0, self.speed - value)


if __name__ == "__main__":
    ionel = Car("Lexus", 150)
    print(ionel.speed)

    ionel.speed = 180
    print(ionel.speed)

    ionel.accelerate(20)
    print(ionel.speed)

    ionel.decelerate(60)
    print(ionel.speed)

    ionel.decelerate(999)
    print(ionel.speed)

    try:
        ionel.speed = -5
    except ValueError as error:
        print(f"Error: {error}")

    try:
        ionel.decelerate(-5)
    except ValueError as error:
        print(f"Error: {error}")
