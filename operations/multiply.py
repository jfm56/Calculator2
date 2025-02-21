"""Multplication Plugin Operation"""
from decimal import Decimal
from operation_base import Operation

class Multiply(Operation):
    """Performs multiplication of two numbers."""

    @staticmethod
    def execute(a: Decimal, b: Decimal) -> Decimal:
        """Returns the product of two numbers."""
        Multiply.validate_numbers(a, b)
        return a * b

    @classmethod
    def validate_numbers(cls, a: Decimal, b: Decimal) -> None:
        """Validates that both inputs are numbers and converts them to Decimal if needed."""
        if not isinstance(a, Decimal):
            try:
                a = Decimal(a)
            except Exception as exc:
                raise TypeError(f"Invalid type for 'a': {type(a).__name__}, expected Decimal-compatible.") from exc

        if not isinstance(b, Decimal):
            try:
                b = Decimal(b)
            except Exception as exc:
                raise TypeError(f"Invalid type for 'b': {type(b).__name__}, expected Decimal-compatible.") from exc
