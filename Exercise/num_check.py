class NumCheck:
    """Required one param to check"""

    def __init__(self, num):
        self.num = float(num)
        if num > 0:
            print("Positive")
        elif num == 0:
            print("Zero")
        else:
            print("Negative")


p10 = NumCheck(-90)
