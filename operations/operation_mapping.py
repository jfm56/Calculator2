"""Operation Mapping Module"""
from operations.add import Add
from operations.subtract import Subtract
from operations.multiply import Multiply
from operations.divide import Divide

# ✅ Ensure this is a dictionary
operation_mapping = {
    "add": Add,
    "subtract": Subtract,
    "multiply": Multiply,
    "divide": Divide,
}
