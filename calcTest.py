import pytest
from calculator import Calculator


@pytest.fixture
def calculator():
    return Calculator()


def test_add(calculator):
    assert calculator.add(2, 3) == 5
    assert calculator.add(-2, 3) == 1
    assert calculator.add(0, 0) == 0


def test_subtract(calculator):
    assert calculator.subtract(5, 2) == 3
    assert calculator.subtract(-5, 2) == -7
    assert calculator.subtract(0, 0) == 0


def test_multiply(calculator):
    assert calculator.multiply(2, 3) == 6
    assert calculator.multiply(-2, 3) == -6
    assert calculator.multiply(0, 5) == 0


def test_divide(calculator):
    assert calculator.divide(6, 3) == 2
    assert calculator.divide(-6, 3) == -2
    assert calculator.divide(0, 5) == 0


def test_divide_by_zero(calculator):
    with pytest.raises(ZeroDivisionError):
        calculator.divide(6, 0)