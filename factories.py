import abc
import enum

from items import *


class ItemFactory(abc.ABC):
    """
    The base item factory class.
    """

    @abc.abstractmethod
    def create_toy(self, **kwargs) -> Toy:
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        pass

    @abc.abstractmethod
    def create_candy(self, **kwargs) -> Candy:
        pass


class ChristmasFactory(ItemFactory):
    """
    This factory class implements the ItemFactory interface. It returns a
    product family consisting of christmas items.
    """
    def create_toy(self, **kwargs) -> Toy:
        return SantasWorkShop(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs):
        return CandyCanes(**kwargs)


class HalloweenFactory(ItemFactory):
    """
    This factory class implements the ItemFactory interface. It returns a
    product family consisting of halloween items.
    """
    def create_toy(self, **kwargs) -> Toy:
        return RCSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        return PumpkinCaramelToffee(**kwargs)


class EasterFactory(ItemFactory):
    """
    This factory class implements the ItemFactory interface. It returns a
    product family consisting of easter items.
    """
    def create_toy(self, **kwargs) -> Toy:
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        return CremeEggs(**kwargs)


class EventEnum(enum.Enum):
    CHRISTMAS = 0,
    HALLOWEEN = 1,
    EASTER = 2


class FactoryGrabber:
    """
    Mapper
    """
    # Maps world types to their respective factories
    item_factory_mapper = {
        EventEnum.CHRISTMAS: ChristmasFactory,
        EventEnum.HALLOWEEN: HalloweenFactory,
        EventEnum.EASTER: EasterFactory
    }
    def get_factory(self, event: EventEnum) -> ItemFactory:
        """
        Retrieves the associated factory for the specified EventEnum
        :param event: EventEnum
        :return: a ItemFactory if found, None otherwise
        """
        return self.item_factory_mapper[event]()
