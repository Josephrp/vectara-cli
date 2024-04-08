# Basic Usage of Vectara CLI

The Vectara CLI provides a simple and efficient way to interact with the Vectara platform, allowing users to create corpora, index documents, and perform various other operations directly from the command line. This section covers the basic usage of the Vectara CLI for common tasks such as creating a corpus and indexing documents.

## Creating a Corpus

To create a new corpus, you can use the `create-corpus` command. A corpus represents a collection of documents and serves as the primary organizational unit within Vectara.

### Basic Corpus Creation

```bash
vectara create-corpus <corpus_id> <name> <description>
```

- `<corpus_id>`: The unique identifier for the corpus. Must be an integer.
- `<name>`: The name of the corpus. This should be a unique name that describes the corpus.
- `<description>`: A brief description of what the corpus is about.

#### Example

```bash
vectara create-corpus 123 "My Corpus" "A corpus containing documents on topic XYZ"
```

This command creates a basic corpus with the specified ID, name, and description.

## Indexing a Document

To index a document into a corpus, you can use the `index-text` command. This command allows you to add a text document to the specified corpus, making it searchable within the Vectara platform.

### Indexing Text

```bash
vectara-cli index-text <corpus_id> <document_id> <text> <context> <metadata_json>
```

- `<corpus_id>`: The unique identifier for the corpus where the document will be indexed.
- `<document_id>`: A unique identifier for the document being indexed.
- `<text>`: The actual text content of the document that you want to index.
- `<context>`: Additional context or information about the document.
- `<metadata_json>`: A JSON string containing metadata about the document.

#### Example

```bash
vectara-cli index-text 12345 67890 "This is the text of the document." "Summary of the document" '{"author":"John Doe", "publishDate":"2024-01-01"}'
```

This command indexes a document with the provided text, context, and metadata into the specified corpus.

## Advanced Corpus Creation

For more advanced scenarios, you might want to specify additional options such as custom dimensions, filter attributes, or privacy settings for your corpus. The `create-corpus-advanced` command allows for these additional configurations.

### Advanced Creation with Options

```bash
vectara create-corpus-advanced <name> <description> [options]
```

Options include setting custom dimensions, filter attributes, public/private status, and more.

#### Example

```bash
vectara create-corpus-advanced "Research Papers" "Corpus for academic research papers" --custom_dimensions '{"dimension1": "value1", "dimension2": "value2"}' --filter_attributes '{"author": "John Doe"}'
```

This command creates a corpus with custom dimensions and filter attributes specified, allowing for more detailed organization and retrieval capabilities.

### Deleting a Corpus

To remove an existing corpus from the Vectara platform, you can use the `delete-corpus` command. Deleting a corpus will permanently remove the corpus and all documents contained within it. This action cannot be undone, so ensure that you really want to delete the corpus before proceeding.

#### Basic Corpus Deletion

```bash
vectara delete-corpus <corpus_id>
```

- `<corpus_id>`: The unique identifier for the corpus you wish to delete. This must be an integer.

#### Example

```bash
vectara delete-corpus 12345
```

This command deletes the corpus with the specified ID from the Vectara platform. Upon successful deletion, you will receive a confirmation message. If the corpus cannot be found or if there is an error during the deletion process, an error message will be displayed instead.

### Uploading a Document

To upload a document to a specific corpus in the Vectara platform, you can use the `upload-document` command. This allows you to add various types of documents, such as PDFs, Word documents, and plain text files, making them searchable within your corpus.

#### Basic Document Upload

```bash
vectara-cli upload-document <corpus_id> <file_path> [document_id]
```

- `<corpus_id>`: The unique identifier for the corpus where the document will be uploaded. This must be an integer.
- `<file_path>`: The path to the document file that you want to upload.
- `[document_id]`: An optional parameter that specifies the document ID. If not provided, Vectara will generate a unique ID for the document.

#### Example

```bash
vectara-cli upload-document 12345 "/path/to/document.pdf"
```

This command uploads a document from the specified file path to the corpus with the given ID. If the upload is successful, you will receive a confirmation message along with any relevant details provided by the Vectara platform.

#### Uploading with a Specific Document ID

If you wish to specify a document ID during the upload process, you can include it as an additional argument:

```bash
vectara-cli upload-document 12345 "/path/to/document.pdf" "custom-document-id-123"
```

This allows you to assign a custom identifier to the document, which can be useful for tracking or referencing the document within your application or database.

#### Supported Document Formats

Vectara supports a variety of document formats for upload, including but not limited to:

- PDF (.pdf)
- Microsoft Word (.docx)
- PowerPoint (.pptx)
- Plain Text (.txt)

Ensure that your documents are in one of the supported formats before attempting to upload them to the Vectara platform.

#### Metadata and Context

While the basic upload command does not include options for metadata and context, it's important to note that Vectara allows for the association of metadata with documents. This can be accomplished through advanced usage of the Vectara CLI or API, enabling you to provide additional information about the documents you upload, such as author, publication date, tags, and more.

For detailed instructions on advanced document upload options, including how to include metadata and context, please refer to the Vectara documentation or the advanced usage section of the Vectara CLI help.