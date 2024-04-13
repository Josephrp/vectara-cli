# /tests/test_create_corpus.py

import pytest
from unittest.mock import Mock, patch
import sys
from vectara_cli.commands.create_corpus import parse_json_arg, parse_args, main
from vectara_cli.data.defaults import CorpusDefaults

@pytest.fixture
def mock_sys_argv_minimal():
    """Fixture to mock sys.argv with minimal valid args"""
    with patch.object(sys, 'argv', ['create_corpus.py', 'test_name', 'test_description']):
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
    with pytest.raises(ValueError) as excinfo:
        parse_json_arg(json_input)
    assert "Invalid JSON format" in str(excinfo.value)

@pytest.mark.parametrize("args, expected_output", [
    (['test_name', 'test_description'], ('test_name', 'test_description', CorpusDefaults.get_defaults())),
    (['test_name', 'test_description', '--custom_dimensions={"dimension": "value"}'], 
     ('test_name', 'test_description', {'customDimensions': {"dimension": "value"}, **CorpusDefaults.get_defaults()})),
    (['test_name', 'test_description', '--encoder_id=123'], 
     ('test_name', 'test_description', {'encoderId': 123, **CorpusDefaults.get_defaults()}))
])
def test_parse_args_valid(args, expected_output):
    assert parse_args(args) == expected_output

def test_parse_args_insufficient_arguments(mock_sys_argv_minimal):
    with pytest.raises(SystemExit) as e:
        main(sys.argv, vectara_client_mock())  # Using mocker for vectara_client
    assert e.value.code == 1

def test_main_functionality(mock_sys_argv_minimal, vectara_client_mock):
    main(sys.argv, vectara_client_mock)
    vectara_client_mock.create_corpus.assert_called_once()