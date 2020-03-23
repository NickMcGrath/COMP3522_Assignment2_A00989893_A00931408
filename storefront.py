"""
The storefront module is responsible for receiving and maintaining its
inventory, getting items from a factory class if the store doesn't have
enough stock, and generating the daily transaction report.
"""
from order_processor import *


class Store:
    """
    A Store is responsible for receiving, maintaining, and retrieving
    order items and generating the daily transaction report.
    """

    def __init__(self, item_list=None):
        """
        Store is initialized with empty inventory.
        :param item_list: a sequence of Order objects.
        """
        if item_list:
            self.item_dic = item_list
        else:
            self.item_dic = {}  # product_id, [items?]
        self.orders = []

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
            try:
                user_input = int(input("> "))
            except ValueError:
                print('Enter an INT!')
                continue

            if user_input == 1:
                pass

            elif user_input == 2:
                pass

            elif user_input == 3:
                pass

            else:
                print("Invalid option.")
        print("Come again!")

    def process_orders(self, file_name):
        # for storefront class
        op = OrderProcessor()  # this class could just be static or have
        # static process method, no reason to instantiate
        for an_order in op.process_data('orders.xlsx'):
            try:
                self.orders.append(an_order)
                if an_order.item.lower() == 'candy':
                    item = an_order.factory.create_candy(
                        **an_order.item_details)
                elif an_order.item.lower() == 'stuffedanimal':
                    item = an_order.factory.create_stuffed_animal(
                        **an_order.item_details)
                elif an_order.item.lower() == 'toy':
                    item = an_order.factory.create_toy(**an_order.item_details)

                product_id = an_order.product_id
                if product_id in self.item_dic:
                    if self.item_dic[product_id] >= an_order.quantity:
                        self.item_dic[product_id] -= an_order.quantity
                    else:
                        self.item_dic[product_id] += 100
                        self.item_dic[product_id] -= an_order.quantity
                else:
                    self.item_dic[product_id] = 100
            except TypeError as e:
                print('Invalid parameters!' + str(e),
                      file=sys.stderr)
                print('at: ' + str(an_order), file=sys.stderr)


def main():
    store = Store()
    store.process_orders('orders.xlsx')
    for an_order in store.orders:
        print(an_order)
    # for v in store.item_dic.values():
    #     print(v)
    store.user_menu()


if __name__ == '__main__':
    main()
