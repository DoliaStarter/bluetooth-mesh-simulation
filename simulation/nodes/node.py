"""Contains abstract base for all nodes"""
from simulation.network import Frame
# https://www.bluetooth.com/blog/3-key-factors-that-determinethe-range-of-bluetooth/
from .elements import Element

class Node:
    """Device/collection of devices, that could communicate via network."""
    count = 0

    def __init__(self, elements: list, topics: dict, feature = None):
        """
        :param elements: elements, that will be placed in this node
        :param topics: dict, where key is a topic and all subscribed devices in this node are values
        {'temperature': [device1, device2, device3 ...]}
        :param feature: describes, what should do this node on receiving
        """
        self.id = self._set_id()
        self._elements = elements
        self._topics = topics
        self.roles = []
        self._transmitting_power = 10
        self._sensitivity = 5
        """
        Minimum power of signal, that this node could receive
        """
        self._feature = feature

    @property
    def transmitting_power(self) -> int:
        return self._transmitting_power

    @transmitting_power.setter
    def transmitting_power(self, value):
        self._transmitting_power = value

    @property
    def sensitivity(self) -> int:
        return self._sensitivity

    @sensitivity.setter
    def sensitivity(self, value) -> int:
        self._sensitivity = value

    def _set_id(self) -> int:
        Node.count += 1
        return Node.count

    def receive(self, frame: Frame):
        """Receives frame passed to device."""
        if self._feature:
            self._feature.receive(frame)
        # check if really such mechanism ?
        else:
            for element in self._topics[frame.topic]:
                element.receive(frame)


    def could_receive(self, signal_power) -> bool:
        return self.sensitivity < signal_power

    def add_element(self, device):
        # Change 
        dev = Element.from_name(device['device'])
        self._elements.append(dev)