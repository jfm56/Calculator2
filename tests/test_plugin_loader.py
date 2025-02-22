"""Tests for Plugin Loader"""
from operation_base import Operation

def test_plugins_loaded():
    """Ensures plugins are loaded into the registry."""
    assert "add" in Operation.registry
    assert "subtract" in Operation.registry
    assert "multiply" in Operation.registry
    assert "divide" in Operation.registry

def test_operation_retrieval():
    """Ensures that retrieving operations dynamically works."""
    add_op = Operation.get_operation("add")
    assert add_op is not None
    assert add_op.__name__ == "Add"
