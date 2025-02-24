"""Operations Package: Dynamically registers all available operations."""

from .add import Add
from .subtract import Subtract
from .multiply import Multiply
from .divide import Divide

# ✅ Create operation mapping dynamically
operation_mapping = {
    "add": Add,
    "subtract": Subtract,
    "multiply": Multiply,
    "divide": Divide
}

__all__ = ["operation_mapping", "Add", "Subtract", "Multiply", "Divide"]
