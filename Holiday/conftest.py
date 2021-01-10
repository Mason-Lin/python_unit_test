import pytest
from datetime import date


@pytest.fixture(scope="function")
def fake_today(request):
    ANY_YEAR = 2019
    month, day = request.param
    return date(ANY_YEAR, month, day)
