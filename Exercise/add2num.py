class Add2Number:
    """Need two numbers when initializing"""

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        s = num1 + num2
        print(str(num1) +
              " + " +
              str(num2) +
              " = " +
              str(s))


p2 = Add2Number(6, 9)  # Example with 6 and 9
