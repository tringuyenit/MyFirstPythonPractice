def solve(num1, num2):
    found = 1
    if num1 % num2 == 0:
        print("GCD is", num2)
    else:
        for i in range(2, int(num2 / 2)):
            if num2 % i == 0 and num1 % i == 0:
                found = i
        print("GCD is", found)

    print("LCM is", int(num1 * (num2 / found)), "\n----------")


class Common:
    """No need any params. I invented this method of solving GCD and LCM so I'm not sure about the accuracy"""
    def __init__(self):
        self.a = int(input("Input first number : "))
        self.b = int(input("Input second number : "))

        if self.a > self.b:
            solve(self.a, self.b)
        else:
            solve(self.b, self.a)


p25 = Common()
