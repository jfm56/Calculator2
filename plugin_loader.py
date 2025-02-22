"""
Plugin Loader Module

This module dynamically loads all mathematical operation plugins 
from the `operations` package. It ensures that any new operation 
subclasses of `Operation` are automatically registered and available 
for use in the calculator.

Usage:
    - This module is automatically executed when imported.
    - It scans the `operations` directory for all Python modules.
    - It dynamically imports each module, ensuring they are registered.

Functions:
    - load_plugins(): Scans the `operations` package and imports all modules.

Example:
    # Simply importing this module will load all plugins
    import plugin_loader

    # Operations will be registered and available in Operation.registry
"""
import logging
import importlib
import pkgutil
import operations

# Logging for better debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Track loaded modules to prevent duplicate imports
_loaded_plugins = set()

def load_plugins():
    """Dynamically loads all operation plugins from the 'operations' package."""
    package = operations

    for _, module_name, _ in pkgutil.iter_modules(package.__path__, package.__name__ + "."):
        if module_name in _loaded_plugins:
            logger.debug("Skipping already loaded plugin: %s", module_name)
            continue

        try:
            importlib.import_module(module_name)
            _loaded_plugins.add(module_name)
            logger.info("Successfully loaded plugin: %s", module_name)
        except ImportError as e:
            logger.error("Failed to import %s: %s", module_name, e)

# Load all plugins at runtime
load_plugins()
