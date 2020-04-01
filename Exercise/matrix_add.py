class MatrixAd:
    """I'm too lazy to give the program the \'custom\' feature to edit the input matrices"""

    def __init__(self):

        a = [[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]]

        b = [[5, 8, 1],
             [6, 7, 3],
             [4, 5, 9]]

        s = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

        for i in range(len(a)):
            for j in range(len(b[0])):
                s[i][j] = a[i][j] + b[i][j]

        for r in a:
            print(r)
        print("\n     +     \n")
        for r in b:
            print(r)
        print("\n     =     \n")
        for r in s:
            print(r)


p32 = MatrixAd()
print(p32.__doc__)