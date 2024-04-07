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


![Span Models for Named Entity Recognition](https://git.tonic-ai.com/releases/vectara-cli/-/raw/devbranch/res/images/image.png?ref_type=heads)

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
![The mRebel pre-trained model is able to extract triplets for up to 400 relation types from Wikidata](https://git.tonic-ai.com/releases/vectara-cli/-/raw/devbranch/res/images/Screenshot_2024-04-05_112142.png?ref_type=heads)

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
