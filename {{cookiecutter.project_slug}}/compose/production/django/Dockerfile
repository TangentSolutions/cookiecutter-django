FROM python:3.7

# Setup environment
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ARG BUILD

RUN apt-get update && apt-get install -y netcat{%- if cookiecutter.pdf_plugin == "y" %} \
    libcairo2 libpango-1.0-0 \
    libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    libffi-dev shared-mime-info{% endif %}{% if cookiecutter.use_sass_preprocessor == 'y' %} \
	libsass-dev
{%- endif %}

RUN groupadd django
RUN useradd django -g django

# Install python dependencies here so that they are cached
COPY ./Pipfile* /
COPY ./install.sh /install.sh
RUN sed -i 's/\r//' /install.sh
RUN chmod +x /install.sh
RUN /install.sh

COPY ./compose/production/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

{% if cookiecutter.use_celery == "y" %}
COPY ./compose/production/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/production/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/production/django/celery/flower/start /start-flower
RUN sed -i 's/\r//' /start-flower
RUN chmod +x /start-flower
{% endif %}

# Copy code
COPY . /app

RUN chown -R django /app

USER django
WORKDIR /app

# Run the application
CMD ["sh", "/start"]
