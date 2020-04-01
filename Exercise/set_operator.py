class SetOp:
    """This sample program is too beautiful that I cannot comment anything"""

    def __init__(self):
        a = {0, 2, 4, 6, 8}
        b = {1, 2, 3, 4, 5}

        print("Given two sets : ")
        print("A =", a)
        print("B =", b)
        print("We have :")
        print("A ⋃ B =", a | b)
        print("A ⋂ B =", a & b)
        print("A/B =", a - b)
        print("(A/B) ⋃ (B/A) =", a ^ b)


p34 = SetOp()
