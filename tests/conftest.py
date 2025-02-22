"""Test includes faker to generate test data."""

# pylint: disable=wrong-import-position, wrong-import-order, global-statement, unnecessary-dunder-call
# flake8: noqa

import sys
import os

# Add project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from decimal import Decimal
import pytest
from faker import Faker

from operations.subtract import Subtract
from operations.add import Add
from operations.multiply import Multiply
from operations.divide import Divide

fake = Faker()

@pytest.fixture
def operation_test_cases():
    """Fixture that provides test cases for arithmetic operations."""
    return [
        (Add, Decimal("2"), Decimal("3"), Decimal("5")),
        (Subtract, Decimal("7"), Decimal("3"), Decimal("4")),
        (Multiply, Decimal("4"), Decimal("3"), Decimal("12")),
        (Divide, Decimal("10"), Decimal("2"), Decimal("5")),
    ]

def generate_test_data(num_record):
    """
    Generate test data dynamically for Calculator operations.

    Args:
        num_records (int): Number of test cases to generate.

    Yields:
        tuple: (a, b, operation_name, operation_function, expected_result)
    """
    operation_mapping = {
        'add': Add,
        'subtract': Subtract,
        'multiply': Multiply,
        'divide': Divide
    }

    for _ in range(num_record):
        a = Decimal(fake.random_number(digits=2))
        b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))

        operation_name = fake.random_element(elements=list(operation_mapping.keys()))
        operation_func = operation_mapping[operation_name]

        # Ensure b is never zero for division
        if operation_func is Divide and b == Decimal('0'):
            b = Decimal('1')

        try:
            expected = operation_func.execute(a, b)
        except ZeroDivisionError:
            expected = "ZeroDivisionError"

        yield a, b, operation_name, operation_func, expected

def pytest_addoption(parser):
    """Allows pytest to recognize --num_record argument."""
    parser.addoption("--num_record", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """Dynamically parameterizes tests based on the --num_record option."""
    if {"a", "b", "operation", "expected"}.intersection(set(metafunc.fixturenames)):  # Fixed missing "operation"
        num_records = metafunc.config.getoption("num_record")

        # Generate test cases
        parameters = list(generate_test_data(num_records))

        metafunc.parametrize("a, b, operation, expected", parameters)  # Fixed wrong function call
