class Base:
    """This exercise is so lame"""

    def __init__(self, num=10):

        self.num = int(num)

        print(self.num)
        print(bin(self.num))
        print(oct(self.num))
        print(hex(self.num))
        print("--------")


p23a = Base(79)
p23b = Base(-79)
