

#### Querying

To perform a query in a specific corpus:

```bash
vectara-cli query "<query_text>" <num_results> <corpus_id>
```

- `<query_text>`: The text of the query.
- `<num_results>`: The maximum number of results to return.
- `<corpus_id>`: The ID of the corpus to query against.


#### Deleting a Corpus

To delete an existing corpus:

```bash
vectara-cli delete-corpus <corpus_id>
```

- `<corpus_id>`: The ID of the corpus to delete.

#### Setting Up a Vectara Client

First, initialize the Vectara client with your customer ID and API key. This client will be used for all subsequent operations.

```python
from vectara_cli.core import VectaraClient

customer_id = 'your_customer_id'
api_key = 'your_api_key'
vectara_client = VectaraClient(customer_id, api_key)
```

#### Indexing a Document

To index a document, you need its corpus ID, a unique document ID, and the text you want to index. Optionally, you can include context, metadata in JSON format, and custom dimensions.

```python
corpus_id = 'your_corpus_id'
document_id = 'unique_document_id'
text = 'This is the document text you want to index.'
context = 'Document context'
metadata_json = '{"author": "John Doe"}'

vectara_client.index_text(corpus_id, document_id, text, context, metadata_json)
```

#### Indexing Documents from a Folder

To index all documents from a specified folder into a corpus, provide the corpus ID and the folder path.

```python
corpus_id = 'your_corpus_id'
folder_path = '/path/to/your/documents'

results = vectara_client.index_documents_from_folder(corpus_id, folder_path)
for document_id, success, extracted_text in results:
    if success:
        print(f"Successfully indexed document {document_id}.")
    else:
        print(f"Failed to index document {document_id}.")
```

#### Querying Documents

To query documents, specify your search query, the number of results you want to return, and the corpus ID.

```python
query_text = 'search query'
num_results = 10  # Number of results to return
corpus_id = 'your_corpus_id'

results = vectara_client.query(query_text, num_results, corpus_id)
print(results)
```

#### Deleting a Corpus

To delete a corpus, you only need to provide its ID.

```python
corpus_id = 'your_corpus_id'
response, success = vectara_client.delete_corpus(corpus_id)

if success:
    print("Corpus deleted successfully.")
else:
    print("Failed to delete corpus:", response)
```

#### Uploading a Document

To upload and index a document, specify the corpus ID, the path to the document, and optionally, a document ID and metadata.

```python
corpus_id = 'your_corpus_id'
file_path = '/path/to/your/document.pdf'
document_id = 'unique_document_id'  # Optional
metadata = {"author": "Author Name", "title": "Document Title"}  # Optional

try:
    response, status = vectara_client.upload_document(corpus_id, file_path, document_id, metadata)
    print("Upload successful:", response)
except Exception as e:
    print("Upload failed:", str(e))
```