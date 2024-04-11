# main_adv.py

import argparse
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.utils.utils import get_vectara_client
from vectara_cli.commands.create_corpus_adv import setup_arg_parser as setup_create_corpus_adv_parser
from vectara_cli.commands.delete_corpus_adv import setup_arg_parser as setup_delete_corpus_adv_parser
from vectara_cli.commands.index_document_adv import setup_index_document_adv_parser
from vectara_cli.commands.index_text_adv import setup_index_text_adv_parser
from vectara_cli.commands.set_keys import setup_arg_parser as setup_set_keys_parser

def main():
    vectara_client = None
    try:
        vectara_client = get_vectara_client()
        api_keys_set = True
    except ValueError:
        api_keys_set = False

    parser = argparse.ArgumentParser(description="Vectara CLI Tool")
    subparsers = parser.add_subparsers(dest='command', help='commands')

    setup_set_keys_parser(subparsers)

    if api_keys_set:
        setup_create_corpus_adv_parser(subparsers, vectara_client)
        setup_delete_corpus_adv_parser(subparsers, vectara_client)
        setup_index_document_adv_parser(subparsers, vectara_client)
        setup_index_text_adv_parser(subparsers, vectara_client)
        args = parser.parse_args()

        if hasattr(args, 'func') and callable(getattr(args, 'func')):
            args.func(args, vectara_client)
        else:
            if not api_keys_set and args.command != 'set-api-keys':
                print("API keys are not set. Please set them using the 'set-api-keys' command.")
            else:
                parser.print_help()

if __name__ == "__main__":
    main()
