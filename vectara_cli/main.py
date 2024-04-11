# ./main.py

import sys
from vectara_cli.commands import (
    create_corpus,
    nerdspan_upsert_folder,
    index_text,
    index_document,
    query,
    delete_corpus,
    span_enhance_folder,
    upload_document,
    upload_enriched_text,
    span_text,
    rebel_upsert_folder,
    upload_folder
)
from vectara_cli.utils.create_ui import create_ui
# from vectara_cli.utils.config_manager import ConfigManager
from vectara_cli.utils.utils import get_vectara_client, set_api_keys as set_api_keys_main
from vectara_cli.helptexts.help_text import main_help_text

def command_func_wrapper(command_func):
    def wrapper(args):
        if args.command == "set-api-keys":
            command_func(args)
        else:
            try:
                vectara_client = get_vectara_client()
                if args.command == "advanced-query":
                    command_func([args.query_text, str(args.num_results), str(args.corpus_id), args.context_config, args.summary_config], vectara_client)
                else:
                    command_func(args, vectara_client)
            except ValueError as e:
                print(e)
                sys.exit(1)
    return wrapper

def get_command_mapping():
    command_mapping = {
        "index-document": index_document.main,
        "query": query.main,
        "create-corpus": create_corpus.main,
        "delete-corpus": delete_corpus.main,
        "span-text": span_text.main,
        "span-enhance-folder": span_enhance_folder.main,
        "upload-document": upload_document.main,
        "upload-enriched-text": upload_enriched_text.main,
        "nerdspan-upsert-folder": nerdspan_upsert_folder.main,
        "rebel-upsert-folder": rebel_upsert_folder.main,
        "index-text": index_text.main,
        "create-ui":create_ui,
        "advanced-query":advanced_query.main
        "index-text-adv": index_text_adv.main,
    }
    return command_mapping

def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("help", "--help", "-h"):
        main_help_text()
        sys.exit(0)

    command = sys.argv[1]
    args = sys.argv[2:]
    if command == "set-api-keys":
        if len(args) != 2:
            print("Error: set-api-keys requires exactly 2 arguments: customer_id and api_key.")
            sys.exit(1)
        set_api_keys_main(*args) 

    else:
        vectara_client = get_vectara_client()
        command_mapping = get_command_mapping()
        if command in command_mapping:
            command_mapping[command](args, vectara_client)
        else:
            print(f"vectara: '{command}' is not a vectara command. See 'vectara --help'.")
            sys.exit(1)

if __name__ == "__main__":
    main()
