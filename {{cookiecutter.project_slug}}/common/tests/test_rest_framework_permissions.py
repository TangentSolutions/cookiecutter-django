from django.contrib.auth import get_user_model
from rest_framework.test import APIRequestFactory
from unittest.mock import MagicMock, patch
from common.rest_framework.permissions import (
    has_object_permission,
    get_permission_dict,
    UserRolePermission,
)

import pytest


pytestmark = pytest.mark.django_db
User = get_user_model()


@pytest.fixture
def user():
    user = User.objects.create(username="test")
    user.set_password("test")
    return user


@pytest.fixture
def superuser(user: User):
    user.is_superuser = True
    user.is_staff = True
    user.save()

    return user


class TestHasObjectPermission:
    """Test suite for the has_object_permission function."""

    def test_has_object_permission_existing(
        self, vendor_admin: User, api_request_factory: APIRequestFactory
    ):
        """Ensure the has_object_read_permission is called when passing read."""

        request = api_request_factory.get("some-url")
        request.user = vendor_admin
        instance = MagicMock()

        has_object_permission(request, "read", instance)
        instance.has_object_read_permission.assert_called()

    def test_has_object_permission_mapped(
        self, vendor_admin: User, api_request_factory: APIRequestFactory
    ):
        """Ensure the has_object_write_permission is called when passing create."""

        request = api_request_factory.get("some-url")
        request.user = vendor_admin
        instance = MagicMock()
        instance.has_object_create_permission = None

        has_object_permission(request, "create", instance)
        instance.has_object_write_permission.assert_called()

    def test_has_object_permission_missing(
        self, vendor_admin: User, api_request_factory: APIRequestFactory
    ):
        """Ensure that when no permission function is found False is returned."""

        request = api_request_factory.get("some-url")
        request.user = vendor_admin
        instance = MagicMock()
        instance.has_object_testing_permission = None
        instance.has_object_None_permission = None

        assert has_object_permission(request, "testing", instance) is False


class TestGetPermisssionDict:
    """Test suite for the get_permission_dict function."""

    def test_get_permission_dict_superuser(
        self, superuser: User, api_request_factory: APIRequestFactory
    ):
        """Ensure superusers have full access."""

        request = api_request_factory.get("some-url")
        request.user = superuser
        instance = MagicMock()

        expected_dict = {"read": True, "write": True}
        actual_dict = get_permission_dict(request=request, instance=instance)

        assert expected_dict == actual_dict

    def test_get_permission_dict(
        self, vendor_admin: User, api_request_factory: APIRequestFactory
    ):
        request = api_request_factory.get("some-url")
        request.user = vendor_admin
        instance = MagicMock()

        def mock_permission(value):
            return value

        instance.has_object_read_permission = lambda **kwargs: mock_permission(True)
        instance.has_object_write_permission = lambda **kwargs: mock_permission(False)

        expected_dict = {"read": True, "write": False}
        actual_dict = get_permission_dict(request=request, instance=instance)

        assert expected_dict == actual_dict


class TestUserRolePermission:
    """Test suite for UserRolePermission."""

    def test_superuser(self, superuser: User, api_request_factory: APIRequestFactory):
        """Ensure superusers have full access."""

        request = api_request_factory.get("some-url")
        request.user = superuser

        permission = UserRolePermission()
        actual_permission = permission.has_object_permission(
            request=request, view=None, instance=None
        )
        assert actual_permission is True

    def test_regular_user(self, user: User, api_request_factory: APIRequestFactory):
        """Ensure superusers have full access.

        This test mocks out common.rest_framework.permissions.has_object_permission as this
        method is tested above.
        """

        request = api_request_factory.get("some-url")
        request.user = user
        view = MagicMock()
        instance = MagicMock()

        permission = UserRolePermission()
        with patch(
            "common.rest_framework.permissions.has_object_permission", return_value=True
        ):
            actual_permission = permission.has_object_permission(
                request=request, view=view, instance=instance
            )
            assert actual_permission is True
