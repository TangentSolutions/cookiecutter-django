from typing import Dict
from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin, SingleTableView
from django_tables2.export.views import ExportMixin
from django_weasyprint import WeasyTemplateResponseMixin
from showcase.tables import UserTable, UserTablePdf
from showcase.filters import UserFilterSet


User = get_user_model()


class ShowcaseDemoView(LoginRequiredMixin, ExportMixin, SingleTableMixin, FilterView):
    """Demo view showcasing tables, filters and export."""

    model = User
    template_name = "showcase/table.html"
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


class ShowcaseDemoViewPrintView(
    LoginRequiredMixin, WeasyTemplateResponseMixin, SingleTableView
):
    """Print as PDF view for the ShowcaseDemoView."""

    model = User
    template_name = "showcase/table_pdf.html"
    table_class = UserTablePdf
    table_pagination = False
    pdf_stylesheets = [str(settings.ROOT_DIR.path("static")) + "/css/bootstrap.min.css"]


# View functions
showcase_demo_view = ShowcaseDemoView.as_view()
showcase_demo_view_print = ShowcaseDemoViewPrintView.as_view()
