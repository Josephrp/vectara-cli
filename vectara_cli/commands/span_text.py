# ./commands/span_text.py

import argparse
import json

from vectara_cli.rebel_span.noncommercial.nerdspan import Span
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.core import VectaraClient, LocalVectaraClient
from vectara_cli.rebel_span.noncommercial.nerdspan import Span


def main():
    parser = argparse.ArgumentParser(description='Process text using Vectara CLI')
    parser.add_argument('--text', type=str, default="the lazy fox jumped over the brown dog", help='The text to analyze')
    parser.add_argument('--model_name', type=str, default='fewnerdsuperfine', help='The name of the model to use')
    parser.add_argument('--model_type', type=str, default='span_marker', help='The type of the model')
    args = parser.parse_args()
    
    try:
        vectara_client = ConfigManager()
    except:
        vectara_client = LocalVectaraClient()
    

    try:
        span = Span(args.text, vectara_client, args.model_name, args.model_type)
        span.load_model()  
        output_str, key_value_pairs = span.analyze_text()
        print(output_str)
        print(json.dumps(key_value_pairs))
    except Exception as e:
        print("Error processing text:", str(e))
        



if __name__ == "__main__":
    main()
