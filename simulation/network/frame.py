"""Decribe messages that are passing through network."""
from dataclasses import dataclass


@dataclass
class Frame:
    """
    Describe frame, that devices sen to each other.
    :param topic: topic of this message
    :param ttl: how many hops this fram can made
    :param content: message sent with this frame
    """
    topic: str
    ttl: int
    content: str

    def __str__(self):
        return f"Frame on topic '{self.topic}'. TTL: {self.ttl}"