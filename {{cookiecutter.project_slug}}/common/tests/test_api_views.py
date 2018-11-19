from django.conf import settings
from django.test import RequestFactory
from rest_framework.response import Response
from common.views.api import APIRootBaseView
from unittest.mock import patch

import pytest


pytestmark = pytest.mark.django_db


class TestAPIRootBaseView:
    def test_get_routes_raises(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):

        view = APIRootBaseView()
        request = request_factory.get("/fake-url/")
        request.user = user
        view.request = request

        with pytest.raises(NotImplementedError):
            routes = view.get_routes(request)

    def test_get_routes_raises(
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
