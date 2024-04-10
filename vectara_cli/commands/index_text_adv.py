# ./vectara-cli/commands/index_text_adv.py
import argparse
import json
import sys
from vectara_cli.helptexts.help_text import print_index_text_usage
import json

def parse_args(args):
    """
    Parses command line arguments.
    """
    parser = argparse.ArgumentParser(description="Index text with advanced options using the Vectara platform.")
    parser.add_argument("corpus_id", type=int, help="Corpus ID where the document will be indexed.")
    parser.add_argument("document_id", type=str, help="Unique Document ID for indexing.")
    parser.add_argument("text", type=str, help="Text content of the document to index.")
    parser.add_argument("--context", type=str, default="", help="Context or additional information about the document.")
    parser.add_argument("--metadata_json", type=str, default="{}", help="Metadata about the document in JSON format.")
    parser.add_argument("--custom_dims", nargs='*', help="Custom dimensions for the document, specified as name=value pairs.", default=[])
    return parser.parse_args(args)

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
def main(args, vectara_client):
    args = parse_args(args)
    custom_dims = parse_custom_dimensions(args.custom_dims)
    # custom_dims_dicts = [dim.to_dict() for dim in custom_dims]
    # metadata_dict = json.loads(args.metadata_json)
    args = parse_args(args)
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

    # except ValueError as e:
    #     print(f"Error: {e}")

# if __name__ == "__main__":
#     print("This script is intended to be used as a module and should not be executed directly.")
if __name__ == "__main__":
    main(sys.argv)