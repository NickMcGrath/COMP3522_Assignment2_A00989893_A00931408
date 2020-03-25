import pandas

from factories import *
import sys


class EventEnum(enum.Enum):
    CHRISTMAS = 0,
    HALLOWEEN = 1,
    EASTER = 2


class InvalidDataError(Exception):
    def __init__(self, param, value, expected):
        super().__init__()
        self.param = param
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
            self.error_msg = f'Order {order_number}, Could not process ' \
                             f'order data was corrupted, ' \
                             f'InvalidDataError - ' \
                             f'{e.param} can only be {e.expected} ' \
                             f'received' \
                             f' "{e.value}"'

    @staticmethod
    def validate_data(**kwargs) -> None:
        if kwargs['item'] == 'Toy':
            if kwargs['holiday'] == 'Christmas':
                if kwargs['has_batteries']:
                    raise InvalidDataError('has_batteries', kwargs[
                        'has_batteries'], '"N"')
            elif kwargs['holiday'] == 'Halloween':
                if not kwargs['has_batteries']:
                    raise InvalidDataError('has_batteries', kwargs[
                        'has_batteries'], '"N"')
                elif kwargs['spider_type'] not in ['Tarantula', 'Wolf Spider']:
                    raise InvalidDataError('spider_type',
                                           kwargs['spider_type'],
                                           '"Tarantula" or "Wolf Spider"')
            elif kwargs['holiday'] == 'Easter':
                if not kwargs['has_batteries']:
                    raise InvalidDataError('has_batteries',
                                           kwargs['has_batteries'], '"N"')
                elif kwargs['colour'] not in ['Orange', 'Pink', 'Blue']:
                    raise InvalidDataError('colour', kwargs['colour'],
                                           '"Orange", "Pink", "Blue"')
        elif kwargs['item'] == 'Stuffed Animals':
            if kwargs['holiday'] == 'Halloween':
                if not kwargs['has_glow']:
                    raise InvalidDataError('has_glow', kwargs['has_glow'],
                                           '"Y"')
                elif not kwargs['fabric'] == 'Acrylic':
                    raise InvalidDataError('fabric', kwargs['fabric'],
                                           '"Acrylic"')
                elif kwargs['stuffing'] not in 'Polyester Fiberfill':
                    raise InvalidDataError('stuffing', kwargs['stuffing'],
                                           '"Polyester Fiberfill"')
                elif kwargs['size'] not in ['S', 'M', 'L']:
                    raise InvalidDataError('size', kwargs['size'], '"S" or '
                                                                   '"M" or '
                                                                   '"L"')
            elif kwargs['holiday'] == 'Christmas':
                if not kwargs['has_glow']:
                    raise InvalidDataError('has_glow', kwargs['has_glow'],
                                           '"Y"')
                elif not kwargs['fabric'] == 'Cotton':
                    raise InvalidDataError('fabric', kwargs['fabric'],
                                           '"Cotton"')
                elif not kwargs['stuffing'] == 'Wool':
                    raise InvalidDataError('stuffing', kwargs['stuffing'],
                                           '"Wool"')
                elif kwargs['size'] not in ['S', 'M', 'L']:
                    raise InvalidDataError('size', kwargs['size'], '"S" or '
                                                                   '"M" or '
                                                                   '"L"')
            elif kwargs['holiday'] == 'Easter':
                if not kwargs['fabric'] == 'Linen':
                    raise InvalidDataError('fabric', kwargs['fabric'],
                                           '"Linen"')
                elif not kwargs['stuffing'] == 'Polyester Fiberfill':
                    raise InvalidDataError('stuffing', kwargs['stuffing'],
                                           '"Polyester Fiberfill"')
                elif kwargs['colour'] not in ['White', 'Grey', 'Pink', 'Blue']:
                    raise InvalidDataError('colour', kwargs['colour'],
                                           '"White" or "Grey" or "Pink" or '
                                           'Blue')
                elif kwargs['size'] not in ['S', 'M', 'L']:
                    raise InvalidDataError('size', kwargs['size'], '"S" or '
                                                                   '"M" or '
                                                                   '"L"')
        elif kwargs['item'] == 'Candy':
            if kwargs['holiday'] == 'Halloween':
                if not kwargs['has_lactose']:
                    raise InvalidDataError('has_lactose', kwargs[
                        'has_lactose'], '"T"')
                elif not kwargs['has_nuts']:
                    raise InvalidDataError('has_nuts', kwargs['has_nuts'],
                                           '"T"')
                elif kwargs['variety'] not in ['Sea Salt', 'Regular']:
                    raise InvalidDataError('variety', kwargs['variety'],
                                           '"Sea Salt" or "Regular"')
            elif kwargs['holiday'] == 'Christmas':
                if kwargs['has_lactose']:
                    raise InvalidDataError('has_lactose', kwargs[
                        'has_lactose'], '"N"')
                elif kwargs['has_nuts']:
                    raise InvalidDataError('has_nuts', kwargs['has_nuts'],
                                           '"N"')
                elif kwargs['colour'] not in ['Green', 'Red']:
                    raise InvalidDataError('colour', kwargs['colour'],
                                           '"Green" or "Red"')
            elif kwargs['holiday'] == 'Easter':
                if not kwargs['has_lactose']:
                    raise InvalidDataError('has_lactose', kwargs[
                        'has_lactose'], '"Y"')
                elif not kwargs['has_nuts']:
                    raise InvalidDataError('has_nuts', kwargs['has_nuts'],
                                           '"Y"')
                elif not kwargs['pack_size']:
                    raise InvalidDataError('pack_size', kwargs['pack_size'],
                                           "'Y'")
        return True

    def __str__(self):
        if self.is_valid:
            return f'Order {self.order_number}, Item {self.item}, Product ID ' \
                   f'{self.product_id}, Name "{self.name}", Quantity ' \
                   f'{self.quantity}'
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
