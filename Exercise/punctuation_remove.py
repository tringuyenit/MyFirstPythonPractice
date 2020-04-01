class PuncDel:
    """Required one param wwhen initializing"""

    def __init__(self, line):
        self.line = str(line)
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        punct_del = ""

        for char in self.line:
            if char not in punctuations:
                punct_del += char

        print(punct_del)


p38 = PuncDel("Tri!!! Nguyen@#$% that la____() dep "":""trai")