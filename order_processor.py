import pandas

from factories import *
import sys


class EventEnum(enum.Enum):
    CHRISTMAS = 0,
    HALLOWEEN = 1,
    EASTER = 2


class Order:
    def __init__(self, order_number: str, product_id: str, item: str,
                 name: str, factory: ItemFactory, quantity: int,
                 **item_details: dict) -> None:
        self.order_number = order_number
        self.product_id = product_id
        self.item = item
        self.name = name
        self.quantity = quantity
        item_details['name'] = name
        item_details['product_id'] = product_id
        del item_details['holiday']
        self.item_details = item_details
        self.factory = factory

    def __str__(self):
        return f'Order {self.order_number}, Item {self.item}, Product ID ' \
               f'{self.product_id}, Name "{self.name}", Quantity {self.quantity}'


class OrderProcessor:
    """
    Mapper
    """
    # Maps world types to their respective factories
    item_factory_mapper = {
        EventEnum.CHRISTMAS: ChristmasFactory,
        EventEnum.HALLOWEEN: HalloweenFactory,
        EventEnum.EASTER: EasterFactory
    }

    def __init__(self):
        pass

    def process_data(self, path: str) -> Order:
        df = pandas.read_excel(path)
        columns = df.columns.ravel()
        for k, row in df.iterrows():
            row = row.dropna().to_dict()
            try:
                item = row['item'].lower()
                if item == 'toy':
                    row['has_batteries'] = True if row['has_batteries'] == 'Y' \
                        else False
                    if 'dimensions' in row:
                        row['dimensions'] = row['dimensions'].split(',')
                    if 'num_rooms' in row:
                        row['num_rooms'] = int(row['num_rooms'])
                    if 'has_glow' in row:
                        row['has_glow'] = True if row['has_glow'] == 'Y' \
                            else False
                    row['min_age'] = int(row['min_age'])
                elif item == 'candy':
                    row['has_nuts'] = True if row['has_nuts'] == 'Y' else False
                    row['has_lactose'] = True if row['has_lactose'] == 'Y' \
                        else False
                elif item == 'stuffedanimal':
                    if 'has_glow' in row:
                        row['has_glow'] = True if row['has_glow'] == 'Y' \
                            else False
                row['factory'] = self.get_factory(row['holiday'])
            except KeyError as e:
                print('Invalid parameters!, missing: ' + str(e),
                      file=sys.stderr)
                print('at: ' + str(row), file=sys.stderr)
            else:
                yield Order(**row)

    def get_factory(self, event: str) -> ItemFactory:
        """
        Retrieves the associated factory for the specified EventEnum
        :param event: EventEnum
        :return: a ItemFactory if found, None otherwise
        """
        event = event.lower()
        if event == "halloween":
            return self.item_factory_mapper[EventEnum.HALLOWEEN]()
        elif event == "easter":
            return self.item_factory_mapper[EventEnum.EASTER]()
        elif event == "christmas":
            return self.item_factory_mapper[EventEnum.CHRISTMAS]()


# for testing
if __name__ == '__main__':
    o = OrderProcessor()
    for order in o.process_data('orders.xlsx'):
        print(order.__dict__)
