"""Addition Plugin Opperation"""
from decimal import Decimal
from operation_base import Operation

class Add(Operation):
    """Performs addition of two numbers."""

    @staticmethod
    def exicute (a: Decimal, b: Decimal)-> Decimal:
        """Returns the sum of two numbers."""
        Operation.validate_numbers(a, b)
        return a + b
