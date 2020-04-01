class ASS:
    """Required one param to covert"""

    def __init__(self, in_put):
        if type(in_put) is str:
            if len(in_put) == 1:
                print("Value of \"%c\" in ASCII is %d" % (in_put, ord(in_put)))
            else:
                print("WTF")
        else:
            if type(in_put) is int:
                print("In ASCII,", in_put, "is", chr(in_put))
            else:
                print("WTF")


p25a = ASS('h')
p25b = ASS('hello')
p25c = ASS(120)
