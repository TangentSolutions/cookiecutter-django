from django.conf import settings
from rest_framework.reverse import reverse as drf_reverse

import pytest


pytestmark = pytest.mark.django_db


def test_user_get_absolute_url(user: settings.AUTH_USER_MODEL):
    assert user.get_absolute_url(api=False) == f"/accounts/{user.username}/"


def test_user_get_absolute_url_api(user: settings.AUTH_USER_MODEL):
    expected_result = drf_reverse("accounts-api:user-detail", kwargs={"pk": user.pk})
    assert user.get_absolute_url(api=True) == expected_result
