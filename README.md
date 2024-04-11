# vectara-cli

`vectara-cli` is a Python package designed to interact with the Vectara platform, providing a command-line interface (CLI) and a set of APIs for indexing and querying documents, managing corpora, and performing advanced text analysis and processing tasks. This package is particularly useful for developers and data scientists working on search and information retrieval applications.

## Features

- Indexing text and documents into Vectara corpora.
- Querying indexed documents.
- Creating and deleting corpora.
- Advanced text processing and analysis using pre-trained models (optional advanced package).

## Get Started

Get started with the [example_notebooks here](https://git.tonic-ai.com/releases/vectara-cli/examples/examples.ipynb) by downloading them and running them locally on any laptop.

### Basic Installation

The basic installation includes the core functionality for interacting with the Vectara platform.

```bash
pip install vectara-cli
```

#### Advanced Installation

The advanced installation includes additional dependencies for advanced text processing and analysis features. This requires PyTorch, Transformers, and Accelerate, which can be substantial in size.

```bash
pip install vectara-cli[rebel_span]
```

Ensure you have an appropriate PyTorch version installed for your system, especially if you're installing on a machine with GPU support. Refer to the [official PyTorch installation guide](https://pytorch.org/get-started/locally/) for more details.

#### Command Line Interface (CLI) Usage

The `vectara-cli` provides a powerful command line interface for interacting with the Vectara platform, enabling tasks such as document indexing, querying, corpus management, and advanced text processing directly from your terminal.

Before your start always set your api keys with :

```bash
vectara set-api-keys <user_id> <api_key>
```

<details>
<summary> Get Started </summary>
## Command Line Interface (CLI) Usage

The `vectara-cli` provides a powerful command line interface for interacting with the Vectara platform, enabling tasks such as document indexing, querying, corpus management, and advanced text processing directly from your terminal.

Before your start always set your api keys with :

```bash
vectara set-api-keys <user_id> <api_key>
```

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
</details>

<details>
<summary>  Configuration </summary>

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


#### Activating the Environment

Once the environment is created, you can activate it using the following command:

```bash
conda activate vectara
```


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
</details>

<details>
<summary>  Configuration </summary>

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


#### Activating the Environment

Once the environment is created, you can activate it using the following command:

```bash
conda activate vectara
```


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

#### Deploy Your App

- [x] **`vectara create-ui`:** This command will create a new UI for your app.

**Note:** that this script assumes you have [Node.js and NPM installed](https://nodejs.org/en/download) on your system, as required by the npx command.
<details>
<summary> Table of Contents </summary>

- **[Get started with the example_notebooks here](https://git.tonic-ai.com/releases/vectara-cli/examples/examples.ipynb)**
- **[More About Configuration](https://git.tonic-ai.com/releases/vectara-cli/-/blob/devbranch/docs/configuration.md)**

### Usage

- **[Basic Usage CLI](https://git.tonic-ai.com/releases/vectara-cli/-/blob/devbranch/docs/basic_useage_cli.md?ref_type=heads)**
- **[Programmatic Usage](https://git.tonic-ai.com/releases/vectara-cli/-/blob/devbranch/docs/basic_usage.md?ref_type=heads)**
- **[Advanced Usage](https://git.tonic-ai.com/releases/vectara-cli/-/blob/devbranch/docs/advanced_usage.md?ref_type=heads)**

## Deploy Your App

- [x] **`vectara create-ui`:** This command will create a new UI for your app.

**Note:** that this script assumes you have [Node.js and NPM installed](https://nodejs.org/en/download) on your system, as required by the npx command.

### 3. Write Tests

- Add tests for your new functionalities in the `tests/` directory.
- Ensure all tests pass by running them locally.

### 4. Document Your Changes

Update any documentation relevant to your changes, including inline comments and README if necessary.

## Submitting Changes

### 1. Commit Your Changes

Commit your changes with a clear message describing the feature or fix:

```bash
git commit -am "Add feature XYZ"
```

### 2. Push Your Changes

Push your branch to your GitHub fork:

```bash
git push origin your-feature-branch
```

### 3. Create a Merge Request
- Go to the [Merge Requests](https://git.tonic-ai.com/contribute/vectara/vectara-cli/-/merge_requests) page.
- Create a new merge request, compare your feature branch to the main repository's `devbranch`.
- Fill in a detailed description of your changes and link to any relevant issues.

## Review Process
Once your merge request is submitted:
- The project maintainers will review your code and may request changes.
- Collaborate on modifications and push updates to your branch accordingly.
- Once approved, a maintainer will merge your changes into the main codebase.

## Post-merge
After your changes have been merged:
- Sync your fork with the original repository.
- Consider deleting your branch to keep your fork clean:
  ```bash
  git branch -d your-feature-branch
  git push origin --delete your-feature-branch
  ```

Thank you for contributing to `vectara-cli`! For any questions or further discussions, please reach out on the issues page or [on discord](https://discord.gg/7H4SKQekKe).

- **[CONTRIBUTE](https://git.tonic-ai.com/releases/vectara-cli/-/blob/devbranch/CONTRIBUTE.md?ref_type=heads)**
- **[Testing](https://git.tonic-ai.com/releases/vectara-cli/-/blob/devbranch/tests)**

</details>

<details> <summary> License</summary>

`vectara-cli` is MIT licensed. See the [LICENSE](https://git.tonic-ai.com/releases/vectara-cli/-/blob/devbranch/LICENSE.md?ref_type=heads) file for more details.

</details>

```
@misc{Vectara Cli,
  author = {p3nGu1nZz, Tonic},
  title = {Vectara Cli is a Python package for Vectara platform interaction, ideal for search and information retrieval tasks.},
  year = {2024},
  publisher = {Tonic-AI},
  journal = {Tonic-AI repository},
  howpublished = {\url{https://git.tonic-ai.com/releases/vectara-cli}}
}
```