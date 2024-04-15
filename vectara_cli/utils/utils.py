# vectara-cli/utils/utils.py

from vectara_cli.core import VectaraClient
from vectara_cli.utils.config_manager import ConfigManager

def get_vectara_client() -> VectaraClient:
    customer_id, api_key = ConfigManager.get_api_keys()
    vectara_client = VectaraClient(customer_id, api_key)  
    return vectara_client

def set_api_keys(customer_id, api_key) -> None:
    ConfigManager.set_api_keys(customer_id, api_key)
    print("API keys set successfully.")
    return get_vectara_client() 

def set_api_keys_adv(customer_id, api_key) -> None:
    ConfigManager.set_api_keys(customer_id=customer_id, api_key=api_key)
    print("API keys set successfully.")
