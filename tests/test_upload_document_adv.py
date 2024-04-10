# /tests/test_upload_document_adv.py

import pytest
import argparse
from unittest.mock import Mock

from vectara_cli.commands.index_text_adv import setup_index_document_adv_parser, parse_metadata, index_document_advanced

vectara_client = Mock()

@pytest.fixture
def parser():
    return argparse.ArgumentParser()

def test_setup_index_document_adv_parser(parser):
    setup_index_document_adv_parser(parser.add_subparsers())

    args = parser.parse_args(['index-text-adv', '123', 'document1', 'title1', '{"author": "some_author"}', 'content1'])

    assert args.corpus_id == '123'
    assert args.document_id == 'document1'
    assert args.title == 'title1'
    assert args.metadata_json == '{"author": "some_author"}'
    assert args.section_text == 'content1'
    assert args.func == index_document_advanced

def test_parse_metadata():
    result = parse_metadata('{"some_key": "some_value"}')
    assert result == ({"some_key": "some_value"}, None)

    result = parse_metadata('invalid')
    assert 'Error decoding metadata_json' in result[1]

def test_index_document_advanced():
    args = argparse.Namespace(corpus_id=123, document_id='doc1', title='title1', 
                              metadata_json='{"author": "author1"}', section_text='content1')

    vectara_client.index_document.return_value = ("response", True)
    index_document_advanced(args, vectara_client)
    vectara_client.index_document.assert_called_with(123, 'doc1', 'title1', {"author": "author1"}, 'content1')

    vectara_client.index_document.return_value = ("fail_response", False)
    index_document_advanced(args, vectara_client)
    vectara_client.index_document.assert_called_with(123, 'doc1', 'title1', {"author": "author1"}, 'content1')