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
        holiday = Holiday()
        self.assertEqual(expected, holiday.say_hello())

    def given_today(self, month, day):
        self.fake_get_today.return_value = date(2020, month, day)

    def setUp(self) -> None:
        get_today_patcher = patch('Holiday.holiday.Holiday._Holiday__get_today')
        self.fake_get_today = get_today_patcher.start()

    def tearDown(self) -> None:
        patch.stopall()


if __name__ == '__main__':
    unittest.main()