from django.conf import settings
from django.test import RequestFactory
from django.urls import resolve
from django.urls import reverse as django_reverse
from rest_framework.reverse import reverse as drf_reverse
from rest_framework.response import Response
from accounts.urls import APIRootView

import pytest


pytestmark = pytest.mark.django_db


def test_detail(user: settings.AUTH_USER_MODEL):
    assert (
        django_reverse("accounts:user-detail", kwargs={"username": user.username})
        == f"/accounts/{user.username}/"
    )
    assert resolve(f"/accounts/{user.username}/").view_name == "accounts:user-detail"


def test_list():
    assert django_reverse("accounts:user-list") == "/accounts/"
    assert resolve("/accounts/").view_name == "accounts:user-list"


def test_update():
    assert django_reverse("accounts:user-update") == "/accounts/update/"
    assert resolve("/accounts/update/").view_name == "accounts:user-update"


def test_redirect():
    assert django_reverse("accounts:user-redirect") == "/accounts/redirect/"
    assert resolve("/accounts/redirect/").view_name == "accounts:user-redirect"


def test_api_root():
    assert drf_reverse("accounts-api:api-root") == "/api/accounts/"


class TestApiRootView:
    def test_api_root_get_routes(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        """Ensure the api root view produces the required hyperlinks."""

        view = APIRootView()
        url = drf_reverse("accounts-api:api-root")
        request = request_factory.get(url)
        request.user = user

        view.request = request
        routes = view.get_routes(request)

        assert isinstance(routes, dict)
        assert routes["users"] == drf_reverse("accounts-api:user-list", request=request)
        assert routes["check-username-availability"] == drf_reverse(
            "accounts-api:user-check-username-availability", request=request
        )

    def test_api_root_get(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        """Ensure the api root view produces the required hyperlinks."""

        view = APIRootView()
        url = drf_reverse("accounts-api:api-root")
        request = request_factory.get(url)
        request.user = user

        view.request = request
        response = view.get(request)
        assert isinstance(response, Response)


def test_api_user_list():
    assert drf_reverse("accounts-api:user-list") == "/api/accounts/users/"


def test_api_user_detail(user: settings.AUTH_USER_MODEL):
    assert (
        drf_reverse("accounts-api:user-detail", kwargs={"pk": user.pk})
        == f"/api/accounts/users/{user.pk}/"
    )


def test_api_username_available():
    assert (
        drf_reverse("accounts-api:user-check-username-availability")
        == "/api/accounts/users/check-username-availability/"
    )
