from datetime import date


class Holiday:
    def say_hello(self):
        today = self.__get_today()
        if today.month == 12 and today.day in [24, 25]:
            return "Merry Xmax"
        else:
            return "Today Is Not Xmax"

    def __get_today(self):
        today = date.today()
        return today
