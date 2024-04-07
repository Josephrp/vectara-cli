import json
from vectara_cli.core import VectaraClient
from vectara_cli.helptexts.helpetext import print_index_document_help

def main(args, vectara_client):
    if len(args) < 6:
        print_index_document_help()
        return
    corpus_id = int(args[1])
    document_id = args[2]
    title = args[3]
    metadata_json = args[4]
    section_text = args[5]
    try:
        metadata = json.loads(metadata_json)
    except json.JSONDecodeError as e:
        print(f"Error decoding metadata_json: {e}")
        return
    response, success = vectara_client.index_document(
        corpus_id, document_id, title, metadata, section_text
    )

    if success:
        print("Document indexed successfully.")
    else:
        print(f"Document indexing failed: {response}")

if __name__ == "__main__":
    import sys

    main(sys.argv[1:])
