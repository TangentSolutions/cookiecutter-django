from django.urls import path
from showcase.views.template import showcase_demo_view


api_urlpatterns = []

template_urlpatterns = [path('', showcase_demo_view, name='demo')]

app_name = 'showcase'
urlpatterns = api_urlpatterns + template_urlpatterns
