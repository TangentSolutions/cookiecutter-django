from typing import Dict
from django.urls import path, include
from rest_framework.reverse import reverse
from rest_framework.routers import SimpleRouter
from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
{% if cookiecutter.use_graphql == "y" -%}
from graphene_django.views import GraphQLView
from accounts.schema import schema
{% endif -%}
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


class APIRootView(APIView):
    """Root API view for the users module."""

    @staticmethod
    def get_routes(request: Request) -> Dict:
        routes = {
            "users": reverse("accounts-api:user-list", request=request),
            "check-username-availability": reverse(
                "accounts-api:user-check-username-availability", request=request
            ),
        }

        return routes

    def get(self, request: Request) -> Response:
        """Provides the routes available under the users module.

        Returns:
            A DRF response containing hyperlinks to the available routes.
        """

        routes = self.get_routes(request)
        return Response(routes)


# API url patterns
api_root = APIRootView.as_view()
{% if cookiecutter.use_graphql == "y" -%}
graphql_view = GraphQLView.as_view(schema=schema, graphiql=True)
{% endif -%}

api_urlpatterns = [
    path('', api_root, name='api-root'),
    path('', include(router.urls)),
    {%- if cookiecutter.use_graphql == "y" %}
    path('graphiql', graphql_view, name='graphiql'),
    {%- endif %}
]

# Template based url patterns
urlpatterns = [
    path('', view=user_list_view, name='user-list'),
    path('redirect/', view=user_redirect_view, name='user-redirect'),
    path('update/', view=user_update_view, name='user-update'),
    path('<str:username>/', view=user_detail_view, name='user-detail'),
]
