{%- if cookiecutter.python_version == "3.6" %}
FROM python:3.6
{% elif cookiecutter.python_version == "3.7" %}
FROM python:3.7
{% endif -%}

# Setup environment
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ARG BUILD

RUN printf "deb http://archive.debian.org/debian/ jessie main\ndeb-src http://archive.debian.org/debian/ jessie main\ndeb http://security.debian.org jessie/updates main\ndeb-src http://security.debian.org jessie/updates main" > /etc/apt/sources.list
RUN apt-get update && apt-get install -y netcat

# Install libcairo if pdf exports are required
{%- if cookiecutter.pdf_plugin == "y" %}
RUN apt-get update && apt-get -y install libcairo2 libpango-1.0-0 \
    libpangocairo-1.0-0 libgdk-pixbuf2.0-0 \
    libffi-dev shared-mime-info
{% endif %}

# Install libsass-dev
{%- if cookiecutter.use_sass_preprocessor == 'y' %}
RUN apt-get update && apt-get -y install apt-utils libsass-dev
{% endif %}

# Install python dependencies here so that they are cached
COPY ./Pipfile /Pipfile
COPY ./install.sh /install.sh
RUN sed -i 's/\r//' /install.sh
RUN chmod +x /install.sh
RUN /install.sh

COPY ./compose/local/django/start /start
RUN sed -i 's/\r//' /start
RUN chmod +x /start

{% if cookiecutter.use_celery == "y" %}
COPY ./compose/local/django/celery/worker/start /start-celeryworker
RUN sed -i 's/\r//' /start-celeryworker
RUN chmod +x /start-celeryworker

COPY ./compose/local/django/celery/beat/start /start-celerybeat
RUN sed -i 's/\r//' /start-celerybeat
RUN chmod +x /start-celerybeat

COPY ./compose/local/django/celery/flower/start /start-flower
RUN sed -i 's/\r//' /start-flower
RUN chmod +x /start-flower
{% endif %}

# Copy code
COPY . /app
WORKDIR /app

# Run the application
CMD ["sh", "/start"]
