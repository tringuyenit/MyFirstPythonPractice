class LeapYear:
    """Required one number to check the year"""

    def __init__(self, num):
        self.year = float(num)
        if self.year < 0:
            print("WTF")
        else:
            if self.year % 4 == 0:
                if self.year % 100:
                    if self.year % 400:
                        print("Leap year")
                    else:
                        print("Not leap year")
                else:
                    print("Leap year")
            else:
                print("Not leap year")


p12 = LeapYear(2012)
