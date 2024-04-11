# vectara_cli/commands/index_text_adv.py

import json
import sys
from vectara_cli.core import VectaraClient

def parse_custom_dimensions(custom_dims):
    """
    Parses custom dimensions from a list of name=value strings into a list of dictionaries.
    """
    dims = []
    for dim in custom_dims:
        if '=' not in dim:
            raise ValueError(f"Invalid custom dimension format: {dim}. Expected format: name=value.")
        name, value = dim.split('=', 1)
        try:
            # Assuming that all custom dimension values are numeric
            value = float(value)
        except ValueError:
            raise ValueError(f"Value for {name} must be numeric.")
        dims.append({"name": name, "value": value})
    return dims

def index_text_advanced(args, vectara_client):
    custom_dims = parse_custom_dimensions(args.custom_dims)
    
    try:
        response = vectara_client.index_text(
            corpus_id=args.corpus_id,
            document_id=args.document_id,
            text=args.text,
            context=args.context,
            metadata_json=args.metadata_json,
            custom_dims=custom_dims
        )
        print("Indexing response:", response)
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)

# Function to setup argparse for this specific command
def setup_index_text_adv_parser(subparsers, vectara_client):
    parser = subparsers.add_parser('index-text-adv', help='Index text with advanced options')
    parser.add_argument('corpus_id', type=int, help='Corpus ID where the document will be indexed.')
    parser.add_argument('document_id', type=str, help='Unique Document ID for indexing.')
    parser.add_argument('text', type=str, help='Text content of the document to index.')
    parser.add_argument('--context', type=str, default="", help='Context or additional information about the document.')
    parser.add_argument('--metadata_json', type=str, default="{}", help='Metadata about the document in JSON format.')
    parser.add_argument('--custom_dims', nargs='*', help="Custom dimensions for the document, specified as name=value pairs.", default=[])
    parser.set_defaults(func=lambda args: index_text_advanced(args, vectara_client))
