"""
The storefront module is responsible for receiving and maintaining its
inventory, getting items from a factory class if the store doesn't have
enough stock, and generating the daily transaction report.
"""

class Store:
    """
    A Store is responsible for receiving, maintaining, and retrieving
    order items and generating the daily transaction report.
    """

    def __init__(self, item_list = None):
        """
        Store is initialized with empty inventory.
        :param item_list: a sequence of Order objects.
        """
        if not item_list:
            self.item_list = []
        else:
            self.item_list = item_list

    def user_menu(self):
        """
        The interactive menu for the user. The user can process web
        orders, check the inventory, or exit the program and print out
        the daily transaction report.
        """
        print("\nWelcome to the Toy Store!")
        user_input = None
        while user_input != 3:
            print("\nSelect from the following:")
            print("1. Process Web Orders")
            print("2. Check the Inventory")
            print("3. Exit and Print the Daily Transaction Report")
            user_input = int(input("> "))

            if user_input == 1:
                pass

            elif user_input == 2:
                pass

            elif user_input == 3:
                pass

            else:
                print("Invalid option.")
        print("Come again!")

def main():
    store = Store()
    store.user_menu()

if __name__ == '__main__':
    main()