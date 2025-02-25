"""Tests for `plugin_loader.py` plugin loading behavior."""

import runpy
from unittest.mock import patch
import plugin_loader


@patch("plugin_loader.importlib.import_module", side_effect=ImportError("Mocked failure"))
@patch("plugin_loader.logger.error")
@patch("plugin_loader.pkgutil.iter_modules", return_value=[(None, "fake_module", None)])
def test_load_plugins_import_error(mock_iter_modules, mock_logger, mock_import):
    """Ensure `load_plugins()` logs an error when a plugin fails to import."""
    plugin_loader.load_plugins()

    mock_import.assert_called_with("fake_module")
    mock_logger.assert_called_once()
    actual_args = mock_logger.call_args[0]
    assert actual_args[0] == "Failed to import %s: %s"
    assert actual_args[1] == "fake_module"
    assert isinstance(actual_args[2], ImportError)
    assert str(actual_args[2]) == "Mocked failure"

def test_load_plugins_success(caplog):
    """Ensure successful plugin loads are logged."""
    with patch("plugin_loader.pkgutil.iter_modules", return_value=[(None, "operations.fake_op", None)]):
        with patch("plugin_loader.importlib.import_module") as mock_import:
            plugin_loader.load_plugins()

    mock_import.assert_called_with("operations.fake_op")
    assert "Successfully loaded plugin: operations.fake_op" in caplog.text

def test_main_called_on_script_execution():
    """Ensure `load_plugins()` is called when script runs as __main__."""
    # Mock import_module to prevent actual plugin loading during test execution
    with patch("importlib.import_module") as mock_import_module:
        runpy.run_path(plugin_loader.__file__, run_name="__main__")

    # Check if import_module was called, proving load_plugins() executed
    assert mock_import_module.called, "⚠️ load_plugins() was never called!"
