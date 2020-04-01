import calendar


class Date:
    """Awesome built-in function! Need no params"""
    def __init__(self):
        self.year = int(input("Enter year: "))
        self.month = int(input("Enter month : "))

        if self.year > 0 and 0 < self.month < 13:
            print(calendar.month(self.year, self.month))


p27 = Date()
