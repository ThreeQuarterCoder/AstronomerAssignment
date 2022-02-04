import DeliveryPolicy
class Order:

    def __init__(self):
        self.widgetObjects = []
        self.widgets = []
        self.offers = []
        self.price = 0
        self.deliverypolicy = DeliveryPolicy()

    def getWidgets(self):
        return self.widgets

    def getOffers(self):
        return self.offers

    def getDeliveryPolicy(self):
        return self.deliverypolicy

    def getWidgetObjects(self):
        return self.widgetObjects

    def getPrice(self):
        return self.price

    def setWidgets(self, widgets):
        self.widgets = widgets

    def setOffers(self, offers):
        self.offers = offers

    def setDeliveryPolicy(self, deliverypolicy):
        self.deliverypolicy = deliverypolicy

    def setWidgetObjects(self, widgetObjects):
        self.widgetObjects = widgetObjects

    def computePrice(self):
        discounts = []
        for offer in self.offers:
            discs = offer.evaluate(self.widgets)
            for index in range(len(discounts)):
                discounts[index] = discounts[index] + discs[index]

        for index in range(len(self.widgets)):
            self.widgets[index] = self.widgets[index] - discounts[index]

        price = 0
        for index in range(len(self.widgetObjects)):
            price = price + self.widgets[index] * self.widgetObjects[index].getPrice()

        price = price + self.deliverypolicy.getDeliveryCharge(price)

        self.price = price

