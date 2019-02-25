from django.urls import path
from showcase.views.template import showcase_demo_view
{%- if cookiecutter.pdf_plugin == 'y' %}
from showcase.views.template import showcase_demo_view_print
{%- endif %}

app_name = "showcase"

# API url patterns
api_urlpatterns = []


# Template based url patterns
urlpatterns = [
    path("", showcase_demo_view, name="demo"),
    {%- if cookiecutter.pdf_plugin == 'y' %}
    path("pdf/", showcase_demo_view_print, name="demo-pdf"),
    {%- endif %}
]
