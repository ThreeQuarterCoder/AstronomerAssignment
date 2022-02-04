import os
import Offer
import Order
import Widget
import OfferLoader
import WidgetLoader

class DriverProgram:

    def __init__(self):
        offerloader = OfferLoader()
        offerloader.load()
        self.offers = offerloader.getOfferObjects()

        widgetloader = WidgetLoader()
        widgetloader.load()
        self.widgets = widgetloader.getWidgetObjects()

    def printMenu(self):
        print("----------")
        print("Enter 1 for new order")
        print("Enter 2 to exit")
        print("----------")

    def printWidgets(self):
        print("----------")
        print("List of all widgets available")
        for widget in self.widgets:
            print(widget.getName())

        print("Enter Quantity for each one")


    def main(self):

        while True:
            self.printMenu()
            choice = int(input())
            if choice == 1:
                self.printWidgets()
                widgetNumbers = []
                for index in range(len(self.widgets)):
                    num = int(input())
                    widgetNumbers.append(num)

                order = Order()
                order.setWidgetObjects(self.widgets)
                order.setWidgets(widgetNumbers)
                order.setOffers(self.offers)
                order.computePrice()
                print("Total Price to pay")
                print(order.getPrice())

            else:
                break
