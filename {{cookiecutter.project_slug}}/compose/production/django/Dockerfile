{%- if cookiecutter.python_version == "3.6" %}
FROM python:3.6.7
{% elif cookiecutter.python_version == "3.7" %}
FROM python:3.7
{% endif -%}
ENV PYTHONUNBUFFERED 1

RUN apt-get update && apt-get -y install apt-utils libsass-dev
{%- if cookiecutter.pdf_plugin == "y" %}
RUN apt-get -y install libcairo2 libpango-1.0-0 \
	libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
	libffi-dev shared-mime-info
{%- endif %}

RUN groupadd django
RUN useradd django -g django

# Requirements are installed here to ensure they will be cached.
COPY ./requirements /requirements
RUN pip install --no-cache-dir -r /requirements/production.txt \
    && rm -rf /requirements

COPY ./compose/production/django/entrypoint /entrypoint
RUN sed -i 's/\r//' /entrypoint
RUN chmod +x /entrypoint
RUN chown django /entrypoint

COPY ./compose/production/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start
RUN chown django /start
{% if cookiecutter.use_celery == "y" %}
COPY ./compose/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker
RUN chown django /start-celeryworker

COPY ./compose/production/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat
RUN chown django /start-celerybeat

COPY ./compose/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r//' /start-flower
RUN chmod +x /start-flower
{% endif %}
COPY . /app

RUN chown -R django /app

USER django

WORKDIR /app

ENTRYPOINT ["/entrypoint"]
