# cookiecutter-django

A django cookie cutter template inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django).

# Installation & Usage

```bash
$ python -m venv env
$ source env/bin/activate

$ pip install --upgrade pip
$ pip install -r requirements.txt
$ cookiecutter https://github.com/TangentSolutions/cookiecutter-django
```

After generating the project cd into it and run the following.

```bash
$ npm install # This is for bootstrap
$ python ./copy_bootstrap.py
$ docker-compose -f local.yml up --build
```

# First steps

The project includes a small demo of the libraries it bundles. Once running open your browser on [localhost:8000](http://localhost:8000) and create an account. The mail hog server can be accessed on [localhost:8025](http://localhost:8025/) when you need to retrieve the confirmation email.

## Optional

Optionally you can load some fixtures for the demo.

```bash
$ docker-compose -f local.yml run --rm django python manage.py loaddata fixtures.json
```

# Included libraries

## web-pdb

Web pdb is included and can be used as follows (Note the port is important in the example below as this port is exposed by the local docker container).

```python
import web_pdb

web_pdb.set_trace(port=1836)
```

Within the local environment `PYTHONBREAKPOINT="web_pdb.set_trace"` is set. Therefore in Python 3.7 and up the debugger can be activated by calling `breakpoint()`.

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

TODO:

- Add django channels support
- Add GraphQL support
- Investigate replacing allauth
