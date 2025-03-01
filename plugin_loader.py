"""Plugin Loader Module - Dynamically loads operation plugins"""

import importlib
import logging
import pkgutil
from log_config import logger

# ✅ Store loaded plugins to prevent duplicate imports
_loaded_plugins = set()

def load_plugins():
    """Dynamically loads all operation plugins from the 'operations' package."""
    import operations  # ✅ Prevents circular imports

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

def load_plugin(plugin_name):
    """Loads a plugin by name and raises ImportError if it fails."""
    try:
        logger.debug("Attempting to load plugin: %s", plugin_name)

        # Call import_module to dynamically import the plugin
        module = importlib.import_module(plugin_name)

        logger.info("Successfully loaded plugin: %s", plugin_name)
        return module

    except ImportError as e:
        logger.error("Failed to load plugin: %s - %s", plugin_name, e)
        raise

def main():
    """Only load plugins once to avoid duplicate logs."""
    if not _loaded_plugins:  # ✅ Ensures it only runs once
        load_plugins()

if __name__ == "__main__":
    main()
