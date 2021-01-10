import pytest
from Holiday.holiday import say_hello

def test_today_is_xmax():
    assert say_hello() == "Merry Xmax"
