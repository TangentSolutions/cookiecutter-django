from typing import Any
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.request import Request


# Custom user model
User = get_user_model()


class RequestUserIsInstanceUser(permissions.BasePermission):
    """Custom permission class specifically api views which make use
    of the User model.
    """

    def has_object_permission(
        self, request: Request, view: Any, instance: User
    ) -> bool:
        """Check if the request user is the user requesting the specified
        user instance.
        """

        if not isinstance(instance, User):
            message = (
                f'\'{self.__class__}\' is only applicable to '
                ' api views which make use of the User model.'
            )

            raise TypeError(message)

        return request.user == instance
