from typing import Any, Sequence
from django.contrib.auth import get_user_model
from factory import DjangoModelFactory, post_generation
from {{ cookiecutter.project_slug }}.common.faker.providers import SouthAfricaCommonProvider

import faker
import factory


class UserFactory(DjangoModelFactory):
    """Django user factory for testing purposes."""

    username = factory.Faker('user_name')
    email = factory.Faker('email')

    class Meta:
        model = get_user_model()
        django_get_or_create = ['username']

    @factory.lazy_attribute
    def id_number(self) -> str:
        """Create a valid id number for the user."""

        fake = faker.Faker()
        fake.add_provider(SouthAfricaCommonProvider)

        return fake.id_number()

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
