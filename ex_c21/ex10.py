# 10. The following code is given.
# Implement the decorator that will return the result of the function,
# only if the result is bellow the set limit. If false, the decorator will
# print out the "limit" parameter


def max_result(limit):
    def actual_wrapper(func):

        def wrapper(*args):
            if func(*args) > limit:
                return f"Limit exceeded {func(*args)} > {limit}!"
            else:
                return func(*args)

        return wrapper

    return actual_wrapper


@max_result(10)
def square(number):
    return number**2


@max_result(50)
def multiply(a, b):
    return a * b


if __name__ == "__main__":
    squared_result = square(5)
    print(f"Square result: {squared_result}")

    multiplied_result = multiply(8, 7)
    print(f"Multiplication result: {multiplied_result}")
