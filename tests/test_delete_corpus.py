# tests/test_delete_corpus_adv.py

import pytest
from unittest.mock import patch, MagicMock
from vectara_cli.commands.delete_corpus_adv import main, delete_corpus

class ArgsMock:
    def __init__(self, corpus_id):
        self.corpus_id = corpus_id

@pytest.fixture
def vectara_client_mock(mocker):
    mock = mocker.patch('vectara_cli.core.VectaraClient')
    mock.return_value.delete_corpus.return_value = ({}, True)  
    return mock

def test_delete_corpus_success(vectara_client_mock):
    corpus_id = 12345
    args = ArgsMock(corpus_id=corpus_id)
    with patch('vectara_cli.commands.delete_corpus_adv.ConfigManager.get_api_keys', return_value=('customer_id', 'api_key')):
        with patch('sys.argv', ['prog', str(corpus_id)]):
            main(args)
            vectara_client_mock.return_value.delete_corpus.assert_called_once_with(corpus_id)

def test_delete_corpus_failure(vectara_client_mock):
    vectara_client_mock.return_value.delete_corpus.return_value = ({"error": "Some error"}, False)
    corpus_id = 12345
    args = ArgsMock(corpus_id=corpus_id)
    with patch('vectara_cli.commands.delete_corpus_adv.ConfigManager.get_api_keys', return_value=('customer_id', 'api_key')):
        with patch('sys.argv', ['prog', str(corpus_id)]), pytest.raises(SystemExit) as e:
            main(args)
            assert e.type == SystemExit
            vectara_client_mock.return_value.delete_corpus.assert_called_once_with(corpus_id)
            assert e.value.code != 0
