from django.conf import settings
from django.test import RequestFactory, Client
from rest_framework.test import APIRequestFactory, APIClient
from accounts.tests.factories import UserFactory
from common.rest_framework.utils import CommonResponses
from faker import Faker

import pytest


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


@pytest.fixture
def faker() -> Faker:
    """Pytest fixture to inject an instance of the Faker object.

    Usage:
        def test_feature(faker):
            first_name = faker.first_name()
    """

    return Faker()


@pytest.fixture
def user() -> settings.AUTH_USER_MODEL:
    """Pytest user fixture which can be injected into test cases.

    Usage:

        def test_user(user):
            assert user.username is not None
    """

    return UserFactory()


@pytest.fixture
def request_factory() -> RequestFactory:
    """Pytest fixture which injects a django request factory instance.

    Usage:
        def test_user_view(request_factory):
            response = request_factory.get(reverse('accounts:user-detail'))
            assert response.status_code == 200
    """

    return RequestFactory()


@pytest.fixture
def api_request_factory() -> APIRequestFactory:
    """Pytest fixture which injects a django rest framework request factory instance.

    Usage:
        def test_user_view(api_request_factory):
            payload = ...
            response = api_request_factory.post(reverse('accounts-api:user-list'), payload)
    """

    return APIRequestFactory()


@pytest.fixture
def django_client() -> Client:
    """Pytest fixture which injects a django test client.

    Usage:
        def test_user_view():
            response = client.get(reverse('my-view'))
    """

    return Client()


@pytest.fixture
def api_client() -> APIClient:
    """Pytest fixture which injects a django rest framework client instance.

    Usage:
        def test_user_view(api_client):
            payload = ...
            response = api_client.post(reverse('accounts-api:user-list'), payload)
    """

    return APIClient()


@pytest.fixture
def api_common_responses() -> CommonResponses:
    """Pytest fixture which injects a class with common responses useful for testing.

    Usage:
        def test_user_view(api_common_responses):
            payload = ...
            response = api_request_factory.post(reverse('accounts-api:user-list'), payload)
    """

    return CommonResponses()
