"""
Xmas, no multi language support
Xmas is only 12/25, using local time of server
new requirement: 12/24 is also Xmas
"""

from datetime import date


class Holiday:
    def say_hello(self):
        today = self.__get_today()
        if today.month == 12 and today.day in [25, 24]:
            return "Merry Xmas"
        else:
            return "Today is not Xmas"

    def __get_today(self):
        today = date.today()
        return today
