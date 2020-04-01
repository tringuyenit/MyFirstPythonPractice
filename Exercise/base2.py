def convert(n):
    if n > 1:
        convert(n // 2)
    print(n % 2, end='')  # Very nice technique to custom the ending of a line


class Base2:
    def __init__(self, num=100):
        self.num = int(num)
        convert(self.num)


p31 = Base2(169)
