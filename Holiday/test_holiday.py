import unittest
from datetime import date
from unittest.mock import patch

from Holiday.holiday import Holiday


class HolidayTests(unittest.TestCase):
    def test_today_is_xmas(self):
        self.given_today(12, 25)
        self.response_should_be("Merry Xmas")

    def test_today_is_xmas_when_12_24(self):
        self.given_today(12, 24)
        self.response_should_be("Merry Xmas")

    def test_today_is_not_xmas(self):
        self.given_today(11, 25)
        self.response_should_be("Today is not Xmas")

    def response_should_be(self, expected):
        self.assertEqual(expected, self.holiday.say_hello())

    def given_today(self, month, day):
        ANY_YEAR = 2019
        patch(
            "Holiday.holiday.Holiday._Holiday__get_today",
            return_value=date(ANY_YEAR, month, day),
        ).start()

    def setUp(self) -> None:
        self.holiday = Holiday()

    def tearDown(self) -> None:
        patch.stopall()


if __name__ == "__main__":
    unittest.main()
