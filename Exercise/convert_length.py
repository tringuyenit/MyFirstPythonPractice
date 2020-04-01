class Convert:
    """Required 1 param to convert"""

    def __init__(self, km=1):
        self.km = float(km)
        mile = self.km * 0.621371
        print(self.km, " km = ", mile, " miles")


p8a = Convert()
p8b = Convert(12)