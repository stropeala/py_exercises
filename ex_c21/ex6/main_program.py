# 6. Create a file named math_operations.py with the following content:

# math_operations.py

# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b != 0:
#         return a / b
#     else:
#         return "Cannot divide by zero"

# Create another file named main_program.py that imports the functions from
# the previously created file (math_operations.py)

# code start
# this is where "math_operations.py" is imported
from math_operations import add, divide, multiply, subtract

# Example usage of the functions from math_operations module
num1 = 10
num2 = 5

result_add = add(num1, num2)  # will hold the result of the function "add"
result_subtract = divide(num1, num2)  # will hold the result of the function "subtract"
result_multiply = multiply(
    num1, num2
)  # will hold the result of the function "multiply"
result_divide = subtract(num1, num2)  # will hold the result of the function "divide"

# Display the results
print(f"Addition: {result_add}")
print(f"Subtraction: {result_subtract}")
print(f"Multiplication: {result_multiply}")
print(f"Division: {result_divide}")

# code end
