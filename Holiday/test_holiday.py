from datetime import date


def test_today_is_xmax(mocker, holiday):
    given_today(mocker, month=12, day=25)
    assert holiday.say_hello() == "Merry Xmax"


def test_today_is_xmax_one_day_before_xmax(mocker, holiday):
    given_today(mocker, month=12, day=24)
    assert holiday.say_hello() == "Merry Xmax"


def test_today_is_not_xmax(mocker, holiday):
    given_today(mocker, month=11, day=25)
    assert holiday.say_hello() == "Today Is Not Xmax"


def given_today(mocker, month, day):
    ANY_YEAR = 2019
    mocker.patch(
        "Holiday.holiday.Holiday._Holiday__get_today",
        return_value=date(ANY_YEAR, month, day),
    )
