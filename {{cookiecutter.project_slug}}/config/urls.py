from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.reverse import reverse
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response

import accounts.urls


# Root view for all API endpoints
class APIRoot(APIView):
    """Root view for all API based views in all applications."""

    def get(self, request: Request) -> Response:
        """Generate a mapping of url names to urls for the APIs within
        the application.

        Args:
            request: A DRF request instance

        Returns:
            A response containing the names and urls for the root apis of each
            application.
        """

        routes = {'accounts': reverse('accounts-api:api-root', request=request)}

        return Response(routes)


api_root = APIRoot.as_view()


# DRF urlpatterns
api_urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', api_root, name='api-root'),
    path(
        'api/accounts/',
        include((accounts.urls.api_urlpatterns, 'accounts'), namespace='accounts-api'),
    ),
]


# Standard django urlpatterns
urlpatterns = [
    path('', include('showcase.urls', namespace='showcase')),
    # Django Admin, use {% raw %}{% url 'admin:index' %}{% endraw %}
    path(settings.ADMIN_URL, admin.site.urls),
    # User management
    path('accounts/', include('allauth.urls')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    # Your stuff: custom urls includes go here
]

urlpatterns += api_urlpatterns
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            '400/',
            default_views.bad_request,
            kwargs={'exception': Exception('Bad Request!')},
        ),
        path(
            '403/',
            default_views.permission_denied,
            kwargs={'exception': Exception('Permission Denied')},
        ),
        path(
            '404/',
            default_views.page_not_found,
            kwargs={'exception': Exception('Page not Found')},
        ),
        path('500/', default_views.server_error),
    ]
    if 'debug_toolbar' in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path('__debug__/', include(debug_toolbar.urls))] + urlpatterns
