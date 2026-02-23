# 8. Create a file named operations.py (content down bellow) in a new python package
# called "math_operations".
# Import the functions from the file "math_operations.py" (created at exercise 6) in the correct
# file, so that "main_program.py" may run properly.

# contents of operations.py
# def test_add():
#     result = operations.add(3, 5)
#     assert result == 8

# def test_subtract():
#     result = operations.subtract(10, 4)
#     assert result == 6

# def test_multiply():
#     result = operations.multiply(2, 6)
#     assert result == 12

# def test_divide():
#     result = operations.divide(8, 4)
#     assert result == 2

# def test_divide_by_zero():
#     result = operations.divide(10, 0)
#     assert result == "Cannot divide by zero"


# contents of main_program.py
from math_operations import operations

if __name__ == "__main__":
    operations.test_add()
    operations.test_subtract()
    operations.test_multiply()
    operations.test_divide()
    operations.test_divide_by_zero()
