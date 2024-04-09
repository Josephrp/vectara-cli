import os
from unittest.mock import patch
import pytest
from vectara_cli.main import ConfigManager

class TestConfigManager:
    @patch.dict(os.environ, {}, clear=True)
    def test_set_api_keys(self):
        """Test setting API keys correctly sets environment variables."""
        customer_id = "test_customer_id"
        api_key = "test_api_key"
        ConfigManager.set_api_keys(customer_id, api_key)

        assert os.environ['VECTARA_CUSTOMER_ID'] == customer_id
        assert os.environ['VECTARA_API_KEY'] == api_key

    @patch.dict(os.environ, {}, clear=True)
    def test_get_api_keys_without_setting(self):
        """Test getting API keys without setting them first raises an error."""
        with pytest.raises(ValueError) as exc_info:
            ConfigManager.get_api_keys()

        assert "API keys are not set in environment variables" in str(exc_info.value)

    @patch.dict(os.environ, {'VECTARA_CUSTOMER_ID': 'test_customer_id', 'VECTARA_API_KEY': 'test_api_key'})
    def test_get_api_keys_with_setting(self):
        """Test getting API keys returns the correct values after they have been set."""
        customer_id, api_key = ConfigManager.get_api_keys()

        assert customer_id == 'test_customer_id'
        assert api_key == 'test_api_key'

    @patch.dict(os.environ, {'VECTARA_CUSTOMER_ID': 'test_customer_id'}, clear=True)
    def test_get_api_keys_missing_one_key(self):
        """Test getting API keys raises an error if one key is missing."""
        with pytest.raises(ValueError) as exc_info:
            ConfigManager.get_api_keys()

        assert "API keys are not set in environment variables" in str(exc_info.value)