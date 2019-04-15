from typing import Any, Dict
from django.contrib.auth.models import AnonymousUser
from rest_framework.request import Request
from rest_framework.permissions import IsAuthenticated


ACTION_MAPPING = {
    "create": "write",
    "destroy": "write",
    "update": "write",
    "list": "read",
    "retrieve": "read",
}


def has_object_permission(
    request: Request, action: str, instance: Any, action_mapping: Dict = None
) -> bool:
    """Check if the specified user has the appropriate permissions for the specified instance."""

    # System wide permissions
    if request.user.is_superuser:
        return True

    conds = [
        isinstance(request.user, AnonymousUser) is True,
        getattr(request.user, "vendor", None) is None,
    ]

    if any(conds):
        return False

    if action_mapping is not None and isinstance(action_mapping, dict):
        ACTION_MAPPING_COPY = {**action_mapping, **ACTION_MAPPING}
    else:
        ACTION_MAPPING_COPY = ACTION_MAPPING.copy()

    # Check model permissions
    permission_checker = getattr(instance, f"has_object_{action}_permission", None)

    if permission_checker is None:
        action = ACTION_MAPPING_COPY.get(action, None)
        permission_checker = getattr(instance, f"has_object_{action}_permission", None)

    if permission_checker is not None:
        return permission_checker(request=request)
    else:
        return False


def get_permission_dict(request: Request, instance: Any) -> Dict:
    """Return the permissions for the specified user."""

    if request.user.is_superuser:
        return {"read": True, "write": True}

    return {
        action: has_object_permission(request, action, instance)
        for action in ["read", "write"]
    }


class UserRolePermission(IsAuthenticated):
    """Determines the request users permission based on their role."""

    def has_object_permission(self, request: Request, view: Any, instance: Any) -> bool:
        """At this stage it is determined that the user is the vendor admin.

        Given this only allow them access to their own company.
        """

        if request.user.is_superuser:
            return True

        action_mapping = getattr(view, "permission_action_mapping", {})
        return has_object_permission(request, view.action, instance, action_mapping)
