# tests/index_text_adv.py

import pytest
from unittest.mock import patch, MagicMock
from vectara_cli.commands.index_text_adv import main as index_text_adv_main
from vectara_cli.commands.index_text_adv import parse_args

@pytest.fixture
def mock_client():
    """Fixture to mock the Vectara client."""
    mock = MagicMock()
    return mock

def test_index_text_adv_success(mock_client):
    """Test successful advanced text indexing."""
    args = ["123", "doc123", "Hello, world!", "--context", "test context", "--metadata_json", '{"key":"value"}', "--custom_dims", "dim1=1.0", "dim2=2.0"]
    with patch('vectara_cli.commands.index_text_adv.parse_args', return_value=MagicMock(corpus_id=123, document_id="doc123", text="Hello, world!", context="test context", metadata_json='{"key":"value"}', custom_dims=["dim1=1.0", "dim2=2.0"])):
        index_text_adv_main(args, mock_client)
    mock_client.index_text.assert_called_once()

def test_index_text_adv_failure_invalid_custom_dims(mock_client):
    """Test failure due to invalid custom dimensions format."""
    args = ["123", "doc123", "Hello, world!", "--custom_dims", "dim1"]
    with pytest.raises(ValueError):
        index_text_adv_main(args, mock_client)

# Assuming parse_custom_dimensions is accessible for testing
from vectara_cli.commands.index_text_adv import parse_custom_dimensions

def test_parse_custom_dimensions_success():
    """Test parsing of valid custom dimensions."""
    custom_dims = ["size=10.5", "age=2"]
    expected = [{"name": "size", "value": 10.5}, {"name": "age", "value": 2.0}]
    assert parse_custom_dimensions(custom_dims) == expected

def test_parse_custom_dimensions_failure():
    """Test parsing with an invalid custom dimension format."""
    custom_dims = ["invalid_format"]
    with pytest.raises(ValueError):
        parse_custom_dimensions(custom_dims)

# Test parse_args
def test_parse_args_success(monkeypatch):
    """Test successful argument parsing."""
    test_args = ["prog", "123", "doc123", "Hello, world!", "--context", "test context", "--metadata_json", '{"key":"value"}', "--custom_dims", "dim1=1.0", "dim2=2.0"]
    monkeypatch.setattr(sys, 'argv', test_args)
    args = parse_args()
    assert args.corpus_id == 123
    assert args.document_id == "doc123"
    assert args.text == "Hello, world!"
    assert args.context == "test context"
    assert args.metadata_json == '{"key":"value"}'
    assert args.custom_dims == ["dim1=1.0", "dim2=2.0"]

def test_parse_args_failure(monkeypatch):
    """Test argument parsing with missing required arguments."""
    test_args = ["prog"]
    monkeypatch.setattr(sys, 'argv', test_args)
    with pytest.raises(SystemExit):
        parse_args()
        
# Integration Testing 

def test_index_text_adv_integration_success(mock_client):
    """Integration test for successful text indexing with all parameters."""
    args = ["123", "doc123", "Hello, world!", "--context", "test context", "--metadata_json", '{"key":"value"}', "--custom_dims", "dim1=1.0", "dim2=2.0"]
    with patch('sys.argv', args):
        with patch('vectara_cli.commands.index_text_adv.vectara_client', return_value=mock_client):
            index_text_adv_main()
    mock_client.index_text.assert_called_once()

def test_index_text_adv_integration_failure(mock_client):
    """Integration test for failure due to invalid custom dimensions."""
    args = ["123", "doc123", "Hello, world!", "--custom_dims", "dim1"]
    with patch('sys.argv', args):
        with patch('vectara_cli.commands.index_text_adv.vectara_client', return_value=mock_client):
            with pytest.raises(ValueError):
                index_text_adv_main()

if __name__ == "__main__":
    pytest.main()
