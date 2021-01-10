import pytest


@pytest.mark.parametrize(
    "fake_today, expected",
    [
        ((12, 25), "Merry Xmas"),
        ((12, 24), "Merry Xmas"),
        ((11, 25), "Today is not Xmas"),
    ],
    indirect=["fake_today"],
)
def test_say_hello(holiday, fake_today, expected):
    assert expected == holiday.say_hello()
