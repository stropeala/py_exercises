# Exercise 2: OOP Exercise
# Extend the Person class.

# Instead of modifying the age directly, create a setter method.

# Tasks:
# 1. Create a method set_age(new_age).
# 2. If the value is negative, raise a ValueError.
# 3. Otherwise update the private attribute.

# Goal: understand how encapsulation controls how data is modified.


class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age: int) -> None:
        if new_age < 0:
            raise ValueError("Age cannot be negative")
        self.__age = new_age

    def get_details(self):
        details = f"Name: {self.name}, Age: {self.age} "
        return details


if __name__ == "__main__":
    ionel = Person("Ionel", 25)
    print(ionel.get_details())

    ionel.age = 35
    print(ionel.get_details())

    try:
        ionel.age = -5
    except ValueError as error:
        print(f"Error: {error}")
