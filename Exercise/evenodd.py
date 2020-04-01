class EvenOdd:
    """Required 1 param to check"""

    def __init__(self, num):
        self.num = float(num)
        if self.num >= 0:
            if self.num % 2 == 0:
                print("Even")
            else:
                print("Odd")
        else:
            print("Negative! WTF??")


p11 = EvenOdd(44)
