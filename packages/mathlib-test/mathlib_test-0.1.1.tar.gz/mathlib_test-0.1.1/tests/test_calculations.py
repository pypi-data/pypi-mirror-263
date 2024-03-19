"""Math test module."""

import pytest

from mathlib import add, divide, multiply, subtract


def test_add():
    assert add(2, 2) == 4


def test_subtract():
    assert subtract(4, 2) == 2


def test_division():
    assert divide(4, 2) == 2


def test_multiply():
    assert multiply(2, 2) == 4


def test_divide_rise_value_error():
    with pytest.raises(ValueError, match="Zero division is forbidden"):
        divide(2, 0)
