import pytest


pytestmark = pytest.mark.django_db


class TestPlaceholder:
    """"""

    def test_placeholder(self):
        assert 1 == 1
