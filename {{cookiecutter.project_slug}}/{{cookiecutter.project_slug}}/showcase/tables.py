from django.urls import reverse
from django.utils.html import format_html
from django.contrib.staticfiles.templatetags.staticfiles import static
from django.contrib.auth import get_user_model
from django_tables2 import columns

import django_tables2


User = get_user_model()


class UserTable(django_tables2.Table):
    """User table to showcase django tables 2."""
    {% raw %}
    username = columns.TemplateColumn(
        """<a href="{% url 'users:detail' username=value %}">{{value}}</a>"""
    )
    {% endraw %}
    first_name_is_long = columns.Column(
        verbose_name='First name is long', accessor='username', orderable=False
    )

    class Meta:
        model = User
        template_name = 'django_tables2/bootstrap.html'
        fields = ['username', 'email', 'first_name', 'last_name', 'first_name_is_long']

    @staticmethod
    def render_first_name_is_long(value) -> str:
        """Checks if the user's name is longer than 10 characters and returns html."""

        if len(value) > 10:
            uri = static('feather/alert-triangle.svg')
            {% raw %}
            element = f"""
                <div>
                    <img class="invert" src="{uri}" alt="warning">
                </div>
            """
            {%- endraw %}
        else:
            element = ''

        return format_html(element)
