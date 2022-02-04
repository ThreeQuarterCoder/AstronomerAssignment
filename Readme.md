
Offer Management System

The details of the widgets are maintained in configs/widgets.conf and the details of offers are mentioned in configs/offers.conf

widgets.conf is a configuration file each widget details on a separate line with the format:
Widget Name, Widget Code, Widget Price 

offers.conf defines the discounts and the conditions
Each offer starts with a 1, A
Then each line is defined by 2 numbers separated by a comma
First number indicates the number of units in the precondition
Second number indicates the effective number to charge

Example an offer of "Buy 1 red widget, get 1 free" will be represented as:
2, 1.5 

indicating that at least 2 objects should be there for red widgets and then charge for 1.5

The calculation of price follows the same data format

The driver program is a menu-driven program to get orders and print the final price

The input to each order is a list of number of widgets of each type in the order


Improvements:

Instead of custom configuration formats, a simple Json or XML file would be better at defining configurations



