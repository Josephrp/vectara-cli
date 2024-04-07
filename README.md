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

### Advanced Installation

The advanced installation includes additional dependencies for advanced text processing and analysis features. This requires PyTorch, Transformers, and Accelerate, which can be substantial in size.

```bash
pip install vectara-cli[advanced]
```

Ensure you have an appropriate PyTorch version installed for your system, especially if you're installing on a machine with GPU support. Refer to the [official PyTorch installation guide](https://pytorch.org/get-started/locally/) for more details.

## Command Line Interface (CLI) Usage

The `vectara-cli` provides a powerful command line interface for interacting with the Vectara platform, enabling tasks such as document indexing, querying, corpus management, and advanced text processing directly from your terminal. This section will guide you through the basics of using the `vectara-cli`.

### Configuration

- **[Configuration](.docs/configuration.md)**

### Usage

- **[Basic Usage](./docs/basic_usage.md)**
- **[Advanced Usage](./docs/advanced_usage.md)**

## Contributing

- **[Contributing](./CONTRIBUTE.md)**

## License

`vectara-cli` is MIT licensed. See the [LICENSE](LICENSE.md) file for more details.

```
@misc{Vectara CLI,
  author = {p3nGu1nZz, Tonic},
  title = {Vectara CLI is a Python package for Vectara platform interaction, ideal for search and information retrieval tasks.},
  year = {2024},
  publisher = {Tonic-AI},
  journal = {Tonic-AI repository},
  howpublished = {\url{https://git.tonic-ai.com/releases/vectara-cli}}
}
```