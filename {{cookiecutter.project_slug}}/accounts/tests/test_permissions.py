from django.conf import settings
from django.test import RequestFactory
from django.contrib.auth.models import Group
from accounts.permissions import RequestUserIsInstanceUser
from accounts.views.api import UserViewSet
from accounts.tests.factories import UserFactory

import pytest


pytestmark = pytest.mark.django_db


class TestRequestUserIsInstanceUser:
    def test_has_object_permission_true(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        """Ensure the test_object_permission function works for a user attemping to
        access their own user record.
        """

        view = UserViewSet.as_view({"get": "retrieve"})
        request = request_factory.get("/fake-url/")
        request.user = user

        permission = RequestUserIsInstanceUser()
        has_object_permission = permission.has_object_permission(
            request=request, view=view, instance=user
        )

        assert has_object_permission is True

    def test_has_object_permission_false(self, request_factory: RequestFactory):
        """Ensure that the has_object_permission method returns False
        for a user trying to access another user's data.
        """

        me = UserFactory()
        imposter = UserFactory()

        view = UserViewSet.as_view({"get": "retrieve"})
        request = request_factory.get("/fake-url/")
        request.user = imposter

        permission = RequestUserIsInstanceUser()
        has_object_permission = permission.has_object_permission(
            request=request, view=view, instance=me
        )

        assert has_object_permission is False

    def test_has_object_permission_raises_type_error(
        self, user: settings.AUTH_USER_MODEL, request_factory: RequestFactory
    ):
        """Ensure the test_object_permission function works for a user attemping to
        access their own user record.
        """

        view = UserViewSet.as_view({"get": "retrieve"})
        request = request_factory.get("/fake-url/")
        request.user = user

        permission = RequestUserIsInstanceUser()
        group = Group.objects.create(name="testing")

        with pytest.raises(TypeError):
            permission.has_object_permission(request=request, view=view, instance=group)
