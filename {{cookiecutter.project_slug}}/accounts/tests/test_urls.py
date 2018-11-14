from django.conf import settings
from django.urls import reverse, resolve

import pytest


pytestmark = pytest.mark.django_db


def test_detail(user: settings.AUTH_USER_MODEL):
    assert (
        reverse("accounts:detail", kwargs={"username": user.username})
        == f"/users/{user.username}/"
    )
    assert resolve(f"/accounts/{user.username}/").view_name == "accounts:detail"


def test_list():
    assert reverse("accounts:list") == "/accounts/"
    assert resolve("/accounts/").view_name == "accounts:list"


def test_update():
    assert reverse("accounts:update") == "/accounts/update/"
    assert resolve("/users/~update/").view_name == "accounts:update"


def test_redirect():
    assert reverse("accounts:redirect") == "/accounts/redirect/"
    assert resolve("/accounts/redirect/").view_name == "accounts:redirect"
