from faker.providers import BaseProvider
from common.validation import append_check_digit_luhn_algorithm

import secrets


random = secrets.SystemRandom()


class SouthAfricaCommonProvider(BaseProvider):
    """Faker provider for common South African data."""

    @staticmethod
    def _get_random_integer(n: int) -> int:
        """Generate a random int of length n."""

        return random.randrange(10 ** (n - 1), 10 ** n)

    def id_number(self) -> str:
        """Create a fake id number."""

        id_number_base = str(self._get_random_integer(12))
        return append_check_digit_luhn_algorithm(id_number_base)

    def cipc_registration_number(self) -> str:
        """Create a fake cipc registration number."""

        company_type = "07"
        return "{}/{}/{}".format(
            self._get_random_integer(4), self._get_random_integer(6), company_type
        )

    def vat_number(self) -> str:
        """Create a fake company vat number."""

        vat_number_base = str(self._get_random_integer(9))
        return append_check_digit_luhn_algorithm(vat_number_base)
