# tests/index_text_adv.py

import pytest
from unittest.mock import patch, MagicMock
from vectara_cli.commands.index_text_adv import main as index_text_adv_main

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

if __name__ == "__main__":
    pytest.main()
