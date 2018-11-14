from django import forms
from common.validation import is_valid_luhn_algorithm, is_valid_cipc_registration_number


class LuhnField(forms.CharField):
    """Django form field to validate a string using luhn's algorithm.

    The LuhnField subclasses CharField and provides all the same validation
    as CharField would however provides an additional validation step where the
    field is validated using the luhn algorithm. This field is useful for validating
    South Africa ID and VAT numbers.
    """

    default_error_messages = {"invalid_input": "The value provided is invalid"}

    def validate(self, value: str) -> None:
        """Validate the field using luhn's algorithm."""

        super().validate(value)

        try:
            is_valid = is_valid_luhn_algorithm(value)
        except (TypeError, ValueError):
            is_valid = False

        if not is_valid:
            raise forms.ValidationError(self.error_messages["invalid_input"])


class CompanyRegistrationNumberField(forms.CharField):
    """Django form field which validates the field according to the
    South African company registration number format.

    South African company registration numbers are issued by Cipc and
    take the following form:

    - \\d{4}/\\d{6}/\\d{2}

    Where:
        - \\d{4} is the year of incorporation
        - \\d{6} is a six digit number assigned by the CIPC
        - \\d{2} represents the type of company

    For valid CIPC company types see common.validation.CIPC_COMPANY_CHOICES.
    """

    default_error_messages = {
        "invalid_input": r"The registration number provided does not match the format \'\d{4}/\d{6}/\d{2}\'"
    }

    def validate(self, value: str) -> None:
        """Validate the field using the is_valid_cipc_registration_number helper function."""

        super().validate(value)

        try:
            is_valid = is_valid_cipc_registration_number(value)
        except (TypeError, ValueError):
            is_valid = False

        if not is_valid:
            raise forms.ValidationError(self.error_messages["invalid_input"])
