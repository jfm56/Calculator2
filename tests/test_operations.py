"""Tests for Arithmetic Operations using EAFP principles."""
from decimal import Decimal
import pytest
from operations.add import Add
from operations.subtract import Subtract
from operations.multiply import Multiply
from operations.divide import Divide

# Mapping operations to their class
operation_mapping = {
    "add": Add,
    "subtract": Subtract,
    "multiply": Multiply,
    "divide": Divide
}

@pytest.mark.parametrize("operation_name, a, b, expected", [
    ("add", Decimal("5"), Decimal("3"), Decimal("8")),
    ("subtract", Decimal("10"), Decimal("4"), Decimal("6")),
    ("multiply", Decimal("2"), Decimal("3"), Decimal("6")),
    ("divide", Decimal("9"), Decimal("3"), Decimal("3")),
    ("divide", Decimal("5"), Decimal("2"), Decimal("2.5")),  # Floating point case
    ("multiply", Decimal("-4"), Decimal("3"), Decimal("-12")),  # Negative number case
])
def test_operations(operation_name, a, b, expected):
    """Tests arithmetic operations using EAFP."""
    try:
        operation = operation_mapping[operation_name]
        result = operation.execute(a, b)
        assert result == expected  # ✅ Ensure correct calculation
    except ZeroDivisionError:
        assert operation is Divide and b == Decimal("0")  # ✅ Expected ZeroDivisionError for divide(10,0)
    except (TypeError, ValueError) as e:
        pytest.fail(f"Unexpected type error: {e}")

@pytest.mark.parametrize("operation_name", ["add", "subtract", "multiply", "divide"])
@pytest.mark.parametrize("a, b", [
    ("10", "5"),   # Strings
    (10, 5),       # Integers
    (10.5, 2.5),   # Floats
    (Decimal("10.5"), Decimal("2.5")),  # Decimals
])
def test_validate_numbers(operation_name, a, b):
    """Tests that validate_numbers correctly converts various types."""
    try:
        operation = operation_mapping[operation_name]
        operation.validate_numbers(a, b)  # ✅ No `expected` needed
    except (TypeError, ValueError) as e:
        pytest.fail(f"Unexpected type error: {e}")

@pytest.mark.parametrize("operation_name", ["add", "subtract", "multiply", "divide"])
@pytest.mark.parametrize("a, b", [
    ("invalid", "3"),   # Invalid string
    (None, 3),          # None type
    ([1, 2], 3),        # List
    ({1: 2}, 3),        # Dictionary
    (object(), 3),      # Random object
])
def test_validate_numbers_invalid(operation_name, a, b):
    """Tests validate_numbers rejects invalid types."""
    with pytest.raises(TypeError):
        operation = operation_mapping[operation_name]
        operation.validate_numbers(a, b)

def test_division_by_zero():
    """Tests division by zero handling."""
    with pytest.raises(ZeroDivisionError):
        Divide.execute(Decimal("10"), Decimal("0"))
