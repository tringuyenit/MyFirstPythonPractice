class Vow:
    """Required one string as param when initializing"""

    def __init__(self, line):
        vowels = 'aeiou'
        self.line = str(line)

        line = line.casefold()

        count = {}.fromkeys(vowels, 0)

        for char in line:
            if char in count:
                count[char] += 1

        print("\"", self.line, "\"")
        print("Vowel  Frequency")
        for i in count:
            print(" ", i, "     ", count[i])


p35 = Vow("Tri that la dep trai")