"""Test for config."""

from app.config import Config

def test_config_values():
    """Ensure environment variables are correctly loaded into Config."""
    assert isinstance(Config.LOG_LEVEL, str)
    assert isinstance(Config.PLUGIN_DIRECTORY, str)
    assert isinstance(Config.DATABASE_URL, str)

    assert Config.LOG_LEVEL in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
    assert Config.PLUGIN_DIRECTORY  # Should not be empty
    assert Config.DATABASE_URL  # Should not be empty
