# ./commands/span_enhance_folder.py

import os
from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.rebel_span.commercial.enterprise import EnterpriseSpan


def main(vectara_client, args):
    if len(args) < 2:
        print(
            "Usage: vectara-cli span-enhance-folder model_name folder_path"
        )
        return

    model_name = args[0]
    folder_path = args[1]

    try:
        if not os.path.isdir(folder_path):
            print(f"The specified folder path does not exist: {folder_path}")
            return

        enterprise_span = EnterpriseSpan(vectara_client, model_name)
        corpus_id_1 , corpus_id_2 = enterprise_span.span_enhance(folder_path)
        print(
            f"Documents in {folder_path} enhanced and uploaded to corpora: {corpus_id_1} (plain), {corpus_id_2} (enhanced)"
        )
#       return corpus_id_1 , corpus_id_2
    except Exception as e:
        print("An error occurred during the enhancement process:", str(e))


if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
