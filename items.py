import abc


class InvalidDataError(Exception):
    def __init__(self, value, expected):
        super().__init__()
        self.value = value
        self.expected = expected


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
                 min_age: int, has_batteries: bool):
        """
        Initialize a toy with the parameter properties.
        :param name: str
        :param description: str
        :param product_id: str
        :param min_age: int
        :param has_batteries: bool
        """
        self.name = name
        self.description = description
        self.product_id = product_id
        self.min_age = min_age
        self.has_batteries = has_batteries

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class SantasWorkShop(Toy):
    """
    A toy that is a premium Christmas present that comes in variety of
    dimensions and number of rooms.
    """

    def __init__(self, dimensions: list, num_rooms: int, **kwarg:
    dict):
        """
        Initialize a work shop with the dimensions, amount of rooms, 
        and properties of a Toy 
        :param width: float in cm
        :param height: float in cm
        :param rooms_amt: int
        :param kwarg: dict keyword arguments to create a Toy
        """
        if kwarg['has_batteries'] != False:
                                  #expected, value received (for the raise)
            raise InvalidDataError(False, kwarg['has_batteries'])
        #kwarg['has_batteries'] = False  # old value is kwarg and is good
        self.dimensions = dimensions
        self.num_rooms = num_rooms
        super().__init__(**kwarg)


class RCSpider(Toy):
    """
    The remote controlled spider is the toy to get during Halloween.
    """

    def __init__(self, speed: int, jump_height: int, has_glow: bool,
                 spider_type: str, **kwargs):
        if kwargs['has_batteries'] != True:
            raise InvalidDataError(True, has_glow)
        self.speed = speed
        self.jump_height = jump_height
        self.has_glow = has_glow
        self.type = spider_type
        super().__init__(**kwargs)


class RobotBunny(Toy):
    """

    """

    def __init__(self, num_sound: int, colour: list, **kwargs):
        super().__init__(**kwargs)
        self.num_sound = num_sound
        self.colour = ['Pink', 'Yellow', 'Blue']


class StuffedAnimal(abc.ABC):
    """
    Abstract base class that represents properties that each stuffed
    animal has in common.
    """

    def __init__(self, name: str, description: str, product_id: str,
                 stuffing: str,
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
        self.description = description
        self.product_id = product_id
        self.stuffing = stuffing
        self.size = size
        self.fabric = fabric

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class DancingSkeleton(StuffedAnimal):
    """

    """

    def __init__(self, has_glow: bool, **kwargs):
        super().__init__(**kwargs)  # todo note if you pass the kwargs here
        # the super will not get the values changed below
        kwargs['fabric'] = 'Acrylic'
        kwargs['stuffing'] = 'Polyester Fiberfill'
        self.has_glow = True


class Reindeer(StuffedAnimal):
    """
    A StuffedAnimal that is made out of cotton, stuffed with wool, and
    glows in the dark.
    """

    def __init__(self, has_glow: bool, **kwargs: dict):
        """
        Initialize a reindeer with
        :param kwargs: keyword arguments to create a StuffedAnimal
        """
        self.has_glow = True
        kwargs['fabric'] = 'cotton'
        kwargs['stuffing'] = 'wool'
        super().__init__(**kwargs)


class EasterBunny(StuffedAnimal):
    """

    """

    def __init__(self, colour, **kwargs):
        super().__init__(**kwargs)
        kwargs['fabric'] = 'Linen'
        kwargs['stuffing'] = 'Polyester Fiberfill'
        self.colour = ['Pink', 'Yellow', 'Blue']


# todo add other scuffed animals (get it?)...no
class Candy(abc.ABC):
    """
    Abstract base class that represents properties that each candy has in
    common.
    """

    def __init__(self, name: str, description: str, product_id: str,
                 has_nuts: bool,
                 has_lactose: bool):
        """
        Initialize a candy with the parameter properties.
        :param name: str
        :param desc: str
        :param product_id: str
        :param has_nuts: bool
        :param has_lactose: bool
        """
        self.name = name
        self.description = description
        self.product_id = product_id
        self.has_nuts = has_nuts
        self.has_lactose = has_lactose

    def __eq__(self, other):
        return self.__dict__ == other.__dict__


class PumpkinCaramelToffee(Candy):
    """
    If it doesn't have artificial pumpkin, you're doing fall wrong!
    Enjoy a Pumpkin Carmel Toffee with your Pumpkin Spiced Latte while
    trudging through a pumpkin patch. Do it for the 'gram!
    """

    def __init__(self, variety: str, **kwargs):
        super().__init__(**kwargs)
        self.type = variety
        kwargs['has_lactose'] = False
        kwargs['has_nuts'] = True


class CandyCanes(Candy):
    """
    A candy that is in the shape of a cane and hung from a tree.
    """

    def __init__(self, colour: str, **kwargs: dict):
        """
        Initialize a candy cane with type and candy parameters.
        :param type: str red or green
        :param kwargs: dict keyword arguments to create a Candy
        """
        self.colour = colour
        kwargs['has_lactose'] = True
        kwargs['has_nuts'] = False
        super().__init__(**kwargs)


class CremeEggs(Candy):
    """
    The candy that confused my childhood. An Easter bunny and a chicken
    fall in love and lay...chocolate eggs? Evolution for the win!
    """

    def __init__(self, pack_size: int, **kwargs):
        super().__init__(**kwargs)
        self.pack_size = pack_size
        kwargs['has_lactose'] = False
        kwargs['has_nuts'] = True
