# tests/test_main_adv.py

import pytest
from unittest.mock import patch, MagicMock
import sys
from vectara_cli.main_adv import main

@pytest.fixture
def mock_client():
    """Fixture to mock the Vectara client."""
    with patch('vectara_cli.utils.utils.get_vectara_client') as mock:
        mock.return_value = MagicMock()
        yield mock

def test_create_ui_command(mock_client):
    """Test the 'create-ui' command."""
    with patch.object(sys, "argv", ["main_adv.py", "create-ui"]):
        main()

def test_advanced_query_adv_command(mock_client):
    """Test the 'advanced-query-adv' command with mocked arguments."""
    test_args = ["main_adv.py", "query", "some", "arguments"]
    with patch.object(sys, "argv", test_args):
        main()

def test_index_text_adv_command(mock_client):
    """Test the 'index-text-adv' command with mocked arguments."""
    test_args = ["main_adv.py", "index-text", "123", "doc123", "Hello, world!"]
    with patch.object(sys, "argv", test_args):
        main()

def test_main_create_corpus_adv(mocker):
    mocker.patch('sys.argv', ['main_advanced.py', 'create-corpus', 'TestCorpus', 'This is a test corpus', '--public'])
    mock_create_corpus_adv = mocker.patch('vectara_cli.commands.create_corpus_adv.create_corpus_adv')
    mock_create_corpus_adv.return_value.index_text.assert_called()

def test_main_delete_corpus_adv(mocker):
    mocker.patch('sys.argv', ['main_advanced.py', 'delete-corpus', '56'])
    mock_delete_corpus_adv = mocker.patch('vectara_cli.commands.delete_corpus_adv.main')
    mock_delete_corpus_adv.return_value.index_text.assert_called()

def test_main_test_upload_document_adv(mocker):
    mocker.patch('sys.argv', ['main_advanced.py', 'upload-document', '56' , "title title", "descriptiondescription", "more text more text"])
    mock_delete_corpus_adv = mocker.patch('vectara_cli.commands.delete_corpus_adv.main')
    mock_delete_corpus_adv.return_value.index_text.assert_called()


def test_unknown_command():
    """Test handling of an unknown command."""
    with patch.object(sys, "argv", ["main_adv.py", "unknown-command"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code != 0  # Expecting a non-zero exit code for unknown commands.

def test_missing_arguments_for_command():
    """Test a command with missing required arguments to ensure it handles errors gracefully."""
    with patch.object(sys, "argv", ["main_adv.py", "index-text"]):
        with pytest.raises(SystemExit) as exc_info:
            main()
    assert exc_info.value.code != 0