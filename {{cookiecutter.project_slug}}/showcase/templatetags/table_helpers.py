from django import template


register = template.Library()


@register.simple_tag
def table_is_filtered(table, request) -> bool:
    """Helper tag which given a django_tables2 Table and a request
    instance determines whether there are any filters in the query params
    for the specified table.

    This is useful to collapse filter accordians.

    Args:
        table: A django_tables2 table instance
        request: A django request instance

    Returns:
        True if the table is currently filtered.
    """

    names_set = set([column.name for column in table.columns])
    queryparam_set = set()

    for key, value in request.GET.items():
        if value == '':
            continue

        queryparam_set.add(key.split('__')[0])

    if 'page' in queryparam_set:
        queryparam_set.remove('page')

    return len(names_set.intersection(queryparam_set)) != 0
