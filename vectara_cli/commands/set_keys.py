# vectara_cli/commands/set_keys.py

import argparse
from vectara_cli.utils.utils import set_api_keys_adv as set_api_keys

def set_api_keys_command(args):
    """
    Sets the API keys using the utility function.
    """
    vectara_client = set_api_keys(args.customer_id, args.api_key)
    print("API keys set successfully. Vectara client initialized.")

def setup_arg_parser(subparsers):
    """
    Sets up argument parser for setting API keys.
    """
    parser = subparsers.add_parser('set-api-keys', help='Set the API keys')
    parser.add_argument('--customer_id', type=str, required=True, help='Customer ID')
    parser.add_argument('--api_key', type=str, required=True, help='API Key')
    parser.set_defaults(func=set_api_keys_command)