# tests/test_main.py
from unittest.mock import patch, MagicMock
import pytest
from vectara_cli.main import main, get_command_mapping
import sys

# # Test the handling of the 'help' command
# def test_help_command():
#     with patch('builtins.print') as mock_print:
#         with patch.object(sys, 'argv', ['main.py', 'help']):
#             main()
#             mock_print.assert_called()  # Ensuring help text is printed

# Test the successful execution of a valid command
@patch('vectara_cli.main.get_vectara_client')
@patch('vectara_cli.commands.index_document.main')
def test_valid_command_execution(mock_index_document_main, mock_get_vectara_client):
    # Mocking get_vectara_client and a specific command function, index_document.main
    vectara_client_mock = MagicMock()
    mock_get_vectara_client.return_value = vectara_client_mock

    with patch.object(sys, 'argv', ['main.py', 'index-document', 'dummy_arg']):
        main()

    # Verify that index_document.main was called with the expected arguments, including the mocked vectara client
    mock_index_document_main.assert_called_once_with(['dummy_arg'], vectara_client_mock)

# Test handling of 'set-api-keys' with incorrect number of arguments
def test_set_api_keys_incorrect_args():
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'argv', ['main.py', 'set-api-keys', 'only_one_arg']):
            with pytest.raises(SystemExit) as exc_info:
                main()
            assert exc_info.value.code == 1  # Expecting a non-zero exit due to error
            mock_print.assert_called_with("Error: set-api-keys requires exactly 2 arguments: customer_id and api_key.")

# Test unknown command handling
def test_unknown_command_stderr():
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'argv', ['main.py', 'nonexistent-command']):
            with pytest.raises(SystemExit) as exc_info:
                main()
    assert exc_info.value.code == 1
    mock_print.assert_called_with("Unknown command: nonexistent-command")

# Verifying that all expected commands are mapped properly
def test_get_command_mapping_completeness():
    expected_commands = [
        "index-document", "query", "create-corpus", "delete-corpus",
        "span-text", "span-enhance-folder", "upload-document", "upload-enriched-text",
        "nerdspan-upsert-folder", "rebel-upsert-folder", "index-text", "create-ui",
        "upload-folder"
    ]
    command_mapping = get_command_mapping()
    assert all(command in command_mapping for command in expected_commands)
