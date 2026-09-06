import pytest

from src.calculator import Calculator


def test_addition():
    calculator = Calculator()

    assert calculator.calc("2 + 3") == "5"


def test_multiplication():
    calculator = Calculator()

    assert calculator.calc("4 * 5") == "20"


def test_complex_expression():
    calculator = Calculator()

    assert calculator.calc("2 + 3 * 4") == "14"


def test_reject_function_call():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.calc('__import__("os").system("ls")')


def test_reject_variable():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.calc("some_variable + 1")


def test_reject_string():
    calculator = Calculator()

    with pytest.raises(ValueError):
        calculator.calc('"hello"')