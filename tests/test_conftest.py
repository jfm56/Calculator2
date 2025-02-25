"""Tests for `conftest.py` utilities and dynamic test generation."""
from decimal import Decimal, InvalidOperation
from unittest.mock import MagicMock, patch
import pytest
from conftest import pytest_addoption, pytest_generate_tests, generate_test_data
from operations.operation_mapping import operation_mapping
from faker import Faker

fake = Faker()

def test_pytest_addoption():
    """Verify CLI option `--num_record` setup."""
    parser = MagicMock()
    pytest_addoption(parser)
    parser.addoption.assert_called_once_with(
        "--num_record",
        action="store",
        default=5,
        type=int,
        help="Number of test records to generate"
    )

def test_pytest_generate_tests():
    """Check dynamic parametrization based on provided fixtures."""
    metafunc = MagicMock()
    metafunc.config.getoption.return_value = 1
    metafunc.fixturenames = ["operation_name", "a", "b", "expected"]

    pytest_generate_tests(metafunc)

    metafunc.parametrize.assert_called_once()
    args, _ = metafunc.parametrize.call_args
    assert args[0] == "operation_name,a,b,expected"
    assert len(args[1]) == 1

def test_generate_test_data():
    """Validate generated test data."""
    test_cases = list(generate_test_data(5))
    assert len(test_cases) == 5
    for op_name, a, b, expected in test_cases:
        assert op_name in operation_mapping
        assert isinstance(a, Decimal) and isinstance(b, Decimal)
        assert isinstance(expected, Decimal)

def test_pytest_generate_tests_warns():
    """Ensure pytest_generate_tests warns if fixtures are missing."""
    metafunc = MagicMock()
    metafunc.config.getoption.return_value = 1
    metafunc.fixturenames = ["unrelated_fixture"]

    with pytest.warns(UserWarning, match="⚠️ Skipping test case generation"):
        pytest_generate_tests(metafunc)

@patch('conftest.Decimal', side_effect=InvalidOperation)
def test_generate_test_data_invalid_operation(mock_decimal):
    """Check handling of InvalidOperation during test data generation."""
    results = list(generate_test_data(5))
    assert not results, "Expected no results due to InvalidOperation exception."

def test_operation_test_cases_fixture(operation_test_cases):
    """Test fixture operation_test_cases returns expected test data."""
    assert len(operation_test_cases) == 4
    assert operation_test_cases[0] == ("add", Decimal("2"), Decimal("3"), Decimal("5"))
    assert operation_test_cases[-1] == ("divide", Decimal("10"), Decimal("2"), Decimal("5"))
