import itertools
import random


class Shuffle:
    """Required no params when initializing"""

    value = ('A', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'J', 'Q', 'K')
    suit = ('Heart', 'Spade', 'Club', 'Diamond')
    deck = list(itertools.product(value, suit))

    def __init__(self):
        random.shuffle(self.deck)
        print("Your 5 random cards")
        for i in range(5):
            print(self.deck[i][0], "of", self.deck[i][1])


p26 = Shuffle()
