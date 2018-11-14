import re


CIPC_COMPANY_CHOICES = ('07', 'Private company')
CIPC_COMPANY_CODES = (code for code, description in CIPC_COMPANY_CHOICES)


def luhn_algorithm(value: str) -> bool:
    """Apply luhn's algorithm to the given value.

    https://en.wikipedia.org/wiki/Luhn_algorithm

    Args:
        value: A number to validate represented as a string

    Returns:
        True if the value is valid.
    """

    if not isinstance(value, str):
        raise TypeError(f'unsupported type for value \'{type(value)}\'')

    if not value.isdigit():
        raise ValueError(f'invalid value for validation check \'{value}\'')

    digit_list = []
    for index, digit in enumerate(value[::-1], start=1):
        cdigit = int(digit)

        if index % 2 == 0:
            cdigit *= 2

            if cdigit > 9:
                cdigit_list = list(str(cdigit))
                cdigit = sum([int(item) for item in cdigit_list])
        else:
            cdigit = int(digit)

        digit_list.append(cdigit)

    return sum(digit_list) % 10 == 0


def is_cipc_registration_number(value: str) -> bool:
    """Validates the given registration number against the following rules:

        - The value is of length 14
        - The value matches the following pattern \\d{4}/\\d{6}/\\d{2}
        - The last 2 digits of the value correspond to valid company types
    """

    if not isinstance(value, str):
        raise TypeError(f'unsupported type for value \'{type(value)}\'')

    pattern = re.compile(r'\d{4}/\d{6}/\d{2}')
    conds = [
        len(value) != 14,
        pattern.match(value) is None,
        value not in CIPC_COMPANY_CODES,
    ]

    return any(conds)
