from django.conf import settings
from rest_framework.test import APIClient, APIRequestFactory
from rest_framework.test import force_authenticate
from rest_framework.reverse import reverse
from accounts.serializers import UserSerializer
from accounts.views.api import UserViewSet
from accounts.tests.factories import UserFactory
from common.rest_framework.utils import CommonResponses

import pytest


pytestmark = pytest.mark.django_db


class TestUserViewSet:
    """Test suite for the UserViewSet."""

    def test_detail_action_access(
        self,
        user: settings.AUTH_USER_MODEL,
        api_client: APIClient,
        api_common_responses: CommonResponses,
    ):
        """Ensure the me action is available."""

        api_client.force_authenticate(user)
        response = api_client.get(
            reverse("accounts-api:user-detail", kwargs={"pk": user.pk})
        )

        assert response.status_code == 403
        assert response.data == api_common_responses.missing_permission

    def test_me_action_authenticated(
        self,
        user: settings.AUTH_USER_MODEL,
        api_client: APIClient,
        api_request_factory: APIRequestFactory,
    ):
        """Ensure the me action is available."""

        url = reverse("accounts-api:user-me")
        request = api_request_factory.get(url)

        api_client.force_authenticate(user)
        response = api_client.get(url)

        serializer = UserSerializer(instance=user, context={"request": request})
        assert response.data == serializer.data

    def test_me_action_unauthenticated(
        self,
        user: settings.AUTH_USER_MODEL,
        api_client: APIClient,
        api_common_responses: CommonResponses,
    ):
        """Ensure the me action is available."""

        response = api_client.get(reverse("accounts-api:user-me"))

        assert response.status_code == 403
        assert response.data == api_common_responses.missing_authentication

    def test_check_username_availability_true(self, api_client: APIClient):
        """Ensure that the check username availability method returns
        True when a username is available.
        """

        response = api_client.post(
            reverse("accounts-api:user-check-username-availability"),
            {"username": "testing"},
        )

        assert response.status_code == 200
        assert response.data == {"username": "testing", "available": True}

    def test_check_username_availability_false(
        self, user: settings.AUTH_USER_MODEL, api_client: APIClient
    ):
        """Ensure that the check username availability method returns
        False when a username is not available.
        """

        response = api_client.post(
            reverse("accounts-api:user-check-username-availability"),
            {"username": user.username},
        )

        assert response.status_code == 200
        assert response.data == {"username": user.username, "available": False}
