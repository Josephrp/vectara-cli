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
