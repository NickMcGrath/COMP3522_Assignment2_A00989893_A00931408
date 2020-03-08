import abc


# todo check if init should have @abc.method about it
# todo consider making item super class because name, desc, and product_id
# appear in all superclasses
# todo kwargs may not actually be :dict because you can use tuples 🤔
class Toy(abc.ABC):
    """
    Abstract base class that represents properties that each toy has in
    common.
    """

    def __init__(self, name: str, description: str, product_id: str,
                 min_age: int, is_battery_operated: bool):
        """
        Initialize a toy with the parameter properties.
        :param name: str
        :param description: str
        :param product_id: str
        :param min_age: int
        :param is_battery_operated: bool
        """
        self.name = name
        self.description = description
        self.product_id = product_id
        self.min_age = min_age
        self.is_battery_operated = is_battery_operated


class SantasWorkShop(Toy):
    """
    A toy that is a premium Christmas present that comes in variety of
    dimensions and number of rooms.
    """

    def __init__(self, width: float, height: float, rooms_amt: int, **kwarg:
    dict):
        """
        Initialize a work shop with the dimensions, amount of rooms, 
        and properties of a Toy 
        :param width: float in cm
        :param height: float in cm
        :param rooms_amt: int
        :param kwarg: dict keyword arguments to create a Toy
        """
        kwarg['is_battery_operated'] = False
        self.width = width
        self.height = height
        self.room_amt = rooms_amt
        super().__init__(**kwarg)


# todo add other toys
class StuffedAnimal(abc.ABC):
    """
    Abstract base class that represents properties that each stuffed
    animal has in common.
    """

    def __init__(self, name: str, desc: str, product_id: str, stuffing: str,
                 size: str, fabric: str):
        """
        Initialize a stuffed animal with the parameter properties.
        :param name: str
        :param desc: str
        :param product_id: str
        :param stuffing: str Polyester, Fiberfill, or Wool
        :param size: str Small, Medium, or Large
        :param fabric: str Linen, Cotton, or Acrylic
        """
        self.name = name
        self.desc = desc
        self.product_id = product_id
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric


class Reindeer(StuffedAnimal):
    """
    A StuffedAnimal that is made out of cotton, stuffed with wool, and
    glows in the dark.
    """

    def __init__(self, **kwargs: dict):
        """
        Initialize a reindeer with
        :param kwargs: keyword arguments to create a StuffedAnimal
        """
        self.glows_in_dark = True
        kwargs['fabric'] = 'cotton'
        kwargs['stuffing'] = 'wool'
        super().__init__(**kwargs)


# todo add other scuffed animals (get it?)
class Candy(abc.ABC):
    """
    Abstract base class that represents properties that each candy has in
    common.
    """

    def __init__(self, name: str, desc: str, product_id: str, has_nuts: bool,
                 is_lactose_free: bool):
        """
        Initialize a candy with the parameter properties.
        :param name: str
        :param desc: str
        :param product_id: str
        :param has_nuts: bool
        :param is_lactose_free: bool
        """
        self.name = name
        self.desc = desc
        self.product_id = product_id
        self.has_nuts = has_nuts
        self.is_lactose_free = is_lactose_free


class CandyCanes(Candy):
    """
    A candy that is in the shape of a cane and hung from a tree.
    """

    def __init__(self, type: str, **kwargs: dict):
        """
        Initialize a candy cane with type and candy parameters.
        :param type: str red or green
        :param kwargs: dict keyword arguments to create a Candy
        """
        self.type = type
        kwargs['is_lactose_free'] = True
        kwargs['has_nuts'] = False
        super().__init__(**kwargs)

# todo add other candy
