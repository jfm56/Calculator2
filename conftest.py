"""Test configuration and dynamic test generation using Faker."""
from plugin_loader import load_plugins
load_plugins()  # ✅ Ensure plugins are loaded before tests

import warnings
import pytest
from decimal import Decimal, InvalidOperation
from faker import Faker
import sys
import os
from operation_base import Operation
from operations.operation_mapping import operation_mapping


sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

fake = Faker()

@pytest.fixture(scope="function", autouse=True)
def reset_operation_registry():
    """Ensures `Operation.registry` is cleared before each test."""
    Operation.registry.clear()


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
    """Generate test data dynamically for Calculator operations."""
    for _ in range(num_record):
        try:
            a = Decimal(fake.random_number(digits=2))
            b = Decimal(fake.random_number(digits=2))

            op_name = fake.random_element(elements=list(operation_mapping.keys()))
            operation_func = operation_mapping[op_name]

            if op_name == "divide":
                b = b if b != 0 else Decimal("1")

            expected = operation_func.execute(a, b)

        except (ValueError, TypeError, InvalidOperation) as e:
            continue  # ✅ Skip faulty test cases

        yield op_name, a, b, expected


def pytest_addoption(parser):
    """Allows pytest to recognize --num_record argument."""
    parser.addoption(
        "--num_record", action="store", default=5, type=int, help="Number of test records to generate"
    )


def pytest_generate_tests(metafunc):
    """Dynamically parameterizes tests based on --num_record option."""
    num_records = metafunc.config.getoption("num_record")
    parameters = list(generate_test_data(num_records))

    param_map = {
        ("operation_name", "a", "b", "expected"): parameters,
        ("operation_name", "a", "b"): [(op, a, b) for op, a, b, _ in parameters],
    }

    # ✅ Only apply parameterization if all required fixtures are available
    matched_param = next(
        ((keys, values) for keys, values in param_map.items() if set(keys).issubset(metafunc.fixturenames)),
        None
    )

    if matched_param:
        keys, values = matched_param
        metafunc.parametrize(",".join(keys), values)  # ✅ Correct argument structure
    elif metafunc.fixturenames:
        # ✅ Only warn if it's an actual missing fixture issue
        missing_fixtures = [f for f in metafunc.fixturenames if f not in param_map]
        if missing_fixtures:
            warnings.warn(
                f"⚠️ Skipping test case generation: Missing required fixtures {missing_fixtures}",
                UserWarning,
            )
