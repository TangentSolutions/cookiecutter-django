from django.urls import path, include
from rest_framework.reverse import reverse
from rest_framework.routers import SimpleRouter
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from accounts.views.api import UserViewSet
from accounts.views.template import (
    user_list_view,
    user_redirect_view,
    user_update_view,
    user_detail_view,
)


app_name = 'accounts'


# Register viewsets and create a root API view
router = SimpleRouter()
router.register('users', UserViewSet, basename='user')


class APIRoot(APIView):
    """Root API view for the users module."""

    def get(self, request: Request) -> Response:
        """Provides the routes available under the users module.

        Returns:
            A DRF response containing hyperlinks to the available routes.
        """

        routes = {
            'users': reverse('accounts-api:user-list', request=request),
            'check-username-availability': reverse(
                'accounts-api:user-check-username-availability', request=request
            ),
        }

        return Response(routes)


# API url patterns
api_root = APIRoot.as_view()
api_urlpatterns = [path('', api_root, name='api-root'), path('', include(router.urls))]


# Template based url patterns
urlpatterns = [
    path('', view=user_list_view, name='list'),
    path('', include('allauth.urls')),
    path('redirect/', view=user_redirect_view, name='redirect'),
    path('update/', view=user_update_view, name='update'),
    path('<str:username>/', view=user_detail_view, name='detail'),
]
