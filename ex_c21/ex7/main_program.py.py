# 7. Create a file named shapes.py (content down bellow) in a new python package. Import
# the functions from the "shapes.py" file in the "main_program.py", in order for the code
# to run properly.

# content of shapes.py

# def area_of_square(side_length):
#     return side_length ** 2

# def area_of_circle(radius):
#     import math
#     return math.pi * (radius ** 2)


# content of main_program.py
import shapes

side_length = 5
radius = 3

square_area = shapes.area_of_square(side_length)
circle_area = shapes.area_of_circle(radius)

# Display the results
print(f"Area of square with side length {side_length}: {square_area}")
print(f"Area of circle with radius {radius}: {circle_area}")
