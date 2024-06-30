######################################
# DSC 510
# Week 11
# Programming Assignment Week 11
# Description: Asking for the user input of prices, creating a loop for
# additional user inputs
# Author: Kalyan Pothineni
# 11/07/2022
######################################
import locale

# Welcome Message to User
print("Welcome to the Personal Cash Register Program. Let's get started.")

class CashRegister:
    def __init__(self):
        self.total_price = 0
        self.item_count = 0

    def add_item(self, price):
        self.total_price = self.total_price + price
        self.item_count += 1

    def get_total(self):
        locale.setlocale(locale.LC_ALL, 'en_US.utf-8')
        return locale.currency(self.total_price, symbol=True)

    def get_count(self):
        return self.item_count

    def clear(self):
        self.total_price = 0
        self.item_count = 0
        print('\nGreat! Your previous cart has been deleted.'
              f'\nThere are currently {self.get_count()} items totalling '
              f'{self.get_total()} in your new cart.')
        main()

def main():
    """
        The main function asking for the user input of prices,
        creating a loop for additional user input, and
        making the calls to the CashRegister class
    """
    register = CashRegister()
    price = []
    while price != 'total':
        price = input("Please enter a price to be included or enter 'total' "
                      "to calculate your cart: ").strip().strip('$').lower()
        while True:
            if price == 'total':
                break
            # try and except block to catch input errors
            try:
                price = float(price)
                break
            except ValueError:
                price = input('\nYour last entry was not a valid selection.\n'
                              "Please enter a price or 'total' to continue: ")\
                    .strip().strip('$').lower()
        if price == 'total':
            print(f'\nThere are {register.get_count()} items in your cart '
                  f'totalling {register.get_total()}')
            option = str(input('Would you like to start a new cart, Yes or No?'
                               ' ')).lower().strip()
            # while loop to allow for a yes selection or to exit the program
            while not (option == 'yes' or option == 'no'):
                option = str(input('\nYour last entry was not a valid selection'
                                   '.\n'
                                   'Please enter Yes or No to continue: '))\
                    .lower().strip()
            if option == 'yes':
                register.clear()
            if option == 'no':
                print('Thank you for using the best Personal Cash Register '
                      'Program in the world .'
                      '')  # Exit Message To User
            break
        register.add_item(price)

if __name__ == "__main__":
    main()
