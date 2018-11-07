from django import template


register = template.Library()


@register.simple_tag
def table_is_filtered(table, queryparams) -> bool:
    """"""

    names_set = set([column.name for column in table.columns])
    queryparam_set = set()

    for key, value in queryparams.items():
        if value == '':
            continue

        queryparam_set.add(key.split('__')[0])

    if 'page' in queryparam_set:
        queryparam_set.remove('page')

    print(queryparam_set)
    return len(names_set.intersection(queryparam_set)) != 0
