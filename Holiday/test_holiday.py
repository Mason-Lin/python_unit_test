from datetime import date

import pytest

from Holiday.holiday import say_hello


def test_today_is_xmax(mocker):
    given_today(mocker, month=12, day=25)
    assert say_hello() == "Merry Xmax"


def test_today_is_not_xmax(mocker):
    given_today(mocker, month=11, day=25)
    assert say_hello() == "Today Is Not Xmax"


def given_today(mocker, month, day):
    ANY_YEAR = 2019
    mocker.patch(
        "Holiday.holiday.get_today", return_value=date(ANY_YEAR, month, day)
    )
