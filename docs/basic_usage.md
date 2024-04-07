
### Basic Commands


#### Indexing a Document

To index a document into a specific corpus:

```bash
vectara-cli index-document <corpus_id> <document_id> "<title>" '<metadata_json>' "<section_text>"
```

- `<corpus_id>`: The ID of the corpus where the document will be indexed.
- `<document_id>`: A unique identifier for the document.
- `<title>`: The title of the document.
- `<metadata_json>`: A JSON string containing document metadata.
- `<section_text>`: The text content of the document.

#### Querying

To perform a query in a specific corpus:

```bash
vectara-cli query "<query_text>" <num_results> <corpus_id>
```

- `<query_text>`: The text of the query.
- `<num_results>`: The maximum number of results to return.
- `<corpus_id>`: The ID of the corpus to query against.

#### Creating a Corpus

To create a new corpus:

```bash
vectara-cli create-corpus <corpus_id> "<name>"
```

- `<corpus_id>`: The ID for the new corpus.
- `<name>`: The name of the new corpus.

#### Deleting a Corpus

To delete an existing corpus:

```bash
vectara-cli delete-corpus <corpus_id>
```

- `<corpus_id>`: The ID of the corpus to delete.

### Advanced Commands

### Basic Usage

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

#### Creating a Corpus

You can create a new corpus by specifying its ID, name, description, and other settings.

```python
create_corpus_response = vectara_client.create_corpus(
    corpus_id=123456789,
    name="Example Corpus",
    description="This is an example corpus.",
    dtProvision=1234567890,
    enabled=True,
    swapQenc=False,
    swapIenc=False,
    textless=False,
    encrypted=False,
    encoderId="default",
    metadataMaxBytes=10000,
    customDimensions=[
        {"name": "dimension1", "description": "First custom dimension", "servingDefault": 1.0, "indexingDefault": 1.0}
    ],
    filterAttributes=[
        {"name": "filter1", "description": "First filter attribute", "indexed": True, "type": "FILTER_ATTRIBUTE_TYPE__UNDEFINED", "level": "FILTER_ATTRIBUTE_LEVEL__UNDEFINED"}
    ]
)
print(create_corpus_response)
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