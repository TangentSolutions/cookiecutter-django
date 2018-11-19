from django.forms import ValidationError
from common.forms.fields import LuhnField, CompanyRegistrationNumberField

import pytest


class TestLuhnField:
    def test_forms_luhn_field_raises_validation_error(self):
        """Ensure the luhn field raises a validation error for an invalid value."""

        field = LuhnField()
        with pytest.raises(ValidationError):
            field.validate("testing")

        with pytest.raises(ValidationError):
            field.validate(100)  # Will raise due to invalid type

    def test_forms_luhn_field(self):
        """Ensure the luhn is able to validate a valid value."""

        field = LuhnField()
        field.validate("1928376459096")


class TestCompanyRegistrationField:
    def test_forms_cipc_company_registration_number_raises_validation_error(self):
        """Ensure the cipc company registration number field raises a validation
        error for an invalid value.
        """

        field = CompanyRegistrationNumberField()
        with pytest.raises(ValidationError):
            field.validate("testing")

        with pytest.raises(ValidationError):
            field.validate(100)  # Will raise due to invalid type

    def test_forms_cipc_company_registration_number(self):
        """Ensure the cipc companyn registration number field is able to
        validate a valid value.
        """

        field = CompanyRegistrationNumberField()
        field.validate("2018/029674/07")
