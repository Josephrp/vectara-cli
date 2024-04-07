import json
from vectara_cli.core import VectaraClient

def main(args, vectara_client):
    if len(args) < 6:
        print(
            "Usage: vectara index-document corpus_id document_id title metadata_json section_text"
        )
        return

    # Extract arguments from the args list
    corpus_id = int(args[1])
    document_id = args[2]
    title = args[3]
    metadata_json = args[4]
    section_text = args[5]

    # Convert the string metadata_json into a dictionary
    try:
        metadata = json.loads(metadata_json)
    except json.JSONDecodeError as e:
        print(f"Error decoding metadata_json: {e}")
        return

    # Call the index_document method on the vectara_client
    response, success = vectara_client.index_document(
        corpus_id, document_id, title, metadata, section_text
    )

    if success:
        print("Document indexed successfully.")
    else:
        print(f"Document indexing failed: {response}")