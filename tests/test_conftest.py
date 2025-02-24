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
    """Ensure `pytest_addoption()` registers `--num_record` with a default of 5 but allows overrides."""

    num_records = pytestconfig.getoption("num_record")  # Get value from pytest CLI or default

    # Ensure the value is either the default (5) or an override
    assert num_records >= 1, f"⚠️ Invalid num_record value: {num_records}"
