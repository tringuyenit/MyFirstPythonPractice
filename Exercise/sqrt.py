import math


class Sqrt:
    """Required 1 number when initializing"""

    def __init__(self, num):
        self.num = num
        print("The square root of " + str(num) + " is " + str(math.sqrt(num)))


p3 = Sqrt(64)  # Example with 64
