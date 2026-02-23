# contents of operations.py
import math_ops as operations


def test_add():
    result = operations.add(3, 5)
    assert result == 8


def test_subtract():
    result = operations.subtract(10, 4)
    assert result == 6


def test_multiply():
    result = operations.multiply(2, 6)
    assert result == 12


def test_divide():
    result = operations.divide(8, 4)
    assert result == 2


def test_divide_by_zero():
    result = operations.divide(10, 0)
    assert result == "Cannot divide by zero"
