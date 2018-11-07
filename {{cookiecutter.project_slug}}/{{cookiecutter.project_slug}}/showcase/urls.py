from django.urls import path
from {{cookiecutter.project_slug}}.showcase.views.template import showcase_demo_view


app_name = 'showcase'

# API url patterns
api_urlpatterns = []


# Template based url patterns
urlpatterns = [path('', showcase_demo_view, name='demo')]

