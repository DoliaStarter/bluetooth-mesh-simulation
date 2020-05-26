"""Decribe messages that are passing through network."""
from dataclasses import dataclass
from enum import IntEnum

# never declare generic a enum !
class Content(IntEnum):
    START_HEAT = 0
    STOP_HEAT = 1

@dataclass
class Frame:
    """
    Describe frame, that devices sen to each other.
    :param topic: topic of this message
    :param ttl: how many hops this fram can made
    """
    topic: str
    ttl: int
    content: Content

    def __str__(self):
        return f"Frame on topic '{self.topic}'. TTL: {self.ttl}"