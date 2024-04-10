# vectara-cli/commands/delete_corpus_adv.py

import argparse
from vectara_cli.core import VectaraClient
from vectara_cli.utils.config_manager import ConfigManager

def delete_corpus(corpus_id, vectara_client):
    try:
        response, success = vectara_client.delete_corpus(corpus_id)
        if success:
            print("Corpus deleted successfully.")
        else:
            print("Failed to delete corpus:", response)
    except ValueError as e:
        print(e)

def main(args):
    corpus_id = args.corpus_id
    try:
        customer_id, api_key = ConfigManager.get_api_keys()
        vectara_client = VectaraClient(customer_id, api_key)
        delete_corpus(corpus_id, vectara_client)
    except ValueError as e:
        print(e)

def setup_arg_parser(subparsers):
    delete_corpus_adv_parser = subparsers.add_parser('delete-corpus-adv', help='Delete a corpus with advanced options')
    delete_corpus_adv_parser.add_argument('corpus_id', type=int, help='Corpus ID to delete')
    delete_corpus_adv_parser.set_defaults(func=main)