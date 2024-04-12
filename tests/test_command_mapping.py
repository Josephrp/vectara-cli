# test_command_mapping.py

from vectara_cli.main import get_command_mapping

def test_command_mapping():
    expected_commands = [
        "index-document",
        "query",
        "create-corpus",
        "delete-corpus",
        "span-text",
        "span-enhance-folder",
        "upload-document",
        "upload-enriched-text",
        "nerdspan-upsert-folder",
        "rebel-upsert-folder",
        "index-text",
        "upload-folder"
    ]
    command_mapping = get_command_mapping()
    for cmd in expected_commands:
        assert cmd in command_mapping, f"Command '{cmd}' is missing in command_mapping"