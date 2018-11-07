from typing import Dict
from django.contrib.auth import get_user_model
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, SingleTableView
from showcase.tables import UserTable
from showcase.filters import UserFilterSet


User = get_user_model()


class ShowcaseDemoView(SingleTableMixin, FilterView):
    """Demo view showcasing tables, filters and export."""

    model = User
    template_name = 'showcase/table.html'
    table_class = UserTable
    filterset_class = UserFilterSet
    paginate_by = 5
    strict = False

    def get_table_kwargs(self) -> Dict:
        """These kwargs will be passed to the table constructor.

        Returns:
            A dict to be passed to the table class as kwargs.
        """

        return {}


# View functions
showcase_demo_view = ShowcaseDemoView.as_view()
