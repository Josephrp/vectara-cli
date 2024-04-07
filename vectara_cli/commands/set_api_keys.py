# set_api_keys.py

from vectara_cli.config_manager import ConfigManager

def main(args):
    if len(args) != 3:
        print("Usage: vectara-cli set-api-keys <customer_id> <api_key>")
        return
    # args[0] is the command, args[1] is the customer_id, args[2] is the api_key
    customer_id, api_key = args[1], args[2]
    ConfigManager.set_api_keys(customer_id, api_key)
    print("API keys set successfully.")

if __name__ == "__main__":
    import sys
    main(sys.argv)
