import pandas

from factories import *
import sys


class EventEnum(enum.Enum):
    CHRISTMAS = 0,
    HALLOWEEN = 1,
    EASTER = 2


class InvalidDataError(Exception):
    def __init__(self, value, expected):
        super().__init__()
        self.value = value
        self.expected = expected


class Order:
    def __init__(self, order_number: str, product_id: str, item: str,
                 name: str, factory: ItemFactory, quantity: int,
                 **item_details: dict) -> None:
        try:
            self.product_id = product_id
            self.order_number = order_number
            self.quantity = quantity
            self.name = name
            self.item = item
            self.item_details = item_details
            self.validate_data(order_number=order_number,
                               product_id=product_id, item=item,
                               name=name, quantity=quantity,
                               **item_details)
            del item_details['holiday']
            item_details['name'] = name
            item_details['product_id'] = product_id
            self.factory = factory
            self.is_valid = True
        except InvalidDataError as e:
            self.is_valid = False
            self.error_msg = f'Order error expected: {e.expected} got' \
                             f' {e.value}'

    @staticmethod
    def validate_data(**kwargs) -> bool:
        if kwargs['item'] == 'Toy':
            if kwargs['holiday'] == 'Christmas':
                if kwargs['has_batteries']:
                    raise InvalidDataError(kwargs['has_batteries'], False)
            elif kwargs['holiday'] == 'Halloween':
                if not kwargs['has_batteries']:
                    raise InvalidDataError(kwargs['has_batteries'], False)
                elif kwargs['spider_type'] is not 'Tarantula' or 'Wolf Spider':
                    raise InvalidDataError(kwargs['spider_type'], False)
            elif kwargs['holiday'] == 'Easter':
                if not kwargs['has_batteries']:
                    raise InvalidDataError(kwargs['has_batteries'], False)
                elif kwargs['colour'] is not 'Orange' or 'Pink' or 'Blue':
                    raise InvalidDataError(kwargs['colour'], False)
        elif kwargs['item'] == 'Stuffed Animals':
            if kwargs['holiday'] == 'Halloween':
                if not kwargs['has_glow']:
                    raise InvalidDataError(kwargs['has_glow'], False)
                elif not kwargs['fabric'] == 'Acrylic':
                    raise InvalidDataError(kwargs['fabric'], False)
                elif not kwargs['stuffing'] == 'Polyester Fiberfill' or \
                        'Polyester Fibrefill':
                    raise InvalidDataError(kwargs['stuffing'], False)
                elif kwargs['size'] is not 'S' or 'M' or 'L':
                    raise InvalidDataError(kwargs['size'], False)
            elif kwargs['holiday'] == 'Christmas':
                if not kwargs['has_glow']:
                    raise InvalidDataError(kwargs['has_glow'], False)
                elif not kwargs['fabric'] == 'Cotton':
                    raise InvalidDataError(kwargs['fabric'], False)
                elif not kwargs['stuffing'] == 'Wool':
                    raise InvalidDataError(kwargs['stuffing'], False)
                elif kwargs['size'] is not 'S' or 'M' or 'L':
                    raise InvalidDataError(kwargs['size'], False)
            elif kwargs['holiday'] == 'Easter':
                if not kwargs['fabric'] == 'Linen':
                    raise InvalidDataError(kwargs['fabric'], False)
                elif not kwargs['stuffing'] == 'Polyester Fiberfill' or \
                        'Polyester Fibrefill':
                    raise InvalidDataError(kwargs['stuffing'], False)
                elif kwargs['colour'] is not 'White' or 'Grey' or 'Pink' \
                        or 'Blue':
                    raise InvalidDataError(kwargs['colour'], False)
                elif kwargs['size'] is not 'S' or 'M' or 'L':
                    raise InvalidDataError(kwargs['size'], False)
        elif kwargs['item'] == 'Candy':
            if kwargs['holiday'] == 'Halloween':
                if not kwargs['has_lactose']:
                    raise InvalidDataError(kwargs['has_lactose'], False)
                elif not kwargs['has_nuts']:
                    raise InvalidDataError(kwargs['has_nuts'], False)
                elif kwargs['variety'] is not 'Sea Salt' or 'Regular':
                    raise InvalidDataError(kwargs['variety'], False)
            elif kwargs['holiday'] == 'Christmas':
                if kwargs['has_lactose']:
                    raise InvalidDataError(kwargs['has_lactose'], False)
                elif kwargs['has_nuts']:
                    raise InvalidDataError(kwargs['has_nuts'], False)
                elif kwargs['colour'] is not 'Green' or 'Red':
                    raise InvalidDataError(kwargs['colour'], False)
            elif kwargs['holiday'] == 'Easter':
                if not kwargs['has_lactose']:
                    raise InvalidDataError(kwargs['has_lactose'], False)
                elif not kwargs['has_nuts']:
                    raise InvalidDataError(kwargs['has_nuts'], False)
                elif not kwargs['pack_size']:
                    raise InvalidDataError(kwargs['pack_size'], False)
        return True

    def __str__(self):
        if self.is_valid:
            return f'Order {self.order_number}, Item {self.item}, Product ID ' \
                   f'{self.product_id}, Name "{self.name}", Quantity {self.quantity}'
        else:
            return self.error_msg


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
