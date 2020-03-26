"""
The factories module contains all of the factories for creating sets of
like items based on the event.
"""
from items import *


class ItemFactory(abc.ABC):
    """
    The base item factory class.
    """

    @abc.abstractmethod
    def create_toy(self, **kwargs) -> Toy:
        """Factory method to create a toy"""
        pass

    @abc.abstractmethod
    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        """Factory method to create a stuffed animal"""
        pass

    @abc.abstractmethod
    def create_candy(self, **kwargs) -> Candy:
        """Factory method to create a candy"""
        pass


class ChristmasFactory(ItemFactory):
    """
    This factory class implements the ItemFactory interface. It returns a
    product family consisting of christmas items.
    """

    def create_toy(self, **kwargs) -> Toy:
        """Factory method to create a toy"""
        return SantasWorkShop(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        """Factory method to create a stuffed animal"""
        return Reindeer(**kwargs)

    def create_candy(self, **kwargs):
        """Factory method to create a candy"""
        return CandyCanes(**kwargs)


class HalloweenFactory(ItemFactory):
    """
    This factory class implements the ItemFactory interface. It returns a
    product family consisting of halloween items.
    """

    def create_toy(self, **kwargs) -> Toy:
        """Factory method to create a toy"""
        return RCSpider(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        """Factory method to create a stuffed animal"""
        return DancingSkeleton(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """Factory method to create a candy"""
        return PumpkinCaramelToffee(**kwargs)


class EasterFactory(ItemFactory):
    """
    This factory class implements the ItemFactory interface. It returns a
    product family consisting of easter items.
    """

    def create_toy(self, **kwargs) -> Toy:
        """Factory method to create a toy"""
        return RobotBunny(**kwargs)

    def create_stuffed_animal(self, **kwargs) -> StuffedAnimal:
        """Factory method to create a stuffed animal"""
        return EasterBunny(**kwargs)

    def create_candy(self, **kwargs) -> Candy:
        """Factory method to create a candy"""
        return CremeEggs(**kwargs)
