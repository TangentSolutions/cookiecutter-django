# {{cookiecutter.project_name}}
{% if cookiecutter.open_source_license != "Not open source" %}
### License {{cookiecutter.open_source_license}}

{% endif %}
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
{% if cookiecutter.use_mailhog == "y" %}

# Email Server

{% if cookiecutter.use_docker == 'y' %}
In development, it is often nice to be able to see emails that are being sent from your application. For that reason local SMTP server `MailHog`_ with a web interface is available as docker container.

Container mailhog will start automatically when you will run all docker containers.
Please check `cookiecutter-django Docker documentation`_ for more details how to start all containers.

With MailHog running, to view messages that are sent by your application, open your browser and go to ``http://127.0.0.1:8025``
{% else %}
In development, it is often nice to be able to see emails that are being sent from your application. If you choose to use `MailHog`_ when generating the project a local SMTP server with a web interface will be available.

#. `Download the latest MailHog release`_ for your OS.

#. Rename the build to ``MailHog``.

#. Copy the file to the project root.

#. Make it executable: ::

    $ chmod +x MailHog

#. Spin up another terminal window and start it there: ::

    ./MailHog

#. Check out `<http://127.0.0.1:8025/>`_ to see how it goes.

Now you have your own mail server running locally, ready to receive whatever you send it.

.. _`Download the latest MailHog release`: https://github.com/mailhog/MailHog/releases
.. _mailhog: https://github.com/mailhog/MailHog
{% endif %}
{% endif %}

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