# 9. The following code is given.
# Implement a decorator that will calculate and print the total duration of the function.

# code start
import datetime
import time


def timer():
    def wrapper(func):
        print(str(datetime.datetime.now()))
        func()
        print(str(datetime.datetime.now()))

    return wrapper


@timer()
def slow_function():
    # Simulate a slow function
    time.sleep(2)
    print("Function executed!")


# code end
