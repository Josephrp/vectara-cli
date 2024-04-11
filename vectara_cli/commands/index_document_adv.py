# vectara-cli/commands/index_document_adv.py

import json

def setup_index_document_adv_parser(subparsers, vectara_client):
    """
    Sets up the argument parser for the 'index-text-adv' command.
    """
    parser = subparsers.add_parser('index-text-adv', help='Index text with advanced options')
    parser.add_argument('corpus_id', type=int, help='Corpus ID where the text will be indexed')
    parser.add_argument('document_id', type=str, help='A unique identifier for the document')
    parser.add_argument('title', type=str, help='The title of the document')
    parser.add_argument('metadata_json', type=str, help='A JSON string containing metadata for the document')
    parser.add_argument('section_text', type=str, help='The main content of the document')
    parser.set_defaults(func=lambda args: index_document_advanced(args, vectara_client))

def parse_metadata(metadata_json):
    """
    Parses the metadata JSON string into a Python dictionary.
    """
    try:
        return json.loads(metadata_json), None
    except json.JSONDecodeError as e:
        return None, f"Error decoding metadata_json: {e}"

def index_document_advanced(args, vectara_client):
    """
    Handles the 'index-text-adv' command, using the provided VectaraClient instance.
    """
    metadata, error = parse_metadata(args.metadata_json)
    if error:
        print(error)
        return

    # Assuming 'index_document' is a method of VectaraClient that takes these parameters
    # and returns a tuple (response, success).
    response, success = vectara_client.index_document(
        corpus_id=args.corpus_id,
        document_id=args.document_id,
        title=args.title,
        metadata=metadata,
        section_text=args.section_text
    )

    if success:
        print("Document indexed successfully.")
    else:
        print(f"Document indexing failed: {response}")