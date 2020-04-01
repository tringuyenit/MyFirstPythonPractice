class Ams:
    """Required one para when initializing"""

    def __init__(self, num=153):
        self.num = int(num)
        if self.num < 0:
            print(self.num, "is not an Armstrong number")
        else:
            digit = []
            tmp = self.num
            count = 1
            s = 0
            while tmp != (tmp % 10):
                count += 1
                digit.append(tmp % 10)
                tmp = int(tmp / 10)
            digit.append(tmp % 10)
            for i in digit:
                s += i ** count
            if s == self.num:
                print(self.num, "is an Armstrong number")
            else:
                print(self.num, "is not an Armstrong number")


p21a = Ams(153)
p21b = Ams(663)
p21c = Ams(407)
