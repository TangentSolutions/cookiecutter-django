from django.contrib.auth import get_user_model

import django_filters


class UserFilterSet(django_filters.FilterSet):
    """Filterset class for the user model."""

    class Meta:
        model = get_user_model()
        fields = {
            "email": ["icontains"],
            "first_name": ["icontains"],
            "last_name": ["icontains"],
            "date_joined": ["year__gte"],
        }
