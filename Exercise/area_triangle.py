import math


class Area:
    """ No need params when initializing """

    def __init__(self):
        print("Input 3 sides of a triangle : ")
        self.a = float(input())
        self.b = float(input())
        self.c = float(input())

    def area(self):
        test1 = self.a > 0 and self.b > 0
        test2 = 0 < self.c < self.a + self.b
        test3 = self.b + self.c > self.a
        test4 = self.a + self.c > self.b
        if test1 and test2 and test3 and test4:
            p = (self.a + self.b + self.c) / 2
            area = (math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c)))
            print("The area of the triangle is : " + str(area))
        else:
            print("Not a triangle!")


p4 = Area()
p4.area()
