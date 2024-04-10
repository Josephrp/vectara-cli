# tests/test_main.py

from unittest.mock import patch
import sys
import pytest
from vectara_cli.main import main


def test_valid_command():
    # Simulate running the script with a valid command
    with patch.object(sys, "argv", ["main.py", "help"]):
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
def test_unknown_command_stderr(capfd):
    with patch.object(sys, 'argv', ['main.py', 'nonexistent-command']):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code == 1
    out, err = capfd.readouterr()
    assert "vectara: 'nonexistent-command' is not a vectara command. See 'vectara --help'." in out

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

# Test handling of 'set-api-keys' with correct number of arguments
@patch('vectara_cli.main.set_api_keys_main')
def test_set_api_keys_correct_args(mock_set_api_keys_main):
    with patch.object(sys, 'argv', ['main.py', 'set-api-keys', 'customer_id', 'api_key']):
        main()
    # Verify that set_api_keys_main was called with the expected arguments
    mock_set_api_keys_main.assert_called_once_with('customer_id', 'api_key')

