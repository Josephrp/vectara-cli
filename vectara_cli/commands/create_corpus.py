# create_corpus.py

import sys
import argparse
from vectara_cli.core import VectaraClient
from vectara_cli.config_manager import ConfigManager

def create_corpus(vectara_client, args):
    # Convert string "True"/"False" to boolean
    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")

    # Parse custom dimensions
    custom_dimensions = []
    if args.custom_dimensions:
        for dim in args.custom_dimensions.split(';'):
            name, description, serving_default, indexing_default = dim.split(',')
            custom_dimensions.append({
                "name": name,
                "description": description,
                "servingDefault": int(serving_default),
                "indexingDefault": int(indexing_default)
            })

    # Parse filter attributes
    filter_attributes = []
    if args.filter_attributes:
        for attr in args.filter_attributes.split(';'):
            name, description, indexed, type, level = attr.split(',')
            filter_attributes.append({
                "name": name,
                "description": description,
                "indexed": str2bool(indexed),
                "type": type,
                "level": level
            })

    response = vectara_client.create_corpus(
        args.corpus_id,
        args.name,
        args.description,
        args.dt_provision,
        str2bool(args.enabled),
        str2bool(args.swap_qenc),
        str2bool(args.swap_ienc),
        str2bool(args.textless),
        str2bool(args.encrypted),
        args.encoder_id,
        args.metadata_max_bytes,
        custom_dimensions,
        filter_attributes,
    )
    print(response)

def main():
    parser = argparse.ArgumentParser(description="Create a new corpus in Vectara platform.")
    parser.add_argument("corpus_id", type=int, help="Corpus ID")
    parser.add_argument("name", type=str, default="CorpusTonic",  help="Name of the corpus")
    parser.add_argument("--description", type=str, default="Description", help="Description of the corpus")
    parser.add_argument("--dt_provision", type=int, default=1234567890, help="Provisioning timestamp")
    parser.add_argument("--enabled", type=str, default="True", help="Enable corpus")
    parser.add_argument("--swap_qenc", type=str, default="False", help="Swap QEnc")
    parser.add_argument("--swap_ienc", type=str, default="False", help="Swap IEnc")
    parser.add_argument("--textless", type=str, default="False", help="Textless")
    parser.add_argument("--encrypted", type=str, default="False", help="Encrypted")
    parser.add_argument("--encoder_id", type=str, default="default", help="Encoder ID")
    parser.add_argument("--metadata_max_bytes", type=int, default=10000, help="Maximum metadata bytes")
    parser.add_argument("--custom_dimensions", type=str, help="Custom dimensions (name,description,servingDefault,indexingDefault;...)")
    parser.add_argument("--filter_attributes", type=str, help="Filter attributes (name,description,indexed,type,level;...)")

    args = parser.parse_args()

    try:
        customer_id, api_key = ConfigManager.get_api_keys()
        vectara_client = VectaraClient(customer_id, api_key)
        create_corpus(vectara_client, args)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
