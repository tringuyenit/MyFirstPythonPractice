import random


class Div:
    """Required one param as test-divisor"""

    def __init__(self, num=4):
        self.num = float(num)
        if self.num == 0:
            print("Nooooooooooooooo!")
        else:
            arr1 = list(map(lambda x: random.randint(1, 1000), range(20)))
            print("This is your list of numbers")
            print(arr1)
            print("-------------")
            arr2 = list(filter(lambda x: x % self.num == 0, arr1))
            print("These are numbers divisible by", self.num)
            arr2.sort()
            print(arr2)


p23 = Div(-5)
