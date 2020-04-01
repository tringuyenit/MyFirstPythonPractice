class MaxNum:
    """Required no params when running"""

    def __init__(self):
        self.list = []
        print("Input 3 number :")
        for i in range(3):
            self.list.append(float(input()))
        self.list.sort()
        print("The maximum number among those numbers is : ", self.list[-1])


p13 = MaxNum()
