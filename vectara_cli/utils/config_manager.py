# config_manager.py

import json
import os

CONFIG_FILE_PATH = 'config.json'

class ConfigManager:
    @staticmethod
    def set_api_keys(customer_id, api_key):
        """Sets the customer ID and API key in environment variables."""
        os.environ['VECTARA_CUSTOMER_ID'] = customer_id
        os.environ['VECTARA_API_KEY'] = api_key

    @staticmethod
    def get_api_keys():
        """Retrieves the customer ID and API key from environment variables."""
        customer_id = os.getenv('VECTARA_CUSTOMER_ID')
        api_key = os.getenv('VECTARA_API_KEY')
        if customer_id is None or api_key is None:
            raise ValueError(
                "API keys are not set in environment variables. Please set them using the appropriate method."
            )
        return customer_id, api_key
