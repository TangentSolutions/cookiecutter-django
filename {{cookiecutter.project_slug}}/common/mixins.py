from typing import Union
from django.http import HttpRequest
from rest_framework.request import Request


UnionRequest = Union[HttpRequest, Request]


class ObjectPermissionsModelMixin:
    """Base model for the models using the object level permissions helper
    functions.

    This class provides the scafolding for some helper functions required
    for permissions.
    """

    def has_object_read_permission(self, request: UnionRequest) -> bool:
        """Check if the request user has permissions for this instance of the model."""

        return False

    def has_object_write_permission(self, request: UnionRequest) -> bool:
        """Check if the request user has permissions for this instance of the model."""

        return False
