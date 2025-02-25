"""Plugin Loader Module - Dynamically loads operation plugins"""
import logging
import importlib
import pkgutil

# ✅ Logging for better debugging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# ✅ Store loaded plugins to prevent duplicate imports
_loaded_plugins = set()

def load_plugins():
    """Dynamically loads all operation plugins from the 'operations' package."""
    import operations  # ✅ Moved here to prevent circular imports

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

def main():
    load_plugins()

if __name__ == "__main__":
    main()
