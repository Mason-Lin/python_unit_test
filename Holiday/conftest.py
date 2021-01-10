import pytest
from Holiday.holiday import Holiday


@pytest.fixture(scope="function")
def holiday():
    return Holiday()
