# ./vectara-cli/commands/index_text_adv.py

import argparse
import json
from vectara_cli.core import VectaraClient

def setup_index_document_adv_parser(subparsers):
    parser = subparsers.add_parser('index-text-adv', help='Index text with advanced options')
    parser.add_argument('corpus_id', type=int, help='Corpus ID where the text will be indexed')
    parser.add_argument('document_id', type=str, help='A unique identifier for the document')
    parser.add_argument('title', type=str, help='The title of the document')
    parser.add_argument('metadata_json', type=str, help='A JSON string containing metadata for the document')
    parser.add_argument('section_text', type=str, help='The main content of the document')
    parser.set_defaults(func=index_text_advanced)

def parse_metadata(metadata_json):
    try:
        return json.loads(metadata_json), None
    except json.JSONDecodeError as e:
        return None, f"Error decoding metadata_json: {e}"

def index_document_advanced(args, vectara_client):
    metadata, error = parse_metadata(args.metadata_json)
    if error:
        print(error)
        return

    response, success = vectara_client.index_document(
        args.corpus_id, args.document_id, args.title, metadata, args.section_text
    )

    if success:
        print("Document indexed successfully.")
    else:
        print(f"Document indexing failed: {response}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Index text with advanced options")
    parser.add_argument('corpus_id', type=int, help='Corpus ID where the text will be indexed')
    parser.add_argument('document_id', type=str, help='A unique identifier for the document')
    parser.add_argument('title', type=str, help='The title of the document')
    parser.add_argument('metadata_json', type=str, help='A JSON string containing metadata for the document')
    parser.add_argument('section_text', type=str, help='The main content of the document')
    args = parser.parse_args()

    # vectara_client = VectaraClient(customer_id="YourCustomerID", api_key="YourAPIKey")  # Placeholder
    index_text_advanced(args, vectara_client)
