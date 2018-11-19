from django.forms import ValidationError
from common.forms.fields import LuhnField, CompanyRegistrationNumberField

import pytest


def test_forms_luhn_field_raises_validation_error():
    """Ensure the luhn field raises a validation error for an invalid value."""

    with pytest.raises(ValidationError):
        field = LuhnField()
        field.validate('testing')


def test_forms_luhn_field():
    """Ensure the luhn is able to validate a valid value."""

    field = LuhnField()
    field.validate('1928376459096')


def test_forms_cipc_company_registration_number_raises_validation_error():
    """Ensure the cipc company registration number field raises a validation
    error for an invalid value.
    """

    with pytest.raises(ValidationError):
        field = CompanyRegistrationNumberField()
        field.validate('testing')


def test_forms_cipc_company_registration_number():
    """Ensure the cipc companyn registration number field is able to
    validate a valid value.
    """

    field = CompanyRegistrationNumberField()
    field.validate('2018/029674/07')
