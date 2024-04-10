# ./vectara-cli/commands/index_text_adv.py

from vectara_cli.helptexts.help_text import print_index_text_usage
import json

def parse_args(args):
    """
    Parses arguments for the advanced index text command.
    """
    parser = argparse.ArgumentParser(description="Index text with advanced options")
    parser.add_argument("corpus_id", type=int, help="Corpus ID")
    parser.add_argument("document_id", type=str, help="Document ID")
    parser.add_argument("text", type=str, help="Text to index")
    parser.add_argument("--context", type=str, default="", help="Context of the text")
    parser.add_argument("--metadata_json", type=str, default="{}", help="Metadata in JSON format")
    parser.add_argument("--custom_dims", nargs='*', help="Custom dimensions as name=value pairs", default=[])
    return parser.parse_args(args)

def main(args, vectara_client):
    args = parse_args(args)
    custom_dims = parse_custom_dimensions(args.custom_dims)
    custom_dims_dicts = [dim.to_dict() for dim in custom_dims]
    metadata_dict = json.loads(args.metadata_json)
       
    try:
        response = vectara_client.index_text(
            corpus_id=args.corpus_id,
            document_id=args.document_id,
            text=args.text,
            context=args.context,
            metadata_json=json.dumps(metadata_dict),
            custom_dims=custom_dims_dicts
        )
        print("Indexing response:", response)
    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("This script is intended to be used as a module and should not be executed directly.")
