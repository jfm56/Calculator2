"""Tests for `conftest.py` utilities and configurations."""
from decimal import Decimal
from conftest import generate_test_data

def test_generate_test_data():
    """Ensure `generate_test_data()` produces valid test cases."""
    test_cases = list(generate_test_data(5))

    assert len(test_cases) > 0  # ✅ Ensure cases exist
    for op_name, a, b, expected in test_cases:
        assert isinstance(op_name, str)
        assert isinstance(a, Decimal)
        assert isinstance(b, Decimal)
        assert isinstance(expected, Decimal)


def test_pytest_addoption(pytestconfig):
    """Ensure `pytest_addoption()` properly registers `--num_record`."""

    # ✅ Verify that `--num_record` exists
    assert pytestconfig.getoption("num_record") == 5  # ✅ Default value should be 5

    # ✅ Simulate passing `--num_record 10`
    pytestconfig.option.num_record = 10  # ✅ Safely modify config for test
    assert pytestconfig.getoption("num_record") == 10  # ✅ Ensure it's updated
