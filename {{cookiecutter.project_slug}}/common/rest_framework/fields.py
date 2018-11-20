from rest_framework import fields
from rest_framework import serializers
from common.validation import is_valid_luhn_algorithm, is_valid_cipc_registration_number


class LuhnField(fields.CharField):
    """Custom DRF field which validates a string using the luhn algorithm.

    This field is useful for validating South Africa ID and VAT numbers.
    """

    default_error_messages = {"invalid_input": "The value provided is invalid"}

    def to_internal_value(self, value: str) -> str:
        """Validate the input value using luhn's algorithm."""

        value = super().to_internal_value(value)

        try:
            is_valid = is_valid_luhn_algorithm(value)
        except (TypeError, ValueError):
            is_valid = False

        if not is_valid:
            raise serializers.ValidationError(self.error_messages["invalid_input"])

        return value


class CompanyRegistrationNumberField(fields.CharField):
    """Custom DRF field which check's if the format of a given value
    is a valid Cipc company registration number.
    """

    default_error_messages = {
        "invalid_input": r"The registration number provided does not match the format \'\d{4}/\d{6}/\d{2}\'"
    }

    def to_internal_value(self, value: str) -> str:
        """Validate the format of the given value."""

        value = super().to_internal_value(value)

        try:
            is_valid = is_valid_cipc_registration_number(value)
        except TypeError:
            is_valid = False

        if not is_valid:
            raise serializers.ValidationError(self.error_messages["invalid_input"])

        return value
