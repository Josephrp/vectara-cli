# tests/test_advanced_query.py

import pytest
from unittest.mock import Mock, patch
from vectara_cli.commands.advanced_query import main

class MockClientResponse:
    def __init__(self, items):
        self.items = items
    
    def __iter__(self):
        return iter(self.items)

@pytest.fixture
def vectara_client_mock():
    client_mock = Mock()
    client_mock.advanced_query = Mock()
    return client_mock

def test_main_with_few_arguments(capsys, vectara_client_mock):
    with patch('vectara_cli.commands.advanced_query.advanced_query_help') as mock_help_function:
        main(["script_name", "query", "text"], vectara_client_mock)
        mock_help_function.assert_called_once()
        captured = capsys.readouterr()
        assert "Invalid" not in captured.out

@pytest.mark.parametrize("context_config_json, summary_config_json, is_valid", [
    ('{}', '{}', True),
    ('{"invalid_json": true', '{}', False),  # Invalid JSON
    ('{}', '{"invalid_json": true', False),  # Invalid JSON
    ('{"context_length": "invalid"}', '{}', False),  # Invalid type in context_config
])
def test_main_with_invalid_configs(context_config_json, summary_config_json, is_valid, vectara_client_mock, capsys):
    arguments = ["script_name", "query", "text", "2", "1", context_config_json, summary_config_json]
    
    main(arguments, vectara_client_mock)
    captured = capsys.readouterr()

    if is_valid:
        vectara_client_mock.advanced_query.assert_called()
    else:
        assert "Invalid" in captured.out or "Error" in captured.out
        vectara_client_mock.advanced_query.assert_not_called()

def test_advanced_query_response(vectara_client_mock, capsys):
    vectara_client_mock.advanced_query.return_value = MockClientResponse(["Result 1", "Result 2"])
    main(["script_name", "query", "text", "2", "1"], vectara_client_mock)

    captured = capsys.readouterr()
    assert "Result 1" in captured.out
    assert "Result 2" in captured.out

def test_no_advanced_query_response(vectara_client_mock, capsys):
    vectara_client_mock.advanced_query.return_value = None
    main(["script_name", "query", "text", "2", "1"], vectara_client_mock)

    captured = capsys.readouterr()
    assert "No response received from the advanced query." in captured.out
