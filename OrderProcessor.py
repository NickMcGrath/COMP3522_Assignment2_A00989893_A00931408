from factories import *


class EventEnum(enum.Enum):
    CHRISTMAS = 0,
    HALLOWEEN = 1,
    EASTER = 2


class Order:
    def __init__(self, order_num: str, product_id, item_type: str,
                 item_name: str, item_details: dict,
                 factory: ItemFactory) -> None:
        self.order_num = order_num
        self.product_id = product_id
        self.item_type = item_type
        self.item_name = item_name
        self.item_details = item_details
        self.factory = factory


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

    def __init__(self, path: str):
        self.path = path

    def get_factory(self, event: EventEnum) -> ItemFactory:
        """
        Retrieves the associated factory for the specified EventEnum
        :param event: EventEnum
        :return: a ItemFactory if found, None otherwise
        """
        return self.item_factory_mapper[event]()
