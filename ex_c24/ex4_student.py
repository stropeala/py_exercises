# 4) Student Average
# Create a class Student with:
# - attributes: name, grades (list of floats)
# - method: average() (return 0.0 if empty list)


class Student:
    def __init__(self, name: str, grades: list) -> None:
        self._name = name
        self._grades = grades

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name: str):
        self._name = new_name

    @property
    def grades(self):
        return self._grades

    @grades.setter
    def grades(self, new_grades: list):
        self._grades = new_grades

    def average(self):
        if self.grades == []:
            return 0.0
        else:
            average = sum(self.grades) / len(self.grades)
            return average


if __name__ == "__main__":
    s1 = Student("Ion", [9.50, 7.00, 8.50])
    s2 = Student("John", [])
    print(s1.average())
    print(s2.average())
