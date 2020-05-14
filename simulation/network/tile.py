"""Contains description of `Tile` from which  `Surface` consists."""
from enum import Enum, auto
from simulation.network import Frame
from simulation.nodes import Node
from kivy.uix.label import Label
from kivy.uix.button import Button

# addresses = {
#     '1.1.1.1': [termometr_1, termometr_2]
# }

# def add_listener(self, ip, listener):
#     self.addresses[ip].add(listener)

# def send(self, topic, frame):
#     for subscriber in self.topics[topic]:
#         subscriber.receive(frame)

class TileType(Enum):
    """Type of created tile. Used for map parsing."""
    EMPTY = 0
    SLOT = 1
    WALL = 2


class Tile:
    """Describes the most basic empty element  of `Surface`."""
    tile_types = {}
    tiles_created = 0
    # TODO Move assigment to Network
    frames_passed = 0

    def __init__(self, **kwargs):
        """
        On create all tiles are empty because they still hadn't received.
        nothing, and there no devices connected to them.
        """
        super().__init__(**kwargs)
        Tile.tiles_created += 1
        self._id = Tile.tiles_created
        self._content = None
        self.neinghbors = []

    def assign_frame_id(self, frame: Frame) -> int:
        """
        Assigns frame id, to frame so it could be identified on `Tile` level
        :param frame: - unregistered Frame
        :return: - assigned id
        """
        Tile.frames_passed += 1
        frame.frame_id = Tile.frames_passed
        return Tile.frames_passed

    @staticmethod
    def from_int(tile_as_int: int, **kwargs):
        """
        Creates new Tile from int if int is a valid type.
        :param `tile_as_int` - integer representation of tile.
        :return: - newly created corresponding to this integer
        """
        if tile_as_int not in Tile.tile_types.keys():
            raise ValueError(f"{tile_as_int} not a valid tile type")
        return Tile.tile_types[tile_as_int](**kwargs)

    def __init_subclass__(cls):
        Tile.tile_types[TileType[str.upper(cls.__name__)].value] = cls

    def __str__(self):
        return str.lower(self.__class__.__name__)


class Slot(Tile, Button):
    """
    Type of `Tile` to which device can be assigned.
    """

    def __init__(self):
        super().__init__()
        self.content = None

    def assign_node(self, node: Node):
        """
        Assign new node to this slot.

        :param node: new node to assign
        """
        self.content = node


class Wall(Tile, Label):
    """
    Type of Tile from which Frame can't pass
    """

class Empty(Tile, Label):
    """
    Type of tile where nothing can't happend.
    """
