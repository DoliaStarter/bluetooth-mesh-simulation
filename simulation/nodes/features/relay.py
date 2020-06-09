from .feature import Feature


class Relay(Feature):
    
    def on_receive(self, frame):
        """
        Transmits frame further to network,
        """
        frame.ttl = str(int(frame.ttl) - 1)
        if int(frame.ttl) > 0:
            self.device.node.send(frame)
