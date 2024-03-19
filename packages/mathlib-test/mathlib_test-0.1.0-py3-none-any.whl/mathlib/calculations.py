"""Provide several sample math calculations.

This module allows the user to make mathematical calculations.

The module contains the following functions:

- `add(a, b)` - Returns the sum of two numbers.
- `subtract(a, b)` - Returns the difference of two numbers.
- `multiply(a, b)` - Returns the product of two numbers.
- `divide(a, b)` - Returns the quotient of two numbers.
"""

import logging

_module_logger = logging.getLogger("mathlib.math")
_module_logger.addHandler(logging.NullHandler())


def add(a: int, b: int) -> int:
    """Returns the sum of two numbers.

    Args:
        a (int): Number a
        b (int): Number b

    Returns:
        int: Result of sum
    """
    msg = "Adding {a} to {b}"
    _module_logger.debug(msg)
    _module_logger.debug("Adding %d to %d", a, b)
    return a + b


def subtract(a: int, b: int) -> int:
    """Returns the difference of two numbers.

    Args:
        a (int): Number a
        b (int): Number b

    Returns:
        int: Result of subtract
    """
    _module_logger.debug(f"Subtracting {b} from {a}")
    return a - b


def multiply(a: int, b: int) -> int:
    """Returns the product of two numbers.

    Args:
        a (int): Number a
        b (int): Number b

    Returns:
        int: Result of multiplication
    """
    _module_logger.debug(f"Multiplication {a} and {b}")
    return a * b


def divide(a: int, b: int) -> int:
    """Returns the quotient of two numbers.

    Args:
        a (int): Number a
        b (int): Number b

    Returns:
        int: Result of division

    Raises:
        ValueError: If b is equal to 0.
    """
    if b == 0:
        err_msg = "Zero division is forbidden"
        raise ValueError(err_msg)

    _module_logger.debug(f"Division {a} and {b}")
    return a / b
