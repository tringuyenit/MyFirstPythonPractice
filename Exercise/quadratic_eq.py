import math


class QuadEx:
    """ No need params when initializing """

    def __init__(self):
        print("Input a, b and c for ax^2 + bx +c = 0 :")
        self.a = float(input())
        self.b = float(input())
        self.c = float(input())

    def solve(self):
        a = self.a
        b = self.b
        c = self.c
        delta = b ** 2 - 4 * a * c

        if delta > 0:
            print("First sol : ", (-b + math.sqrt(delta)) / (2 * a))
            print("Second sol : ", (-b - math.sqrt(delta)) / (2 * a))
        elif delta == 0:
            print("Sol :", (-b / (2 * a)))
        else:
            print("No solution")


p5 = QuadEx()
p5.solve()
