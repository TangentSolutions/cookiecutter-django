from django.urls import path
from showcase.views.template import showcase_demo_view, showcase_demo_view_print


app_name = 'showcase'

# API url patterns
api_urlpatterns = []


# Template based url patterns
urlpatterns = [
    path('', showcase_demo_view, name='demo'),
    path('pdf/', showcase_demo_view_print, name='demo-pdf'),
]
