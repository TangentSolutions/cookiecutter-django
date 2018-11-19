from rest_framework.serializers import ValidationError
from common.rest_framework.fields import LuhnField, CompanyRegistrationNumberField

import pytest


def test_rest_framework_luhn_field_raises_validation_error():
    """Ensure that the rest framework field raises a validation error
    for an invalid input."""

    with pytest.raises(ValidationError):
        field = LuhnField()
        field.to_internal_value('testing')


def test_rest_framework_luhn_field():
    """Ensure that the rest framework field returns the value when it is valid."""

    assert LuhnField().to_internal_value('1928376459096') == '1928376459096'


def test_rest_framework_company_registration_number_field_raises_validation_error():
    """Ensure that the rest framework field raises a validation error
    for an invalid input."""

    with pytest.raises(ValidationError):
        field = CompanyRegistrationNumberField()
        field.to_internal_value('testing')


def test_rest_framework_company_registration_number_field():
    """Ensure that the rest framework field returns the value when it is valid."""

    assert (
        CompanyRegistrationNumberField().to_internal_value('2018/029674/07')
        == '2018/029674/07'
    )
