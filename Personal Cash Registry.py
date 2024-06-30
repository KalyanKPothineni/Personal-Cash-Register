######################################
# DSC 510
# Week 11
# Programming Assignment Week 11
# Description: Cash Register Program
# Author: Kalyan Pothineni
# 05/22/2023
######################################
import locale

class CashRegister:
    def __init__(self):
        self.totalPrice = 0.0
        self.itemCount = 0

    def addItem(self, price):
        self.totalPrice = self.totalPrice + price
        self.itemCount = self.itemCount + 1

    def getTotal(self):
        return self.totalPrice

    def getCount(self):
        return self.itemCount

def main():
    # Setting the locale for currency formatting
    locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

    # Creating an instance of the CashRegister class
    register = CashRegister()

    # Welcome message
    print("Welcome to your own Cash Register Program!\n")

    # Loop to allow the user to add items to the cart
    while True:
        # Prompting the user to enter the price of the item
        price_input = input("Enter the price of the item (or 'q' to quit "
                            "and calculate the total): ")

        # Checking if the user wants to quit
        if price_input.lower() == 'q':
            break

        try:
            # Attempt to convert the input to a float
            price = float(price_input)
            # Adding the item to the cart
            register.addItem(price)
        except ValueError:
            # Handle the case when the input is not a float
            print("Invalid input. Please enter a valid price.")

    # Printing the total number of items in the cart
    print("Total items in the cart:", register.getCount())

    # Printing the total $ amount of the cart in currency format
    print("Total amount of the cart:", locale.currency(register.getTotal()))

if __name__ == '__main__':
    main()
