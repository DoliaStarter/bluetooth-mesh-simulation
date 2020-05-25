from kivy.uix.button import Button
from simulation.nodes import Node
from .tile import Tile


class Slot(Tile, Button):
    """
    Type of `Tile` to which device can be assigned.
    """

    def __init__(self):
        self.content = []
        super().__init__()
        """
        Node placed in this slot.
        """

    def save_device(self, device_record: dict):
        """
        :param device_record: add new device to current slot
        {
            'device': self.device,
            'publishing': self.publishing,
            'subcribed': self.subcribed,
        }
        """
        self.content.append(device_record)

    def __str__(self):
        return str(self.content)
