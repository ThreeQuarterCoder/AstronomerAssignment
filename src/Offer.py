
class Offer:

    def __init__(self):
        self.preconds = []
        self.discounts = []

    def setPreconds(self, preconds):
        self.preconds = preconds

    def setDiscounts(self, discounts):
        self.discounts = discounts

    def getPreconds(self):
        return self.preconds

    def getDiscounts(self):
        return self.discounts

    def evaluate(self, order):
        results = []
        minfac = 0
        for index in range(len(self.preconds)):
            if order[index] >= self.preconds[index]:
                fac = order[index]//self.preconds[index]
                if fac > 0:
                    if minfac == 0 or (minfac > 0 and fac < minfac):
                        minfac = fac

        results = [element * minfac for element in self.discounts]
        return results

