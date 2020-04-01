class Fib:
    """Required one param when initializing"""

    def __init__(self, num=5):  # 'num' is how many Fib number required
        self.count = int(num)
        if self.count <= 0:
            print("Bye")
        else:
            n1 = 0
            n2 = 1
            if self.count == 1:
                print("1\t0")
            elif self.count == 2:
                print("1\t0\n2\t1")
            else:
                i = 0
                limit = self.count - 2
                print("1\t0\n2\t1")
                while i < limit:
                    tmp = n1 + n2
                    print("%d\t%d" % (i + 3, tmp))
                    n1 = n2
                    n2 = tmp
                    i = i + 1


p20 = Fib(30)
