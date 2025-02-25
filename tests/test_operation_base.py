"""Tests for the Operation base class and registry behavior."""

import pytest
from operation_base import Operation

class DummyOperation(Operation):
    """Dummy operation class for testing."""

    @classmethod
    def execute(cls, a, b):
        return a + b

@pytest.fixture(autouse=True)
def reset_operation_registry():
    """Fixture to reset registry and register DummyOperation."""
    Operation.registry.clear()
    Operation.register_operation('dummyoperation', DummyOperation)

def test_duplicate_operation_registration_error():
    """Test explicit duplicate registration raises ValueError."""
    with pytest.raises(ValueError, match="already registered"):
        Operation.register_operation('dummyoperation', DummyOperation)

def test_validate_numbers_invalid_input():
    """Invalid inputs should raise TypeError."""
    invalid_inputs = [("abc", 3), (object(), "xyz"), ([], {})]

    for a, b in invalid_inputs:
        with pytest.raises(TypeError, match="Invalid type"):
            DummyOperation.validate_numbers(a, b)

def test_get_operation_success():
    """Successfully retrieve registered operation."""
    operation = Operation.get_operation("dummyoperation")
    assert operation is DummyOperation

def test_get_operation_failure():
    """Unregistered operation retrieval should raise KeyError."""
    with pytest.raises(KeyError, match="not found in registry"):
        Operation.get_operation("nonexistentoperation")

def test_register_operation_success():
    """Automatic registration works for new subclasses."""
    class ExplicitOperation(Operation):
        """Explicitly registered test operation."""
        @classmethod
        def execute(cls, a, b):
            return a * b

    assert Operation.get_operation("explicitoperation") is ExplicitOperation

def test_register_operation_duplicate_error():
    """Explicit duplicate registration raises ValueError."""
    with pytest.raises(ValueError, match="already registered"):
        Operation.register_operation("dummyoperation", DummyOperation)

def test_duplicate_subclass_definition_error():
    """Duplicate subclass definition raises ValueError."""
    class DuplicateOperation(Operation):  # pylint: disable=unused-variable
        """Initial definition to register the class."""
        @classmethod
        def execute(cls, a, b):
            return a + b

    with pytest.raises(ValueError, match="already registered"):
        class DuplicateOperation(Operation):  # pylint: disable=function-redefined,unused-variable
            """Attempted duplicate registration."""
            @classmethod
            def execute(cls, a, b):
                return a - b

def test_register_operation_method_duplicate():
    """Test duplicate registration with explicit method call."""
    class AnotherOperation(Operation):
        """Another test operation."""
        @classmethod
        def execute(cls, a, b):
            return a * b

    # ✅ Attempt explicit registration again to trigger duplication error
    with pytest.raises(ValueError, match="already registered"):
        Operation.register_operation("anotheroperation", AnotherOperation)
