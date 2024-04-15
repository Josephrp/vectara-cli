# ./commands/nerdspan_upsert_folder.py

import os
from vectara_cli.rebel_span.noncommercial.nerdspan import Span
from vectara_cli.utils.config_manager import ConfigManager


def main(vectara_client, args):
    if len(args) < 3:
        print("Usage: vectara process-and-upload folder_path model_name model_type")
        return

    folder_path = args[0]
    model_name = args[1]
    model_type = args[2]

    try:
        customer_id, api_key = ConfigManager.get_api_keys()
        if not os.path.isdir(folder_path):
            print(f"The specified folder path does not exist: {folder_path}")
            return
        text=""
        span = Span(vectara_client=vectara_client, text=text, model_name=model_name, model_type=model_type)
        corpus_id_1, corpus_id_2 = span.process_and_upload(
            folder_path, model_name, model_type
        )
        print(
            f"Documents processed and uploaded. Raw uploads in Corpus ID: {corpus_id_1}, Processed uploads in Corpus ID: {corpus_id_2}"
        )
    except Exception as e:
        print("An error occurred during processing:", str(e))


if __name__ == "__main__":
    import sys

    main(sys.argv)
