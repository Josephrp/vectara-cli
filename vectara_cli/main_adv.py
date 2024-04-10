# ./main_adv.py

import argparse
import sys

from vectara_cli.utils.create_ui import create_ui
from vectara_cli.utils.utils import get_vectara_client, set_api_keys as set_api_keys_util
from vectara_cli.commands.create_corpus_adv import setup_arg_parser as setup_create_corpus_adv_parser
from vectara_cli.commands.delete_corpus_adv import setup_arg_parser as setup_delete_corpus_adv_parser
from vectara_cli.commands.index_document_adv import setup_index_document_adv_parser
from vectara_cli.commands.index_text_adv import parse_args as setup_index_text_adv_parser 

def set_api_keys(args):
    set_api_keys_util(args.customer_id, args.api_key)

def main():
    parser = argparse.ArgumentParser(description="Vectara CLI Tool")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    # Set API Keys Parser
    set_api_keys_parser = subparsers.add_parser('set-api-keys', help='Set the API keys')
    set_api_keys_parser.add_argument('customer_id', type=str, help='Customer ID')
    set_api_keys_parser.add_argument('api_key', type=str, help='API Key')
    set_api_keys_parser.set_defaults(func=set_api_keys)

    # Setup subparsers for other commands
    setup_create_corpus_adv_parser(subparsers)
    setup_delete_corpus_adv_parser(subparsers)
    setup_index_text_adv_parser(subparsers)
    setup_index_document_adv_parser(subparsers)

    # Parse the arguments
    args = parser.parse_args()

    # Initialize Vectara client
    if args.command != "set-api-keys" and args.command != "create-ui":
        vectara_client = get_vectara_client()

    # Execute the command function
    if hasattr(args, 'func'):
        if args.command == "set-api-keys":
            args.func(args)
        if args.command == "create-ui":
            args.func(args)
        else:
            try:
                args.func(args, vectara_client)
            except Exception as e:
                print(f"Error executing command: {e}")
                sys.exit(1)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
