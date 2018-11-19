from django.conf import settings
from django.test import RequestFactory
from rest_framework.reverse import reverse as drf_reverse
from config.urls import APIRootView

import pytest


pytestmark = pytest.mark.django_db


class TestApiRootView:
    def test_api_root_get_routes(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        """Ensure the api root view produces the required hyperlinks."""

        view = APIRootView()
        url = drf_reverse("api-root")
        request = request_factory.get(url)
        request.user = user

        view.request = request
        routes = view.get_routes(request)

        assert isinstance(routes, dict)
        assert len(routes) == 1
        assert routes["accounts"] == drf_reverse(
            "accounts-api:api-root", request=request
        )
