import pytest
from Otp.authentication_service import is_valid


def test_is_valid(mocker):
    given_otp(mocker, otp="000000")
    given_password(mocker, account="91")
    assert is_valid("joey", "91000000") == True


def test_is_not_valid(mocker):
    given_otp(mocker, otp="000000")
    given_password(mocker, account="91")
    assert is_valid("joey", "wrong password") == False


def test_should_log_when_not_valid(mocker):
    mocked_log = mocker.patch("Otp.authentication_service.log")
    given_login_failed(mocker)

    assert mocked_log.call_count >= 1
    assert "joey" in mocked_log.call_args[0][0]


def given_login_failed(mocker):
    given_otp(mocker, otp="000000")
    given_password(mocker, account="91")
    assert is_valid("joey", "wrong password") == False


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
