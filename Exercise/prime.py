import math


class Prime:
    """Required one number as param to check"""

    def __init__(self, num=11.0):
        self.num = float(num)
        if self.num < 2:
            print(self.num, " is not prime number")
        else:
            if self.num % 2 == 0:
                if self.num == 2:
                    print("2 is prime number")
                else:
                    print(self.num, "is not prime number")
            else:
                limit = int(math.sqrt(self.num)) + 1
                flag = True

                for i in range(2, limit):
                    if self.num % i == 0:
                        flag = False
                        break

                if flag is False:
                    print(self.num, "is not prime number")
                else:
                    print(self.num, "is prime number")


p14a = Prime(-17.8)
p14b = Prime(0)
p14c = Prime(2)
p14d = Prime(8)
p14e = Prime(19)


