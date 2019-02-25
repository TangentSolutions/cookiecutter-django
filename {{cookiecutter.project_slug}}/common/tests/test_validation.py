from common.validation import (
    is_valid_luhn_algorithm,
    is_valid_cipc_registration_number,
    append_check_digit_luhn_algorithm,
)

import pytest


class TestIsValidLuhnAlgorithm:
    def test_is_valid_luhn_algorithm(self):
        """Test that a given string is valid according to luhn's algorithm."""

        assert is_valid_luhn_algorithm("1928376459096") is True

    def test_is_valid_luhn_algorithm_raises_type_error(self):
        """Ensure that if given a value not of type string a type error is raised."""

        with pytest.raises(TypeError):
            is_valid_luhn_algorithm(100)

    def test_is_valid_luhn_algorithm_raises_value_error(self):
        """Ensure that if given a string that contains non digits a value error is raised."""

        with pytest.raises(ValueError):
            is_valid_luhn_algorithm("100testing")


class TestAppendCheckDigitLuhnAlgorithm:
    def test_append_check_digit_luhn_algorithm(self):
        """Test that the generated check digit is valid."""

        assert append_check_digit_luhn_algorithm("192837645909")[-1] == "6"

    def test_append_check_digit_luhn_algorithm_raises_type_error(self):
        """Ensure that if given a value not of type string a type error is raised."""

        with pytest.raises(TypeError):
            append_check_digit_luhn_algorithm(100)

    def test_append_check_digit_luhn_algorithm_raises_value_error(self):
        """Ensure that if given a string that contains non digits a value error is raised."""

        with pytest.raises(ValueError):
            append_check_digit_luhn_algorithm("100testing")


class TestIsValidCipcRegistrationNumber:
    def test_is_valid_cipc_registration_number(self):
        """Test the cipc company registration number validator."""

        assert is_valid_cipc_registration_number("2018/209387/07") is True

    def test_is_valid_cipc_registration_number_raises_type_error(self):
        """Ensure that if given a value not of type string a type error is raised."""

        with pytest.raises(TypeError):
            is_valid_cipc_registration_number(100)

    def test_invalid_format(self):
        """Ensure false is returned if an invalid format is provided."""

        assert is_valid_cipc_registration_number("testingtesting") is False
