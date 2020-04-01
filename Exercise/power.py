class Pow:
    """I hate lambda so I coded this program briefly"""

    def __init__(self, num):
        self.num = float(num)
        count = 1
        for i in list(map(lambda x: x * self.num, range(10))):
            print(self.num, "^", count, "=", i)
            count += 1


p22 = Pow(4)
