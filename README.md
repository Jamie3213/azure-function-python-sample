# Example Azure Function

## Overview

This project contains a sample [Azure Function](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-configuration#folder-structure)
written in Python, along with example unit tests and project configurations like `pre-commit`.
The function is an [HTTP trigger](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook-trigger?tabs=python-v2%2Cin-process%2Cfunctionsv2&pivots=programming-language-python)
and uses the `v1` programming model, however the
[`v2` programming model](https://learn.microsoft.com/en-us/azure/azure-functions/functions-reference-python?tabs=asgi%2Capplication-level&pivots=python-mode-decorators#folder-structure)
can also be used (though will require some alterations to the code). See below for details of
how to get your local environment set up and how to run the application locally.

## Getting started

**Note:** this guide assumes you're running you local environment in macOS.

To begin, install [`homebrew`](https://brew.sh) by following the installation
steps. Once homebrew is installed, install the required project dependencies:

```bash
brew tap azure/functions
brew install azure-functions-core-tools@4 pre-commit pyenv
```

Now install Python 3.10 using `pyenv`:

```bash
pyenv install 3.10.12
```

Add the following line to your `~/.bash_profile` or `~/.zshrc` file:

```bash
export PATH=$(pyenv root)/shims:$PATH
```

Now, make Python 3.10 the global Python version:

```bash
pyenv global 3.10.12
```

Create a new virtual environment:

```bash
python3 -m venv .venv
```

Next, activate the virtual environment and install the dev dependencies -
these include the `azure-functions` package, as well as other non-production
dependencies like `mypy`, `black`, `isort` and `pytest`:

```bash
source .venv/bin/activate
pip install -r requirements-dev.txt
```

Next, ensure `pre-commit` is configured in your local environment and run the hooks to
verify everything works as expected:

```bash
pre-commit install
pre-commit run --all-files
```

To run unit tests alone, run them from `pytest`:

```bash
pytest tests/unit
```

## Running the Azure Function locally

The application is a simple HTTP API which expects to recieve a `GET` request along with
a paramater called `words` which can be any arbitrary string. The application will then
calculate the number of words in the string and return the value in its response. If the
`words` parameter is not provided, then the application will return an error.

To run the application locally, ensure you've followed the steps above to setup the local
environment, then run the following `azure-functions-core-tools` command:

```bash
func start
```

Then, in a new shell, send a test request to the API endpoint with `curl` - it should look
something like this:

```bash
$ curl http://localhost:7071/api/word_count?words=This%20is%20a%20test%string
String 'words' contains 4 words
```

## Other information

* See [the docs](https://learn.microsoft.com/en-us/azure/azure-functions/create-first-function-cli-python?tabs=bash%2Cazure-cli&pivots=python-mode-configuration) for details on how to deploy your Azure Function.
* See [the docs on bindings](https://learn.microsoft.com/en-us/azure/azure-functions/functions-bindings-storage-blob?tabs=in-process%2Cextensionv5%2Cextensionv3&pivots=programming-language-python) to easily read and write from services like Azure Blob Storage.
* If bindings don't offer the flexibility you need, take a look at the [Azure Python SDK](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-quickstart-blobs-python?tabs=managed-identity%2Croles-azure-portal%2Csign-in-azure-cli).
* For Infrastructure as Code, consider [Azure Bicep](https://learn.microsoft.com/en-us/azure/azure-functions/functions-create-first-function-bicep?tabs=CLI) or [Terraform](https://registry.terraform.io/providers/hashicorp/azurerm/latest/docs/resources/linux_function_app).
