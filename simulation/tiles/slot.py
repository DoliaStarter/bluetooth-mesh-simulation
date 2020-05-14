from kivy.uix.button import Button
from simulation.nodes import Node
from .tile import Tile

class Slot(Tile, Button):
    """
    Type of `Tile` to which device can be assigned.
    """

    def __init__(self):
        super().__init__()
        self.content = None
        """
        Node placed in this slot.
        """

