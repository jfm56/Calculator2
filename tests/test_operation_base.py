"""Tests for the `Operation` base class and registry behavior."""

import pytest
from operation_base import Operation


def test_operation_registry_keys():
    """Ensure the operation registry contains expected operation names."""
    assert isinstance(Operation.registry, dict), "⚠️ `Operation.registry` should be a dictionary!"


def test_operation_registry_values():
    """Ensure `Operation.get_operation()` correctly retrieves registered classes."""
    for operation_name, operation_class in Operation.registry.items():
        assert Operation.get_operation(operation_name) == operation_class


def test_get_operation_not_found():
    """Ensure `Operation.get_operation()` raises KeyError for unregistered operations."""
    with pytest.raises(KeyError, match="Operation 'nonexistent' not found in registry"):
        Operation.get_operation("nonexistent")
