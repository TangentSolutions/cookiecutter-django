from rest_framework.serializers import ValidationError
from common.rest_framework.fields import LuhnField, CompanyRegistrationNumberField

import pytest


class TestLuhnField:
    def test_rest_framework_luhn_field_raises_validation_error(self):
        """Ensure that the rest framework field raises a validation error
        for an invalid input.
        """

        with pytest.raises(ValidationError):
            field = LuhnField()
            field.to_internal_value("testing")

    def test_rest_framework_luhn_field(self):
        """Ensure that the rest framework field returns the value when it is valid."""

        assert LuhnField().to_internal_value("1928376459096") == "1928376459096"


class TestCompanyRegistrationNumberField:
    def test_raises_validation_error(self):
        """Ensure that the rest framework field raises a validation error
        for an invalid input.
        """

        with pytest.raises(ValidationError):
            field = CompanyRegistrationNumberField()
            field.to_internal_value("testing")

    def test_rest_framework_company_registration_number_field(self):
        """Ensure that the rest framework field returns the value when it is valid."""

        assert (
            CompanyRegistrationNumberField().to_internal_value("2018/029674/07")
            == "2018/029674/07"
        )
