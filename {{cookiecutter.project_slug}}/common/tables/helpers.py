from django_tables2.export.views import ExportMixin
from django_tables2.views import SingleTableMixin
from django_filters.views import FilterView


class PagedFilteredTableView(ExportMixin, SingleTableMixin, FilterView):
    strict = False

    def get_filterset(self, filterset_class):
        filter_instance = super().get_filterset(filterset_class)
        filter_instance.form.helper = self.formhelper_class()
        return filter_instance
