# cookiecutter-django

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/ambv/black)


A django cookie cutter template inspired by [cookiecutter-django](https://github.com/pydanny/cookiecutter-django).

# Installation & Usage

> Make sure your env is using Python 3+

```bash
$ python -m venv env
$ source env/bin/activate

$ pip install --upgrade pip
$ pip install cookiecutter bumpversion
$ cookiecutter https://github.com/TangentSolutions/cookiecutter-django
```

After generating the project `cd into the folder` and run the following.

```bash
$ ./install-demo.sh
$ ./initialize-demo.sh
```

# First steps

The project includes a small demo of the libraries it bundles. Once running open your browser on [localhost:8000](http://localhost:8000) and create an account. The mail hog server can be accessed on [localhost:8025](http://localhost:8025/) when you need to retrieve the confirmation email.

# Included libraries

## web-pdb

Web pdb is included and can be used as follows (Note the port is important in the example below as this port is exposed by the local docker container).

```python
import web_pdb

web_pdb.set_trace(port=1986)
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

- [ ] Add django channels support
	- [ ] Investigate using a reverse proxy within container
- [x] Add GraphQL support
	- [ ] Integrate with DRF permissioning
- [ ] startapp template
	- [ ] Create startapp templates that reflect choices made by user i.e. include graphql
	- [ ] Include test suite structure
- [ ] Restructure project structure to standard django structure
- [ ] Tests
- [ ] Install cairo for weasy print
- [x] Specify port in docker compose
- [x] Use python 3.6.7
- [ ] Update gitignore in post hook
- [x] Update bumpversion config
- [ ] Tests run on sqlite
