from typing import Dict, Union, Any
from django.http import HttpRequest
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.settings import api_settings
from rest_framework.decorators import api_view
from rest_framework.decorators import permission_classes
from rest_framework.decorators import authentication_classes
{%- if cookiecutter.use_graphql == 'y' %}
from graphene_django.views import GraphQLView
from graphene import Schema
{%- endif %}


class APIRootBaseView(APIView):
    """Base class for an API root view."""

    @staticmethod
    def get_routes(request: Request) -> Dict:
        """Generate a dict of routes for a given package."""

        raise NotImplementedError(
            f"method 'get_routes' not implemented for APIRootView"
        )

    def get(self, request: Request) -> Response:
        """Provides the routes available for a particular module.

        Returns:
            A DRF response containing hyperlinks to the available routes.
        """

        return Response(self.get_routes(request))


{%- if cookiecutter.use_graphql == 'y' %}
class DRFGraphQL(GraphQLView):
    """A sub class of the django graphene GraphQLView which integrates with
    the useful authentication, permission and api_view functionality of the DRF.
    """

    def parse_body(self, request: Union[HttpRequest, Request]) -> Any:
        if isinstance(request, Request):
            return request.data

        return super().parse_body(request)

    @classmethod
    def as_view(cls: "DRFGraphQL", schema: Schema) -> "DRFGraphQL":
        """Wraps the graphql view in the authentication_classes, permission_classes
        and api_view functions available from DRF.
        """

        view = super().as_view(graphiql=True, schema=schema)
        view = authentication_classes(api_settings.DEFAULT_AUTHENTICATION_CLASSES)(view)
        view = permission_classes(api_settings.DEFAULT_PERMISSION_CLASSES)(view)
        return api_view(http_method_names=("GET", "POST"))(view)
{%- endif %}
