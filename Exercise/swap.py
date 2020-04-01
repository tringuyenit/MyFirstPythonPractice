class Swap:
    """Required two params when initializing in order to perform the swap"""

    def __init__(self, num1, num2):
        self.x = num1
        self.y = num2
        print("x = ", self.x)
        print("y = ", self.y)
        print("Swap!")
        tmp = self.x
        self.x = self.y
        self.y = tmp
        print("x = ", self.x)
        print("y = ", self.y)


p6 = Swap(6, 9)  # Swap 6 and 9
