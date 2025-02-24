"""Tests for arithmetic operations and validation."""

from decimal import Decimal
import pytest
from operations.operation_mapping import operation_mapping
from operation_base import Operation

# ✅ SINGLE PARAMETERIZATION FIXTURE TO PREVENT DUPLICATION
@pytest.fixture(params=[
    ("add", Decimal("5"), Decimal("3"), Decimal("8")),
    ("subtract", Decimal("10"), Decimal("4"), Decimal("6")),
    ("multiply", Decimal("2"), Decimal("3"), Decimal("6")),
    ("divide", Decimal("9"), Decimal("3"), Decimal("3")),
    ("divide", Decimal("5"), Decimal("2"), Decimal("2.5")),
    ("multiply", Decimal("-4"), Decimal("3"), Decimal("-12")),
    ("multiply", Decimal("1000000"), Decimal("1000000"), Decimal("1000000000000")),
    ("multiply", Decimal("0.5"), Decimal("0.5"), Decimal("0.25")),
])
def operation_test_case(request):
    """Fixture to supply arithmetic test cases."""
    return request.param  # (operation_name, a, b, expected)


def test_operations_execution(operation_test_case):
    """Tests arithmetic operations execute correctly."""
    operation_name, a, b, expected = operation_test_case
    operation = operation_mapping[operation_name]
    assert operation.execute(a, b) == expected


def test_division_by_zero():
    """Ensure division by zero raises ZeroDivisionError."""
    with pytest.raises(ZeroDivisionError):
        operation_mapping["divide"].execute(Decimal("10"), Decimal("0"))


@pytest.mark.parametrize("valid_op, a, b, expected", [
    ("add", Decimal("3.5"), Decimal("2"), Decimal("5.5")),  # Addition
    ("multiply", 10, 5, Decimal("50")),  # Multiplication
])
def test_valid_numbers_conversion(valid_op, a, b, expected):
    """Tests that validate_numbers correctly converts types before execution."""
    assert valid_op in operation_mapping, f"⚠️ {valid_op} is missing!"
    assert operation_mapping[valid_op].execute(a, b) == expected  # ✅ Uses expected result directly


@pytest.mark.parametrize(
    "a, b",
    [
        ("invalid", "3"),
        (None, 3),
        ([1, 2], 3),
        ({1: 2}, 3),
        (object(), 3),
    ],
)
def test_validate_numbers_invalid(a, b):
    """Ensure `validate_numbers` rejects invalid types."""
    for _, operation in operation_mapping.items():  # ✅ More Pythonic
        with pytest.raises(TypeError):
            operation.validate_numbers(a, b)


def test_get_operation_not_found():
    """Ensure `get_operation()` raises KeyError when an operation is not found."""
    with pytest.raises(KeyError, match=r"Operation 'nonexistent' not found in registry."):
        Operation.get_operation("nonexistent")


def test_validate_numbers_invalid_type():
    """Ensure `validate_numbers()` raises TypeError for invalid inputs."""
    with pytest.raises(TypeError, match="Invalid type"):
        Operation.validate_numbers("abc", "xyz")
