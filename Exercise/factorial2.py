def fact(n):
    if n == 1:
        return n
    else:
        return n * fact(n - 1)


class Fact2:
    """Required one param when initializing"""

    def __init__(self, num=0):
        self.num = int(num)
        if self.num < 0:
            print("Impossible")
        elif self.num == 0:
            print("0! = 1")
        else:
            print("%d! = %d" % (self.num, (fact(self.num))))


p30a = Fact2(15)
p30b = Fact2(0)