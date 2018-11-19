from common.faker.providers import SouthAfricaCommonProvider
from common.validation import is_valid_luhn_algorithm, is_valid_cipc_registration_number


def test_id_number(faker):
    """Ensure the SouthAfricaCommonProvider can generate valid id numbers."""

    faker.add_provider(SouthAfricaCommonProvider)
    id_number = faker.id_number()

    assert len(id_number) == 13
    assert is_valid_luhn_algorithm(id_number) is True


def test_vat_number(faker):
    """Ensure the SouthAfricaCommonProvider can generate valid VAT numbers."""

    faker.add_provider(SouthAfricaCommonProvider)
    vat_number = faker.vat_number()

    assert len(vat_number) == 10
    assert is_valid_luhn_algorithm(vat_number) is True


def test_cipc_registration_number(faker):
    """Ensure the SouthAfricaCommonProvider can generate valid CIPC registration numbers."""

    faker.add_provider(SouthAfricaCommonProvider)
    cipc_registration_number = faker.cipc_registration_number()

    assert len(cipc_registration_number) == 14
    assert is_valid_cipc_registration_number(cipc_registration_number) is True
