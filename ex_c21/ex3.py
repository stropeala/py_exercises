# 3. Add the necessary clause(s) to the code below so that in case the
# ZeroDivisionError exception is raised then the program prints out "Zero!" to the screen.

# code start
try:
    print(25 % 0)
except ZeroDivisionError as error:
    print(f"ERROR!: {error}")
# code end
