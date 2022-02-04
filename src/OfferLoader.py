import os
import Offer


class WidgetLoader:

    def __init__(self):
        self.configfilepath = os.path.join(os.pardir, os.path("configs/offers.conf"))
        self.offerObjects = []

    def load(self):
        offerObjects = []
        filepointer = open(self.configfilepath, "r")

        while True:
            line = filepointer.readline()
            if not line:
                break
            line = line.strip()
            if not line:
                break
            line = line.split(',')

            preconds = []
            discounts = []
            for index in range(3):
                lin2 = filepointer.readline()
                lin2 = lin2.strip()
                lin2 = lin2.split(',')
                preconds.append(int(lin2[0]))
                discounts.append(int(lin2[1]))
                offer = Offer()
                offer.setPreconds(preconds)
                offer.setDiscounts(discounts)

            offerObjects.append(offer)


        filepointer.close()

        self.offerObjects = offerObjects

    def getOfferObjects(self):
        return self.offerObjects
