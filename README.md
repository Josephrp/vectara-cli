# vectara-cli

`vectara-cli` is a Python package designed to interact with the Vectara platform, providing a command-line interface (CLI) and a set of APIs for indexing and querying documents, managing corpora, and performing advanced text analysis and processing tasks. This package is particularly useful for developers and data scientists working on search and information retrieval applications.

## Features

- Indexing text and documents into Vectara corpora.
- Querying indexed documents.
- Creating and deleting corpora.
- Advanced text processing and analysis using pre-trained models (optional advanced package).

## QuickStart

get started with the [example_notebooks here](https://git.tonic-ai.com/releases/vectara-cli/examples/examples.ipynb) by downloading them and running them locally on any laptop.

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

## Command Line Interface (CLI) Usage

The `vectara-cli` provides a powerful command line interface for interacting with the Vectara platform, enabling tasks such as document indexing, querying, corpus management, and advanced text processing directly from your terminal. This section will guide you through the basics of using the `vectara-cli`.

### Installation

Before using the CLI, ensure you have the package installed. You can install it directly from PyPi using pip:

```bash
pip install vectara-cli
```

### Optional: Conda Virtual Environment Setup

Conda is an open-source package management system and environment management system that runs on Windows, macOS, and Linux. It allows you to install, run, and update packages and their dependencies. To set up this project using Conda, follow the steps below:

#### Prerequisites

- Ensure that you have Conda installed on your system. If you do not have Conda installed, you can download it from the [official Conda website](https://www.anaconda.com/products/distribution).

#### Creating a Conda Environment

1. Open your terminal (or Anaconda Prompt on Windows).
2. Navigate to the project directory where the `environment.yml` file is located.
3. Create a new Conda environment by running the following command:

   ```bash
   conda env create -f environment.yml
   ```

   This will create a new environment with the name specified in the `environment.yml` file and install all the required packages.

#### Activating the Environment

Once the environment is created, you can activate it using the following command:

```bash
conda activate <env_name>
```

Replace `<env_name>` with the name of your Conda environment.

#### Deactivating the Environment

When you are done working on the project, you can deactivate the Conda environment by running:

```bash
conda deactivate
```

#### Updating the Environment

If you need to update the environment based on the `environment.yml` file, use the following command:

```bash
conda env update -f environment.yml --prune
```

This will update the environment with any new dependencies specified in the `environment.yml` file.

#### Removing the Environment

If you wish to remove the Conda environment, you can do so with the following command:

```bash
conda env remove -n <env_name>
```

Again, replace `<env_name>` with the name of your Conda environment.

By following these steps, you can manage your project's dependencies in an isolated environment using Conda.

### Configuration

#### Setting Credentials via CLI Commands

The `vectara-cli` tool now supports a convenient feature for setting your Vectara customer ID and API key directly through the command line. This method utilizes a command specifically designed for securely storing your credentials, making it easier to manage your Vectara configuration without manually setting environment variables or directly embedding your credentials in your scripts.

#### Using the `set-api-keys` Command

To set your Vectara customer ID and API key using the `vectara-cli`, you can use the `set-api-keys` command. This command stores your credentials securely, allowing `vectara-cli` to automatically use them for authentication in future operations.

- **Syntax:** The command follows this simple syntax:

```bash
vectara-cli set-api-keys <customer_id> <api_key>
```

Replace `<customer_id>` with your Vectara customer ID and `<api_key>` with your Vectara API key.

- **Example:**

```bash
vectara-cli set-api-keys 123456789 abcdefghijklmnopqrstuvwxyz
```

After executing this command, you will see a confirmation message indicating that your API keys have been set successfully.

#### Windows

For Windows users, you can also set environment variables through the Command Prompt or PowerShell, or via the System Properties window.

- **Command Prompt:**

```cmd
setx VECTARA_CUSTOMER_ID "your_customer_id"
setx VECTARA_API_KEY "your_api_key"
```

- **PowerShell:**

```powershell
[System.Environment]::SetEnvironmentVariable('VECTARA_CUSTOMER_ID', 'your_customer_id', [System.EnvironmentVariableTarget]::User)
[System.Environment]::SetEnvironmentVariable('VECTARA_API_KEY', 'your_api_key', [System.EnvironmentVariableTarget]::User)
```

Note that changes made through the command line will only take effect in new instances of the terminal or command prompt.

#### Using Credentials in `vectara-cli`

Once you have set up your environment variables, `vectara-cli` will automatically use these credentials for authentication. There's no need to manually input your customer ID and API key each time you execute a command.

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

### Advanced Usage


To leverage the advanced text processing capabilities, ensure you have completed the advanced installation of `vectara-cli`. This includes the necessary dependencies for text analysis:

```bash
pip install vectara-cli[advanced]
```

#### Span Text Processing

To process text using the Span model:

```bash
vectara-cli span-text "<text>" "<model_name>" "<model_type>"
```

- `<text>`: The text to process.
- `<model_name>`: The name of the Span model to use.
- `<model_type>`: The type of the Span model.

#### Enhanced Batch Processing with NerdSpan

To process and upload documents from a folder:

```bash
vectara-cli nerdspan-upsert-folder "<folder_path>" "<model_name>" "<model_type>"
```

- `<folder_path>`: The path to the folder containing documents to process and upload.
- `<model_name>`: The name of the model to use for processing.
- `<model_type>`: The type of the model.

For more advanced processing and upsert operations, including using the Rebel model for complex document analysis and upload, refer to the specific command documentation provided with the CLI.

### Commercial Advanced Usage

The commercial advanced features of `vectara-cli` enable users to leverage state-of-the-art text processing models for enriching document indexes with additional metadata. This enrichment process enhances the search and retrieval capabilities of the Vectara platform, providing more relevant and accurate results for complex queries.

**Reference:** Aarsen, T. (2023). SpanMarker for Named Entity Recognition. Radboud University. Supervised by Prof. Dr. Fermin Moscoso del Prado Martin (fermin.moscoso-del-prado@ru.nl) and Dr. Daniel Vila Suero (daniel@argilla.io). Second assessor: Dr. Harrie Oosterhuis (harrie.oosterhuis@ru.nl).

#### CLI Commands for Advanced Usage

The `vectara-cli` includes specific commands designed to facilitate advanced text processing and enrichment tasks. Below are the key commands and their usage:

>> **- supported models:** `science` and `keyphrase`

- **Upload Enriched Text**

  To upload text that has been enriched with additional metadata:

  ```bash
  vectara-cli upload-enriched-text <corpus_id> <document_id> <model_name> "<text>"
  ```

  - `<corpus_id>`: The ID of the corpus where the document will be uploaded.
  - `<document_id>`: A unique identifier for the document.
  - `<model_name>`: The name of the model used for text enrichment. `science` or `keyphrase`
  - `<text>`: The text content to be enriched and uploaded.

- **Span Enhance Folder**

  To process and upload all documents within a folder, enhancing them using a specified model:

  ```bash
  vectara-cli span-enhance-folder <corpus_id_1> <corpus_id_2> <model_name> "<folder_path>"
  ```

  - `<corpus_id_1>`: The ID for the corpus to upload plain text documents.
  - `<corpus_id_2>`: The ID for the corpus to upload enhanced text documents.
  - `<model_name>`: The name of the model used for document enhancement. **supported models :** `science` and `keyphrase`
  - `<folder_path>`: The path to the folder containing the documents to be processed.

#### Code Example for Advanced Usage

The following Python code demonstrates how to use the `EnterpriseSpan` class for advanced text processing and enrichment before uploading the processed documents to Vectara:

```python
from vectara_cli.advanced.commercial.enterpise import EnterpriseSpan

# Initialize the EnterpriseSpan with the desired model
model_name = "keyphrase"
enterprise_span = EnterpriseSpan(model_name)

# Example text to be processed
text = "OpenAI has developed a state-of-the-art language model named GPT-4."

# Predict entities in the text
predictions = enterprise_span.predict(text)

# Format predictions for readability
formatted_predictions = enterprise_span.format_predictions(predictions)
print("Formatted Predictions:\n", formatted_predictions)

# Generate metadata from predictions
metadata = enterprise_span.generate_metadata(predictions)

# Example corpus and document IDs
corpus_id = "123456"
document_id = "doc-001"

# Upload the enriched text along with its metadata to Vectara
enterprise_span.upload_enriched_text(corpus_id, document_id, text, predictions)
print("Enriched text uploaded successfully.")
```

This example showcases how to enrich text with additional metadata using the `EnterpriseSpan` class and upload it to a specified corpus in Vectara. By leveraging advanced models for text processing, users can significantly enhance the quality and relevance of their search and retrieval operations on the Vectara platform.

### Non-Commercial Advanced Usage

The advanced features allow you to enrich your indexes with additional information automatically. This should produce better results for retrieval.


![The mRebel pre-trained model is able to extract triplets for up to 400 relation types from Wikidata](https://git.tonic-ai.com/releases/vectara-cli/res/images/image.png?ref_type=heads)

### Non-Commercial Advanced Usage Using Span Models

The `vectara-cli` package extends its functionality through the advanced usage of Span Models, enabling users to perform sophisticated text analysis and entity recognition tasks. This feature is particularly beneficial for non-commercial applications that require deep understanding and processing of textual data.

The `Span` class supports processing and indexing documents from a folder, enabling batch operations for efficiency. This feature allows for the automatic extraction of entities from multiple documents, which are then indexed into specified corpora with enriched metadata.


#### Features

- **Named Entity Recognition (NER)**: Utilize pre-trained Span Models to identify and extract entities from text, enriching your document indexes with valuable metadata.
- **Model Flexibility**: Choose from a variety of pre-trained models tailored to your specific needs, including `fewnerdsuperfine`, `multinerd`, and `largeontonote`.
- **Enhanced Document Indexing**: Improve search relevance and results by indexing documents enriched with named entity information.

#### Usage

1. **Initialize Vectara Client**: Start by creating a Vectara client instance with your customer ID and API key.

    ```python
    from vectara_cli.core import VectaraClient

    customer_id = 'your_customer_id'
    api_key = 'your_api_key'
    vectara_client = VectaraClient(customer_id, api_key)
    ```

2. **Load and Use Span Models**: The `Span` class facilitates the loading of pre-trained models and the analysis of text to extract entities.

    ```python
    from vectara_cli.advanced.nerdspan import Span

    # Initialize the Span class
    span = Span(customer_id, api_key)

    # Load a pre-trained model
    model_name = "multinerd"  # Example model
    model_type = "span_marker"
    span.load_model(model_name, model_type)

    # Analyze text to extract entities
    text = "Your text here."
    output_str, key_value_pairs = span.analyze_text(model_name)
    print(output_str)
    ```

3. **Index Enhanced Documents**: After extracting entities, use the `VectaraClient` to index the enhanced documents into your corpus.

    ```python
    corpus_id = 'your_corpus_id'
    document_id = 'unique_document_id'
    metadata_json = json.dumps({"entities": key_value_pairs})

    vectara_client.index_text(corpus_id, document_id, text, metadata_json=metadata_json)
    ```

**Reference:** Aarsen, T. (2023). SpanMarker for Named Entity Recognition. Radboud University. Supervised by Prof. Dr. Fermin Moscoso del Prado Martin (fermin.moscoso-del-prado@ru.nl) and Dr. Daniel Vila Suero (daniel@argilla.io). Second assessor: Dr. Harrie Oosterhuis (harrie.oosterhuis@ru.nl).

#### Non-Commercial Advanced Rag Using Rebel

![mRebel](https://git.tonic-ai.com/releases/vectara-cli/-/raw/devbranch/res/images/Screenshot_2024-04-05_112158.png?ref_type=heads)
![Span Models for Named Entity Recognition](https://git.tonic-ai.com/releases/vectara-cli/-/raw/devbranch/res/images/Screenshot_2024-04-05_112142.png?ref_type=heads)

The mRebel pre-trained model is able to extract triplets for up to 400 relation types from Wikidata.


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


### Contributing to Advanced Features

We welcome contributions to improve and expand the advanced features of `vectara-cli`. Whether it's adding new models, enhancing existing functionalities, or fixing bugs, your contributions are valuable to us. Please refer to our contributing guidelines for more information on how to contribute.

## License

`vectara-cli` is MIT licensed. See the [LICENSE](LICENSE.md) file for more details.

---

This README provides a comprehensive guide for installing and using the `vectara-cli` package. For further information or assistance, please refer to the [Vectara documentation](https://docs.vectara.com) or submit an issue on the [GitLab repository](https://git.tonic-ai.com/releases/vectara-cli/).

---

```
@misc{Vectara CLI,
  author = {p3nGu1nZz, Tonic},
  title = {Vectara CLI is a Python package for Vectara platform interaction, ideal for search and information retrieval tasks.},
  year = {2024},
  publisher = {GitHub},
  journal = {GitHub repository},
  howpublished = {\url{https://git.tonic-ai.com/releases/vectara-cli}}
}
```