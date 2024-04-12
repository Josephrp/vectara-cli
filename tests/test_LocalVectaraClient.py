import pytest
from vectara_cli.core import LocalVectaraClient

def is_LocalVectaraClient_valid():
    assert LocalVectaraClient().api_key is not None and LocalVectaraClient().api_key  != ""
    assert LocalVectaraClient().customer_id is not None and LocalVectaraClient().customer_id  != ""

