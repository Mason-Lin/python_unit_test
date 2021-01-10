from datetime import date


class Holiday:
    def say_hello(self):
        today = self.__get_today()
        if today.month == 12 and today.day in [24, 25]:
            return "Merry Xmas"
        else:
            return "Today is not Xmas"

    @staticmethod
    def __get_today():
        return date.today()
