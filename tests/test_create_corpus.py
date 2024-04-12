# /tests/test_create_corpus.py

import pytest
from unittest.mock import Mock, patch
import sys

from vectara_cli.commands.create_corpus import parse_json_arg, parse_args, main


@pytest.fixture
def mock_sys_argv():
    """Fixture to mock sys.argv"""
    with patch.object(sys, 'argv', ['create_corpus_advanced.py']):
        yield


@pytest.fixture
def vectara_client_mock():
    """Fixture to create a mock vectara_client instance"""
    mock = Mock()
    mock.create_corpus.return_value = {"message": "Corpus created successfully"}
    return mock


def test_parse_json_arg_valid():
    json_input = '{"key": "value"}'
    expected_output = {"key": "value"}
    assert parse_json_arg(json_input) == expected_output


def test_parse_json_arg_invalid():
    json_input = '{key: "value"}'  # Invalid JSON format
    with pytest.raises(ValueError) as execinfo:
        parse_json_arg(json_input)
    assert "Invalid JSON format" in str(execinfo.value)


@pytest.mark.parametrize("args, expected_name, expected_description, expected_options", [
    (['test_name', 'test_description'], 'test_name', 'test_description', {'customDimensions': {}}),
    (['test_name', 'test_description', '--custom_dimensions={"dimension": "value"}'], 'test_name', 'test_description', {'customDimensions': {"dimension": "value"}}),
    (['test_name', 'test_description', '--encoder_id=123'], 'test_name', 'test_description', {'encoderId': '123'}),
])
def test_parse_args_valid(args, expected_name, expected_description, expected_options):
    name, description, options = parse_args(args)
    assert name == expected_name
    assert description == expected_description
    assert options == expected_options


def test_parse_args_insufficient_arguments(mock_sys_argv):
    with pytest.raises(SystemExit) as e:
        main()  # Assuming main doesn't need explicit sys.argv due to mock
    assert e.value.code == 1


def test_main_functionality(vectara_client_mock):
    with patch.object(sys, 'argv', ['create_corpus_advanced.py', 'test_name', 'test_description']):
        main(vectara_client_mock)
    vectara_client_mock.create_corpus.assert_called_with(
        name='test_name',
        description='test_description',
        options={})  # Assuming the main function formats call like this based on description
