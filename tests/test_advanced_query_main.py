# tests/test_advanced_query_main.py

import json
from unittest.mock import MagicMock
import pytest
from vectara_cli.core import VectaraClient
from advanced_query_main import advanced_query_main

@pytest.fixture
def vectara_client_mock(mocker):
    mock = mocker.Mock(spec=VectaraClient)
    mock.advanced_query = MagicMock(return_value=["Result 1", "Result 2"])
    return mock

def test_advanced_query_main_with_insufficient_args(capsys, mocker):
    args = ["query"]
    advanced_query_main(args)
    captured = capsys.readouterr()
    assert "No arguments provided." in captured.out

def test_advanced_query_main_with_invalid_context_config_json(capsys):
    args = ["query", "2", "123", '{"invalid_json": true']
    advanced_query_main(args)
    captured = capsys.readouterr()
    assert "Invalid context config JSON" in captured.out

def test_advanced_query_main_with_invalid_summary_config_json(capsys):
    args = ["query", "2", "123", '{}', '{"invalid_json": true']
    advanced_query_main(args)
    captured = capsys.readouterr()
    assert "Invalid summary config JSON" in captured.out

def test_advanced_query_main_successful_query(capsys, vectara_client_mock):
    args = ["query", "2", "123", '{}', '{}']
    advanced_query_main(args, vectara_client=vectara_client_mock)
    captured = capsys.readouterr()
    assert "Result 1" in captured.out
    assert "Result 2" in captured.out
    vectara_client_mock.advanced_query.assert_called_once()

def test_advanced_query_main_with_exception(capsys, vectara_client_mock):
    vectara_client_mock.advanced_query.side_effect = ValueError("An error occurred")
    args = ["query", "2", "123", '{}', '{}']
    advanced_query_main(args, vectara_client=vectara_client_mock)
    captured = capsys.readouterr()
    assert "An error occurred" in captured.out

def test_advanced_query_main_no_vectara_client_initialized(capsys):
    args = ["query", "2", "123", '{}', '{}']
    advanced_query_main(args)
    captured = capsys.readouterr()
    assert "Vectara client is not initialized." in captured.out
