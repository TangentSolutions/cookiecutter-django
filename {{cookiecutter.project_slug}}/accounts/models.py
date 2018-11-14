from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.urls import reverse as django_reverse
from rest_framework.reverse import reverse as drf_reverse


class User(AbstractUser):
    """Custom User model."""

    id_number = models.CharField(
        _("South African identity number of the user"), blank=True, max_length=13
    )

    def get_absolute_url(self, api: bool = False) -> str:
        """Resolve the url for the user detail template or api view.

        Args:
            api: If true the url for the detail resource on the user api will
                 will be returned.
        """

        if api:
            return drf_reverse("accounts-api:user-detail", kwargs={"pk": self.pk})
        else:
            return django_reverse(
                "accounts:user-detail", kwargs={"username": self.username}
            )
