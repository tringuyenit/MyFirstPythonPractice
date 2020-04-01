class MulTable:
    """Required one param when initializing"""

    def __init__(self, num=1.0):
        self.num = float(num)
        for i in range(1, 11):
            print(self.num, "x", i, "=", i*self.num)


p19 = MulTable(13)