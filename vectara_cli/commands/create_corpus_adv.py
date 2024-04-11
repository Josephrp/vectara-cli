# ./vectara-cli/commands/create_corpus_adv.py

import json
import argparse
# from vectara_cli.utils import get_vectara_client
from vectara_cli.data.corpus_data import CorpusData
from vectara_cli.data.defaults import CorpusDefaults

def parse_json_arg(json_str):
    try:
        return json.loads(json_str)
    except json.JSONDecodeError:
        raise ValueError("Invalid JSON format")

def create_corpus_adv(args, vectara_client):
    options = CorpusDefaults.get_defaults()

    options["customDimensions"] = parse_json_arg(args.custom_dimensions) if args.custom_dimensions else options.get("customDimensions")
    options["filterAttributes"] = parse_json_arg(args.filter_attributes) if args.filter_attributes else options.get("filterAttributes")
    options["encoderId"] = args.encoder_id if args.encoder_id else options.get("encoderId")
    options["metadataMaxBytes"] = args.metadata_max_bytes if args.metadata_max_bytes else options.get("metadataMaxBytes")
    options["swapQenc"] = args.swap_qenc
    options["swapIenc"] = args.swap_ienc
    options["textless"] = args.textless
    options["encrypted"] = args.encrypted
    options["public"] = args.public

    corpus_data = CorpusData(corpus_id=None, name=args.name, description=args.description, **options)

    try:
        response = vectara_client.create_corpus(corpus_data.to_dict())
        print(json.dumps(response, indent=4))
    except ValueError as e:
        print(e)

def setup_arg_parser(subparsers, vectara_client):
    parser = subparsers.add_parser('create-corpus-adv', help='Create a corpus with advanced options. Use "vectara create-corpus-adv -h" for more details.')
    parser.add_argument('name', type=str, help='The name of the corpus. This should be a unique name that describes the corpus.')
    parser.add_argument('description', type=str, help='A brief description of what the corpus is about.')
    parser.add_argument('--custom_dimensions', type=str, help='A JSON string representing custom dimensions for the corpus. Example: \'{"dimension1": "value1", "dimension2": "value2"}\'')
    parser.add_argument('--filter_attributes', type=str, help='A JSON string representing attributes used for filtering documents within the corpus. Example: \'{"author": "John Doe"}\'')
    parser.add_argument('--public', type=bool, help='A boolean flag indicating whether the corpus should be public (true) or private (false). Default is false.', default=False)
    parser.add_argument('--encoder_id', type=int, help='Encoder ID, default is 1.', default=1)
    parser.add_argument('--metadata_max_bytes', type=int, help='Maximum metadata bytes, default is 10000.', default=10000)
    parser.add_argument('--swap_qenc', action='store_true', help='Swap query encoder, default is False.')
    parser.add_argument('--swap_ienc', action='store_true', help='Swap index encoder, default is False.')
    parser.add_argument('--textless', action='store_true', help='If the corpus is textless, default is False.')
    parser.add_argument('--encrypted', action='store_true', help='If the corpus is encrypted, default is True.')
    parser.set_defaults(func=lambda args: create_corpus_adv(args, vectara_client))
