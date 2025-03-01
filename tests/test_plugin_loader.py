"""Tests for `plugin_loader.py` plugin loading behavior."""

import runpy
import pytest
import plugin_loader
from unittest.mock import patch
import logging

@pytest.fixture(autouse=True)
def setup_logging(caplog):
    """Ensure log capture is set to DEBUG for all tests."""
    caplog.set_level(logging.DEBUG, logger="plugin_loader")

@patch("plugin_loader.importlib.import_module", side_effect=ImportError("Mocked failure"))
@patch("plugin_loader.pkgutil.iter_modules", return_value=[(None, "fake_module", None)])
def test_load_plugins_import_error(mock_iter_modules, mock_import, caplog):
    """Ensure `load_plugins()` logs an error when a plugin fails to import."""

    plugin_loader.load_plugins()

    # ✅ Ensure import was attempted
    mock_import.assert_called_with("fake_module")

    # ✅ Ensure the error log is captured
    assert "Failed to import fake_module" in caplog.text

def test_load_plugins_success(caplog):
    """Ensure successful plugin loads are logged."""
    with patch("plugin_loader.pkgutil.iter_modules", return_value=[(None, "operations.fake_op", None)]):
        with patch("plugin_loader.importlib.import_module") as mock_import:
            plugin_loader.load_plugins()

    mock_import.assert_called_with("operations.fake_op")
    assert "Successfully loaded plugin: operations.fake_op" in caplog.text

def test_main_called_on_script_execution():
    """Ensure `load_plugins()` is called when script runs as __main__."""
    with patch("importlib.import_module") as mock_import_module:
        runpy.run_path(plugin_loader.__file__, run_name="__main__")

    assert mock_import_module.called, "⚠️ load_plugins() was never called!"

@pytest.mark.parametrize(
    "plugin_name, should_fail, expected_log",
    [
        ("addition", False, "Successfully loaded plugin: addition"),
        ("unknown_plugin", True, "Failed to load plugin: unknown_plugin"),
    ]
)
@patch("plugin_loader.importlib.import_module")
def test_load_plugin(mock_import, caplog, plugin_name, should_fail, expected_log):
    """Test plugin loading behavior (valid and invalid cases)."""

    # ✅ Simulate ImportError only for invalid plugins
    if should_fail:
        mock_import.side_effect = ImportError("Plugin not found")

    if should_fail:
        with pytest.raises(ImportError, match="Plugin not found"):
            plugin_loader.load_plugin(plugin_name)
    else:
        plugin_loader.load_plugin(plugin_name)
        mock_import.assert_called_once_with(plugin_name)

    # ✅ Ensure the expected log message is captured
    assert any(expected_log in record.message for record in caplog.records)

@pytest.mark.usefixtures("setup_logging", "reset_operation_registry")
@patch("plugin_loader.importlib.import_module", side_effect=ImportError("Plugin not found"))
def test_plugin_debug_logging(mock_import, caplog):
    """Ensure debug logs track plugin load attempts."""

    with pytest.raises(ImportError):
        plugin_loader.load_plugin("invalid_plugin")  # ✅ FIXED: Calls `load_plugin`

    # ✅ Ensure the debug log is captured
    assert "Attempting to load plugin: invalid_plugin" in caplog.text
