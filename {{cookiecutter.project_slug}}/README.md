# {{cookiecutter.project_name}}

# Settings

# Basic Commands

# Buidling

1. Running type checks with mypy:

```bash
$ mypy {{cookiecutter.project_slug}}
```

2. Tests and coverage

To run the tests, check your test coverage, and generate an HTML coverage report::

```bash
$ pytest
  $ coverage run -m pytest
  $ coverage html
  $ open htmlcov/index.html
```

{% if cookiecutter.use_celery == "y" %}

# Celery

This app comes with Celery.

To run a celery worker:

```bash
cd {{cookiecutter.project_slug}}
celery -A {{cookiecutter.project_slug}}.taskapp worker -l info
```

Please note: For Celery's import magic to work, it is important *where* the celery commands are run. If you are in the same folder with *manage.py*, you should be right.

{% endif %}

# Email Server

# Post installation

## Sass preprocessing

If using sass preprocessing for bootstrap be sure to install the latest version of bootstrap 4 as specified in the package.json file.

```bash
npm install
```

Note there is a helper script to copy the boostrap files from node_modules into the project's static folders. To run the script execute the command below.

```bash
python ./copy_boostrap.py
```

## Demo fixtures

The project has a demo using django-tables2, django-filters and weasy_print. This demo requires the provided fixtures be loaded. To load the fixtures execute the command below.

```bash
docker-compose -f local.yml run --rm django python manage.py loaddata fixtures.json
```
