import pytest
from Otp.authentication_service import is_valid


def test_is_valid(mocker):
    given_otp(mocker, otp="000000")
    given_password(mocker, account="91")
    assert is_valid("joey", "91000000") == True


def given_password(mocker, account):
    mocker.patch(
        "Otp.authentication_service.get_password_from_db",
        return_value=account,
    )


def given_otp(mocker, otp):
    mocker.patch(
        "Otp.authentication_service.get_otp",
        return_value=otp,
    )
