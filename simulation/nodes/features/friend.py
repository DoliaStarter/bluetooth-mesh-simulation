from .feature import Feature
from simulation.network import Type
from collections import defaultdict


class Friend(Feature):

    def __init__(self, device, **kwargs):
        super().__init__(device, **kwargs)
        self.topics = defaultdict(set)
        """
        Who subsribed on topic
        """
        self.subscribers = defaultdict(list)
        """
        Buckets for each subscriber
        """

    def on_receive(self, frame):
        """
        Cashe messages.
        """
        if frame.topic not in self.topics and frame.type != Type.SUBSCRIPTION:
            return

        if frame.type == Type.SUBSCRIPTION:
            self.subscribe(frame)
        elif frame.type != Type.FRIEND_REQUEST:
            self.store(frame)
        else:
            self.provide_info(frame)

    def is_msg_stored(self, frame, bucket):
        for cached_frame in self.subscribers[bucket]:
            if frame.content == cached_frame.content:
                return True
        return False

    def store(self, frame):
        for subscriber in self.topics[frame.topic]:
            if not self.is_msg_stored(frame, subscriber):
                self.subscribers[subscriber].append(frame)

    def subscribe(self, frame):
        """
        Creates mapping between topic and subscriber bucket
        """
        # frame.message corresponds to all subscribed topics separated by comma
        for topic in frame.message.split(","):
            self.topics[topic].add(frame.topic)


    def provide_info(self, frame):
        """
        Sends to low power device all messages that was cached.
        """
        for cached_frame in self.subscribers[frame.topic]:
            cached_frame.type = Type.CACHED_FRAME
            self.device.node.send(cached_frame)
        self.subscribers[frame.topic] = []
