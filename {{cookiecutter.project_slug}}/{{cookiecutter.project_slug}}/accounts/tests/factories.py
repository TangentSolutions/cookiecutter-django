from typing import Any, Sequence
from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, Faker, post_generation


class UserFactory(DjangoModelFactory):
    """Django user factory for testing purposes."""

    username = Faker('user_name')
    email = Faker('email')
    name = Faker('name')

    @post_generation
    def password(self, create: bool, extracted: Sequence[Any], **kwargs) -> None:
        """Post generation hook to set the user's password.
        """

        password = Faker(
            'password',
            length=42,
            special_chars=True,
            digits=True,
            upper_case=True,
            lower_case=True,
        ).generate(extra_kwargs={})
        self.set_password(password)

    class Meta:
        model = get_user_model()
        django_get_or_create = ['username']
