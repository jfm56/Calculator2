"""Test for environment variables"""
from app.env import get_env_var
from app.env import LOG_LEVEL, PLUGIN_DIRECTORY, DATABASE_URL


def test_get_env_var_existing(monkeypatch):
    """Test retrieving an existing environment variable."""
    monkeypatch.setenv("TEST_VAR", "VALUE")
    assert get_env_var("TEST_VAR") == "VALUE"

def test_get_env_var_default():
    """Test default value when env variable is missing."""
    assert get_env_var("NON_EXISTENT_VAR", "DEFAULT") == "DEFAULT"

print("LOG_LEVEL:", LOG_LEVEL)
print("PLUGIN_DIRECTORY:", PLUGIN_DIRECTORY)
print("DATABASE_URL:", DATABASE_URL)
