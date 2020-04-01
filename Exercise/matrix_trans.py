class MatrixTrans:
    """I'm too lazy to give the program the \'custom\' feature to edit the input matrices"""

    def __init__(self):
        a = [[12, 7],
             [4, 5],
             [3, 8]]

        trans = [[0, 0, 0],
                 [0, 0, 0]]

        for i in range(len(a)):
            for j in range(len(a[0])):
                trans[j][i] = a[i][j]

        print("A =")
        for r in a:
            print(r)
        print("\n")
        print("Aᵀ =")
        for r in trans:
            print(r)


p36 = MatrixTrans()
print(p36.__doc__)
