from django.conf import settings
from django.urls import reverse, resolve

import pytest


pytestmark = pytest.mark.django_db


def test_detail(user: settings.AUTH_USER_MODEL):
    assert (
        reverse("accounts:user-detail", kwargs={"username": user.username})
        == f"/accounts/{user.username}/"
    )
    assert resolve(f"/accounts/{user.username}/").view_name == "accounts:user-detail"


def test_list():
    assert reverse("accounts:user-list") == "/accounts/"
    assert resolve("/accounts/").view_name == "accounts:user-list"


def test_update():
    assert reverse("accounts:user-update") == "/accounts/update/"
    assert resolve("/accounts/update/").view_name == "accounts:user-update"


def test_redirect():
    assert reverse("accounts:user-redirect") == "/accounts/redirect/"
    assert resolve("/accounts/redirect/").view_name == "accounts:user-redirect"
