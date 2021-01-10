import pytest

from Holiday.holiday import Holiday


@pytest.mark.parametrize(
    "fake_today, expected",
    [
        ((12, 25), "Merry Xmas"),
        ((12, 24), "Merry Xmas"),
        ((11, 25), "Today is not Xmas"),
    ],
    indirect=["fake_today"],
)
def test_say_hello(mocker, fake_today, expected):
    given_today(mocker, fake_today)
    holiday = Holiday()
    assert expected == holiday.say_hello()


def given_today(mocker, fake_today):
    mocker.patch(
        "Holiday.holiday.Holiday._Holiday__get_today",
        return_value=fake_today,
    )
