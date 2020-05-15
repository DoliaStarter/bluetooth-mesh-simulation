from .feature import Feature


class Relay(Feature):
    def receive(self, frame):
        """
        Transmits frame further to network,
        """
