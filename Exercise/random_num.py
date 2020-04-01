import random


class Random:
    """
    Required 3 params when initializing
    Default set to 10 random numbers from 0 to 10
    """

    def __init__(self, start=0, to=10, time=10):
        self.start = start
        self.to = to
        self.time = time
        for i in range(self.time):
            print(random.randint(self.start, self.to))
        print("****")


p7a = Random()  # Default
p7b = Random(5, 15, 6)  # Custom
