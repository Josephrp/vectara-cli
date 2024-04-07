# create_corpus.py

import sys
import argparse
from vectara_cli.core import VectaraClient
from vectara_cli.config_manager import ConfigManager
from corpus_data import CorpusData


def main():
    parser = argparse.ArgumentParser(description="Create a new corpus in Vectara platform.")
    parser.add_argument("corpus_id", type=int, help="Corpus ID")
    parser.add_argument("name", type=str, help="Name of the corpus")
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

    # Convert string "True"/"False" to boolean for enabled, swapQenc, swapIenc, textless, encrypted
    def str2bool(v):
        return v.lower() in ("yes", "true", "t", "1")

    corpus_data = CorpusData(
        corpus_id=args.corpus_id,
        name=args.name,
        description=args.description,
        dtProvision=args.dt_provision,
        enabled=str2bool(args.enabled),
        swapQenc=str2bool(args.swap_qenc),
        swapIenc=str2bool(args.swap_ienc),
        textless=str2bool(args.textless),
        encrypted=str2bool(args.encrypted),
        encoderId=args.encoder_id,
        metadataMaxBytes=args.metadata_max_bytes,
        customDimensions=[],  # Add logic to parse custom_dimensions if provided
        filterAttributes=[],  # Add logic to parse filter_attributes if provided
    )

    try:
        customer_id, api_key = ConfigManager.get_api_keys()
        vectara_client = VectaraClient(customer_id, api_key)
        response = vectara_client.create_corpus(corpus_data)
        print(response)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()