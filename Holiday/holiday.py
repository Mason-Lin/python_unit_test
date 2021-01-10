from datetime import date


def say_hello():
    today = get_today()
    if today.month == 12 and today.day == 25:
        return "Merry Xmax"
    else:
        return "Today Is Not Xmax"


def get_today():
    today = date.today()
    return today
