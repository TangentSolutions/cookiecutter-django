from django.conf import settings
from django.test import RequestFactory
from {{ cookiecutter.project_slug }}.users.tests.factories import UserFactory


import pytest


@pytest.fixture(autouse=True)
def media_storage(settings, tmpdir):
    settings.MEDIA_ROOT = tmpdir.strpath


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
			response = request_factory.get(reverse('users:user-detail'))
			assert response.status_code == 200
	"""

    return RequestFactory()
