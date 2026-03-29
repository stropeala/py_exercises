# Exercise 1: OOP Exercise
# Create a class called Person.

# The class should store:
# • name (public attribute)
# • age (private attribute)

# Tasks:
# 1. Create a constructor that receives name and age.
# 2. Store age as a private attribute using __age.
# 3. Create a method get_age() that returns the age.

# Goal: learn how private attributes protect data inside a class.


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
        details = f"Name: {self.name}\nAge: {self.age} "
        return details


if __name__ == "__main__":
    ionel = Person("Ionel", 25)
    print(ionel.age)
    print(ionel.name)
    print(ionel.get_details())
