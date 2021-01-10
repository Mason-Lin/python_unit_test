import pytest


@pytest.mark.parametrize(
    "given_today, expected",
    [
        ((12, 25), "Merry Xmas"),
        ((12, 24), "Merry Xmas"),
        ((11, 25), "Today is not Xmas"),
    ],
    indirect=["given_today"],
)
def test_say_hello(holiday, given_today, expected):
    assert expected == holiday.say_hello()
