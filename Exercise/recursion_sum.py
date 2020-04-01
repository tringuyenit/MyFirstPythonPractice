def resum(n):
    if n <= 1:
        return n
    else:
        return n + resum(n - 1)


class RecurSum:
    """Required one param when initializing"""

    def __init__(self, num):
        self.num = int(num)

        if self.num < 0:
            print("WTF")
        else:
            print("The sum from 1 to", self.num, "is", resum(self.num))


p37 = RecurSum(20)
