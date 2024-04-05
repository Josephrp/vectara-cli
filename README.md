# vectara-cli

`vectara-cli` is a Python package designed to interact with the Vectara platform, providing a command-line interface (CLI) and a set of APIs for indexing and querying documents, managing corpora, and performing advanced text analysis and processing tasks. This package is particularly useful for developers and data scientists working on search and information retrieval applications.

## Features

- Indexing text and documents into Vectara corpora.
- Querying indexed documents.
- Creating and deleting corpora.
- Advanced text processing and analysis using pre-trained models (optional advanced package).

## Installation

### Basic Installation

The basic installation includes the core functionality for interacting with the Vectara platform.

```bash
pip install vectara-cli
```

### Advanced Installation

The advanced installation includes additional dependencies for advanced text processing and analysis features. This requires PyTorch, Transformers, and Accelerate, which can be substantial in size.

```bash
pip install vectara-cli[advanced]
```

Ensure you have an appropriate PyTorch version installed for your system, especially if you're installing on a machine with GPU support. Refer to the [official PyTorch installation guide](https://pytorch.org/get-started/locally/) for more details.

## Usage

### Basic Usage

#### Setting Up a Vectara Client

```python
from vectara_cli.core import VectaraClient

customer_id = 'your_customer_id'
api_key = 'your_api_key'
vectara_client = VectaraClient(customer_id, api_key)
```

#### Indexing a Document

```python
corpus_id = 'your_corpus_id'
document_id = 'unique_document_id'
text = 'This is the document text you want to index.'

vectara_client.index_text(corpus_id, document_id, text)
```

#### Querying Documents

```python
query_text = 'search query'
num_results = 10  # Number of results to return
corpus_id = 'your_corpus_id'

results = vectara_client.query(query_text, num_results, corpus_id)
print(results)
```

### Advanced Usage

The advanced features allow you to enrich your indexes with additional information automatically. This should produce better results for retrieval.

#### Non-Commercial Advanced Rag Using Rebel

**insert images here**


Use the use the `Rebel Class` for advanced indexing. This will automatically extract `named entities`, `key phrases`, and other relevant information from your documents : 



```python
from vectara_cli.advanced.non_commercial.rebel import Rebel

folder_path = '/path/to/your/documents'
query_text = 'search query'
num_results = 10  # Number of results to return
# Initialize the Rebel instance for advanced non-commercial text processing
rebel = Rebel()

# Perform advanced indexing
corpus_id_1, corpus_id_2 = rebel.advanced_upsert_folder(vectara_client, corpus_id_1, corpus_id_2, folder_path)

# Vanilla Retrieval 
plain_results = vectara_client.query(query_text, num_results, corpus_id_1)
# Enhanced Retrieval
enhanced_results = vectara_client.query(query_text, num_results, corpus_id_2)

# Print Results
print("=== Plain Results ===")
for result in plain_results:
    print(f"Document ID: {result['documentIndex']}, Score: {result['score']}, Text: {result['text'][:100]}...")

print("\n=== Enhanced Results ===")
for result in enhanced_results:
    print(f"Document ID: {result['documentIndex']}, Score: {result['score']}, Text: {result['text'][:100]}...")
```

## Contributing

Contributions to `vectara-cli` are welcome! Please refer to the contributing guidelines in the repository for more information on how to contribute.

## License

`vectara-cli` is MIT licensed. See the LICENSE file for more details.

---

This README provides a comprehensive guide for installing and using the `vectara-cli` package. For further information or assistance, please refer to the [Vectara documentation](https://docs.vectara.com) or submit an issue on the GitHub repository.