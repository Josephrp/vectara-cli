# advanced_query_main.py

import json
import sys
from vectara_cli.core import VectaraClient
from vectara_cli.data.query_request import ContextConfig, SummaryConfig
from vectara_cli.helptexts.help_text_main import advanced_query_help

def advanced_query_main(args, vectara_client=None):
    if len(args) < 3:
        advanced_query_help
        return

    query_text = args[0]
    num_results = int(args[1])
    corpus_id = int(args[2])

    context_config_json = args[3] if len(args) > 3 else '{}'
    summary_config_json = args[4] if len(args) > 4 else '{}'

    context_config = None
    summary_config = None

    if context_config_json:
        try:
            context_config_dict = json.loads(context_config_json)
            context_config = ContextConfig(**context_config_dict)
        except json.JSONDecodeError as e:
            print(f"Invalid context config JSON: {e}")
            return
        except TypeError as e:
            print(f"Error in context config parameters: {e}")
            return

    if summary_config_json:
        try:
            summary_config_dict = json.loads(summary_config_json)
            summary_config = SummaryConfig(**summary_config_dict)
        except json.JSONDecodeError as e:
            print(f"Invalid summary config JSON: {e}")
            return
        except TypeError as e:
            print(f"Error in summary config parameters: {e}")
            return

    if not vectara_client:
        print("Vectara client is not initialized.")
        return

    try:
        response = vectara_client.advanced_query(query_text, num_results, corpus_id, context_config, summary_config)
        if response is not None:
            for item in response:
                print(item)
        else:
            print("No response received from the advanced query.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        advanced_query_main(sys.argv)
    else:
        print("No arguments provided.")