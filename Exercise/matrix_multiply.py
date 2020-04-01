class MatrixMul:
    """I'm too lazy to give the program the \'custom\' feature to edit the input matrices"""

    def __init__(self):
        a = [[12, 7, 3],
             [4, 5, 6],
             [7, 8, 9]]

        b = [[5, 8, 1, 2],
             [6, 7, 3, 0],
             [4, 5, 9, 1]]

        m = [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [0, 0, 0, 0]]

        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    m[i][j] += a[i][k] * b[k][j]

        for r in a:
            print(r)
        print("\n     *     \n")
        for r in b:
            print(r)
        print("\n     =     \n")
        for r in m:
            print(r)


p33 = MatrixMul()
print(p33.__doc__)