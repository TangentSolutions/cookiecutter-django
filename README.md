# cookiecutter-django

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


A django cookie cutter template inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django).

# Installation & Usage

> Make sure your env is using Python 3+

```bash
$ python -m venv env
$ source env/bin/activate

$ pip install --upgrade pip
$ pip install cookiecutter
$ cookiecutter https://github.com/TangentSolutions/cookiecutter-django
```

After generating the project `cd into the folder` and run the following.

```bash
$ npm install
$ python copy_clientside_libraries.py
$ docker-compose -f local.yml up --build
```

# First steps

The project includes a small demo of the libraries it bundles. Once running open your browser on [localhost:8000](http://localhost:8000) and create an account. The mail hog server can be accessed on [localhost:8025](http://localhost:8025/) when you need to retrieve the confirmation email.

# Included libraries

## django_tables2 & django_filters

Django tables and django filters are included by default. A template for a table with filters can be found
within the showcase application. The template includes the following features:

- Collapsable django_filter form for the table
- Table export functionality
- Automatic collapse/show functionality on the filter form based on the current state of filters

To enable export on your table just add an `export_formats` attribute to the table class containing the formats you wish to support. 

```python
class UserTable(django_tables2.Table):
    """User table to showcase django tables 2."""

    export_formats = ('csv', 'json', 'latex', 'ods', 'tsv', 'xls', 'xlsx', 'yml')
```

# Known Issues

1. libcairo2 is required by weasyprint for pdf generation and is installed during the docker build. Currently the version of cairo installed triggers a user warning
related to svg images for versions < 1.15.4. At this time a newer version is not available to install via apt-get and would require downloading the source (+- 100mb) and building it. This has not been done since pdf generation is working correctly in spite of the user warning.
