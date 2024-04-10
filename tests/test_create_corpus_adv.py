# tests/test_create_corpus_adv.py

import pytest
from unittest.mock import Mock
from vectara_cli.commands.create_corpus_adv import create_corpus_adv, parse_json_arg

def test_parse_json_arg_valid():
    """Test parsing of a valid JSON string."""
    json_str = '{"key": "value"}'
    result = parse_json_arg(json_str)
    assert result == {"key": "value"}

def test_parse_json_arg_invalid():
    """Test parsing of an invalid JSON string."""
    with pytest.raises(ValueError):
        parse_json_arg("invalid json")

def test_create_corpus_adv_basic(mocker):
    """Test the basic functionality of create_corpus_adv with minimal arguments."""
    args = mocker.MagicMock()
    args.name = "TestCorpus"
    args.description = "This is a test corpus"
    args.custom_dimensions = None
    args.filter_attributes = None
    args.encoder_id = None
    args.metadata_max_bytes = None
    args.swap_qenc = False
    args.swap_ienc = False
    args.textless = False
    args.encrypted = False
    args.public = False

    mock_vectara_client = Mock()
    mock_vectara_client.create_corpus = Mock(return_value={"success": True})

    create_corpus_adv(args, mock_vectara_client)

    # Verify create_corpus was called with expected parameters
    mock_vectara_client.create_corpus.assert_called_once()



# Test each argument separately

def test_name_argument(parser):
    args = parser.parse_args(['create-corpus-adv', 'UniqueCorpus', 'A unique corpus'])
    assert args.name == 'UniqueCorpus'

def test_description_argument(parser):
    args = parser.parse_args(['create-corpus-adv', 'CorpusWithDescription', 'This is a detailed description'])
    assert args.description == 'This is a detailed description'

@pytest.mark.parametrize("json_input,expected", [
    ('{"dimension": "value"}', {"dimension": "value"}),
    ('{"attribute": "filter"}', {"attribute": "filter"})
])
def test_json_arguments(json_input, expected, mocker):
    args = mock_args(custom_dimensions=json_input, filter_attributes=json_input)
    assert parse_json_arg(args.custom_dimensions) == expected
    assert parse_json_arg(args.filter_attributes) == expected

def test_encoder_id_argument(parser):
    args = parser.parse_args(['create-corpus-adv', 'CorpusWithEncoder', 'Description', '--encoder_id', '123'])
    assert args.encoder_id == 123

def test_metadata_max_bytes_argument(parser):
    args = parser.parse_args(['create-corpus-adv', 'CorpusWithMetadata', 'Description', '--metadata_max_bytes', '2048'])
    assert args.metadata_max_bytes == 2048

@pytest.mark.parametrize("flag,expected", [
    ('--swap_qenc', True),
    ('--swap_ienc', True),
    ('--textless', True),
    ('--encrypted', True),
    ('--public', True)
])
def test_boolean_flags(flag, expected, parser):
    args = parser.parse_args(['create-corpus-adv', 'CorpusWithFlags', 'Description', flag])
    assert getattr(args, flag.strip('--')) is expected

# Mock the Vectara client and test the create_corpus_adv function with minimal and full options

@patch('vectara_cli.commands.create_corpus_adv.get_vectara_client')
def test_create_corpus_adv_minimal(mock_get_vectara_client, mocker):
    mock_vectara_client = Mock()
    mock_get_vectara_client.return_value = mock_vectara_client
    mock_vectara_client.create_corpus = Mock(return_value={"success": True})

    args = mock_args()
    create_corpus_adv(args, mock_vectara_client)

    mock_vectara_client.create_corpus.assert_called_once()

@patch('vectara_cli.commands.create_corpus_adv.get_vectara_client')
def test_create_corpus_adv_full_options(mocker):
    """Test create_corpus_adv with all possible arguments provided."""
    args = mocker.MagicMock()
    args.name = "FullOptionsCorpus"
    args.description = "A corpus with all options utilized"
    args.custom_dimensions = '{"dimension": "value"}'
    args.filter_attributes = '{"attribute": "filter"}'
    args.encoder_id = 123
    args.metadata_max_bytes = 1024
    args.swap_qenc = True
    args.swap_ienc = True
    args.textless = True
    args.encrypted = True
    args.public = True

    mock_vectara_client = Mock()
    mock_vectara_client.create_corpus = Mock(return_value={"success": True, "corpusId": 456})

    create_corpus_adv(args, mock_vectara_client)

    # Verify create_corpus was called with the expected parameters
    expected_options = {
        'name': 'FullOptionsCorpus',
        'description': 'A corpus with all options utilized',
        'customDimensions': {"dimension": "value"},
        'filterAttributes': {"attribute": "filter"},
        'encoderId': 123,
        'metadataMaxBytes': 1024,
        'swapQenc': True,
        'swapIenc': True,
        'textless': True,
        'encrypted': True,
        'public': True
    }
    mock_vectara_client.create_corpus.assert_called_once_with(expected_options)

def test_create_corpus_adv_failure(mocker):
    """Test the behavior of create_corpus_adv when the Vectara client raises an exception."""
    args = mocker.MagicMock()
    args.name = "FailingCorpus"
    args.description = "This corpus creation will fail"
    args.custom_dimensions = None
    args.filter_attributes = None
    args.encoder_id = None
    args.metadata_max_bytes = None
    args.swap_qenc = False
    args.swap_ienc = False
    args.textless = False
    args.encrypted = False
    args.public = False

    mock_vectara_client = Mock()
    mock_vectara_client.create_corpus.side_effect = ValueError("An error occurred")

    with pytest.raises(ValueError):
        create_corpus_adv(args, mock_vectara_client)

    mock_vectara_client.create_corpus.assert_called_once()
