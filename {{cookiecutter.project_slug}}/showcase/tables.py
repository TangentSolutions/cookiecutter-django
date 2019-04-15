from django.urls import reverse
from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth import get_user_model
from django_tables2 import columns

import django_tables2


User = get_user_model()


class UserTable(django_tables2.Table):
    """User table to showcase django tables 2."""

    export_formats = ('csv', 'json', 'latex', 'ods', 'tsv', 'xls', 'xlsx', 'yml')
    {%- raw %}
    username = columns.TemplateColumn(
        """<a href="{% url 'accounts:user-detail' username=value %}">{{value}}</a>"""
    )
    {% endraw %}
    first_name_is_long = columns.Column(
        verbose_name='First name is long',
        accessor='username',
        orderable=False,
        exclude_from_export=True
    )

    class Meta:
        model = User
        template_name = 'django_tables2/bootstrap.html'
        fields = ['username', 'email', 'first_name', 'last_name', 'first_name_is_long']

    @staticmethod
    def render_first_name_is_long(value) -> str:
        """Checks if the user's name is longer than 10 characters and returns html."""

        if len(value) > 10:
            {% raw %}
            element = f"""
                <div>
                    <i class="fas fa-exclamation-triangle"></i>
                </div>
            """
            {%- endraw %}
        else:
            element = ''

        return format_html(element)


class UserTablePdf(UserTable):
    """User table to showcase django tables 2 export to pdf."""

    class Meta:
        exclude = ('first_name_is_long',)
