from django.test import RequestFactory
from showcase.templatetags.table_helpers import table_is_filtered
from django_tables2 import Table

import pytest
import django_tables2



@pytest.fixture
def table():
    """Generates a table class with a name field."""

    class TestTable(Table):
        name = django_tables2.Column()

    return TestTable([{"name": "rest_framework", "name": "django"}])



class TestTableIsFiltered:
    """Test suite for the table_is_filtered method."""

    def test_table_is_filtered_no_filters(self, request_factory: RequestFactory, table: Table):

        request = request_factory.get("fake-url")
        assert table_is_filtered(table, request) is False


    def test_table_is_filtered_with_filters(self, request_factory: RequestFactory, table: Table):

        request = request_factory.get("fake-url")
        request.GET = {"missing": "", "page": 1, "name__lte": 10}
        assert table_is_filtered(table, request) is True
