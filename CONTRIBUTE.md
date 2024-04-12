# Contributing Guidelines for vectara-cli

Thank you for your interest in contributing to `vectara-cli`! As an open-source project, we welcome contributions from developers of all skill levels. This guide will provide you with information on how to contribute effectively and make a valuable impact on the project.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python (preferably the latest Python 3 version)
- Conda (for managing environments)
- Git (for version control)

## Getting Started

### 1. Set Up Your Development Environment

1. **Fork the Repository**: Visit [vectara-cli on GitLab](https://git.tonic-ai.com/contribute/vectara/vectara-cli/) and fork the project to your account.
   
2. **Clone Your Fork**: Clone the repository to your local machine:

   ```bash
   git clone https://git.tonic-ai.com/<your-username>/vectara-cli.git
   cd vectara-cli
   ```

3. **Create and Activate Conda Environment**:

   ```bash
   conda env create -f environment.yml
   conda activate vectara-cli
   ```

4. **Install the Project in Editable Mode**:

   ```bash
   pip install --editable .
   ```

### 2. Find a Task

- Browse the [Issues](https://git.tonic-ai.com/contribute/vectara/vectara-cli/issues) to find tasks to work on. You can start with issues labeled as "good first issue".
- If you have an idea or a bug fix that is not listed, feel free to open a new issue to discuss it with other contributors.

## Making Changes

### 1. Create a Branch

Create a new branch for your changes:

```bash
git checkout -b your-feature-branch
```

### 2. Develop

- **Add Functionality**: Write your code and add it to the appropriate directory:
  - For new functionalities, add your code in `./vectara_cli/commands`.
  - Add command line functionality in `main.py`.
  - Create or modify data objects in `./vectara_cli/data`.

- **Add Help Text**: Update help texts in `./vectara_cli/help_texts/help_text.py` to reflect your changes or new commands.

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