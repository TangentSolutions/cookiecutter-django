from rest_framework import fields
from rest_framework import serializers
from {{ cookiecutter.project_slug }}.common.validation import luhn_algorithm


class LuhnField(fields.CharField):
    """Custom DRF field which validates a string using the luhn algorithm.

    This field is useful for validating South Africa ID and VAT numbers.
    """

    default_error_messages = {'invalid_input': 'The value provided is invalid'}

    def to_internal_value(self, value: str) -> str:
        """Validate the input value using luhn's algorithm."""

        value = super().to_internal_value(value)

        try:
            is_valid = luhn_algorithm(value)
        except (TypeError, ValueError):
            is_valid = False

        if not is_valid:
            raise serializers.ValidationError(self.error_messages['invalid_input'])

        return value
