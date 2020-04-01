import math


class Fact:
    """Required one param when initializing"""

    def __init__(self, num=6.0):
        self.num = int(num)
        if self.num < 0:
            print("Impossible!")
        else:
            fact = math.factorial(self.num)
            print("%d! is %d" % (self.num, fact))


p18a = Fact(-7.9)
p18b = Fact(0)
