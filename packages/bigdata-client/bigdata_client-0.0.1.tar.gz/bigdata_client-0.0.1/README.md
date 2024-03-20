# Bigdata Client

[![CI/CD Pipeline](https://github.com/RavenPack/bigdata-client/actions/workflows/cicd.yml/badge.svg)](https://github.com/RavenPack/bigdata-client/actions/workflows/cicd.yml)

## Installation

    poetry install

For development, install the pre-commit hooks:

    poetry run pre-commit install

or run them manually:

    poetry run task pre-commit

### Generate the documentation

    poetry install --with docs
    poetry run task docs

## Running tests:

To run just the unit tests:

```sh
poetry run pytest -m "not integration"
```

Integration tests require a set of environment variables to be set, with some valid user:

```sh
export BIGDATA_USER="youruser"
export BIGDATA_PASSWORD="******"
poetry run pytest tests -m "integration"
```
