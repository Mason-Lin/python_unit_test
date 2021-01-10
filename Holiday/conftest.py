import pytest
from Holiday.holiday import Holiday
from datetime import date


@pytest.fixture()
def holiday():
    return Holiday()


@pytest.fixture()
def fake_today(mocker, request):
    ANY_YEAR = 2019
    month, day = request.param
    mocker.patch(
        "Holiday.holiday.Holiday._Holiday__get_today",
        return_value=date(ANY_YEAR, month, day),
    )
