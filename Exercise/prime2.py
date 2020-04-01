import math


class Prime2:
    """Required no params when initiating"""

    def __init__(self):
        print("Input interval [a, b] :")
        self.a = int(input("a = "))
        self.b = int(input("b = ")) + 1
        for num in range(self.a, self.b):
            if num < 2:
                pass
            else:
                if num % 2 == 0:
                    if num == 2:
                        print(num)
                else:
                    limit = int(math.sqrt(num)) + 1
                    flag = True

                    for i in range(2, limit):
                        if num % i == 0:
                            flag = False
                            break

                    if flag is True:
                        print(num)


p15 = Prime2()
