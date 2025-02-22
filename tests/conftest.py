"""Test configuration and dynamic test generation using Faker."""
import pytest
from decimal import Decimal
from faker import Faker

# Import operation_mapping at the TOP
from tests.test_operations import operation_mapping

import sys
import os

# Ensure project root is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

fake = Faker()


@pytest.fixture
def operation_test_cases():
    """Fixture providing static test cases."""
    return [
        ("add", Decimal("2"), Decimal("3"), Decimal("5")),
        ("subtract", Decimal("7"), Decimal("3"), Decimal("4")),
        ("multiply", Decimal("4"), Decimal("3"), Decimal("12")),
        ("divide", Decimal("10"), Decimal("2"), Decimal("5")),
    ]

def generate_test_data(num_record):
    """
    Generate test data dynamically for Calculator operations.

    Args:
        num_record (int): Number of test cases to generate.

    Yields:
        tuple: (op_name, a, b, expected)
    """
    for _ in range(num_record):
        try:
            a = Decimal(fake.random_number(digits=2))
            b = Decimal(fake.random_number(digits=2)) if _ % 4 != 3 else Decimal(fake.random_number(digits=1))

            op_name = fake.random_element(elements=list(operation_mapping.keys()))
            operation_func = operation_mapping[op_name]

            # Ensure b is never zero for division
            if op_name == "divide" and b == Decimal("0"):
                b = Decimal("1")

            expected = operation_func.execute(a, b)

        except (ValueError, TypeError, ArithmeticError) as e:
            print(f"Error generating test data: {e}")
            continue  # Skip faulty test case


        yield op_name, a, b, expected  # ✅ Now includes `op_name`

def pytest_addoption(parser):
    """Allows pytest to recognize --num_record argument."""
    parser.addoption("--num_record", action="store", default=5, type=int, help="Number of test records to generate")

def pytest_generate_tests(metafunc):
    """
    Dynamically parameterizes tests based on --num_record option.
    Ensures expected is only used where necessary.
    """
    if {"op_name", "a", "b", "expected"}.issubset(set(metafunc.fixturenames)):
        # Generate test cases where expected is needed
        num_records = metafunc.config.getoption("num_record")
        parameters = list(generate_test_data(num_records))
        metafunc.parametrize("op_name, a, b, expected", parameters)

    elif {"op_name", "a", "b"}.issubset(set(metafunc.fixturenames)):
        # Generate test cases for validate_numbers where expected is not needed
        num_records = metafunc.config.getoption("num_record")
        parameters = [(op, a, b) for op, a, b, _ in generate_test_data(num_records)]
        metafunc.parametrize("op_name, a, b", parameters)
