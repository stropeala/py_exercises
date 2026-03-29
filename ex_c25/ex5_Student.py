# Exercise 5: OOP Exercise
# Create a Student class.

# Attributes:
# • name
# • grades (private list)

# Tasks:
# 1. Method add_grade(grade).
# 2. Method get_average().
# 3. If the list is empty return 0.

# Goal: store and manage collections safely.


class Student:
    def __init__(self, name: str, grades: list) -> None:
        self.name = name
        self.grades = grades

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, new_grades: list) -> None:
        self._grades = new_grades

    def add_grade(self, new_grade: float) -> None:
        if new_grade <= 0:
            raise ValueError("Grade cannot be zero or negative")
        self.grades = self.grades + [new_grade]

    def get_average(self):
        if self.grades == []:
            return 0
        average = sum(self.grades) / len(self.grades)
        return average


if __name__ == "__main__":
    ionel = Student("Ionel", [10, 7, 5])
    print(ionel.grades)

    ionel.add_grade(8.5)
    print(ionel.grades)

    print(ionel.get_average())

    try:
        ionel.grades = []
    except ValueError as error:
        print(f"Error: {error}")

    try:
        ionel.add_grade(-1)
    except ValueError as error:
        print(f"Error: {error}")

    ionel.grades = []
    print(ionel.get_average())
