# /tests/test_advanced_query.py

import sys
from unittest.mock import patch
from vectara_cli.commands.advanced_query import main

def test_main_success(capsys):
    with patch('sys.argv', ["script.py", "test query", "2", "corpus_id", '{}', '{}']):
        main([], None)
    captured = capsys.readouterr()
    assert "Result 1" in captured.out
    assert "Result 2" in captured.out

def test_main_few_arguments(capsys):
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'argv', ["script.py", "test query"]):
            main([], None)
        mock_print.assert_called_once_with("Starting advanced query main...")

def test_main_invalid_json(capsys):
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'argv', ["script.py", "test query", "2", "corpus_id", '{invalid_json}', '{}']):
            main([], None)
        mock_print.assert_called_once_with("Error: Expecting property name enclosed in double quotes: line 1 column 2 (char 1)")

def test_no_response_from_query(capsys):
    with patch('builtins.print') as mock_print:
        with patch.object(sys, 'argv', ["script.py", "test query", "2", "corpus_id", '{}', '{}']):
            main([], None)
        mock_print.assert_called_once_with("No response received from the advanced query.")