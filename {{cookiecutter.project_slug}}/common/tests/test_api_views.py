from django.conf import settings
from django.test import RequestFactory
from rest_framework.test import APIRequestFactory
from rest_framework.request import Request
from rest_framework.response import Response
from common.views.api import APIRootBaseView, DRFGraphQL
from unittest.mock import patch, MagicMock
from graphql import GraphQLSchema

import pytest


pytestmark = pytest.mark.django_db


class TestAPIRootBaseView:
    """Test suite for the APIRootBaseView view."""

    def test_get_routes_raises(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):

        view = APIRootBaseView()
        request = request_factory.get("/fake-url/")
        request.user = user
        view.request = request

        with pytest.raises(NotImplementedError):
            view.get_routes(request)

    def test_response(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):

        view = APIRootBaseView()
        request = request_factory.get("/fake-url/")
        request.user = user
        view.request = request
        routes = {"users": "/api/accounts/users/"}

        with patch("common.views.api.APIRootBaseView.get_routes") as mock:
            mock.return_value = routes

            response = view.get(request)

            assert isinstance(response, Response)
            assert response.data == routes


{%- if cookiecutter.use_graphql == 'y' %}
class TestDRFGraphQL:
    """Test suite for the DRFGraphQL view."""

    def test_parse_body_django(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        """Ensure the parse body function returns a dict containing the request data."""

        request = request_factory.post("some-url")
        request.user = user
        request.POST = {"payload": "testing"}

        schema = MagicMock(spec=GraphQLSchema)
        view = DRFGraphQL(schema=schema)
        assert view.parse_body(request=request) == request.POST

    def test_parse_body_rest_framework(
        self, user: settings.AUTH_USER_MODEL, api_request_factory: APIRequestFactory
    ):
        """Ensure the parse body function returns a dict containing the request data."""

        request = MagicMock(spec=Request)
        request.user = user
        request.data = {"payload": "testing"}

        schema = MagicMock(spec=GraphQLSchema)
        view = DRFGraphQL(schema=schema)
        assert view.parse_body(request=request) == request.data
{%- endif %}
