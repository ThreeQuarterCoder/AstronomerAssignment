
class DeliveryPolicy:

    def getDeliveryCharge(self, price):
        if price < 50:
            return 4.95
        elif price > 50 and price < 90:
            return 2.95
        else:
            return 0

