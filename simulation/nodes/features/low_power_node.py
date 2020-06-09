from .feature import Feature
from simulation.network import Frame, Type, Content


class LowPowerNode(Feature):
    def __init__(self, device, **kwargs):
        super().__init__(device, True, 10, **kwargs)
        self.device.stop_scheduler()
        self.is_radio_active = False
        self.subscribe()

    def subscribe(self):
        topics = ",".join(self.device.subscribed)
        frame = Frame(self.device.publishing, 11,
                      content=Content.SUBSCRIPTION, type_=Type.SUBSCRIPTION, payload=topics)
        self.device.node.send(frame)

    def do_action(self, dt):
        self.is_radio_active = not self.is_radio_active
        if self.is_radio_active:
            frame = Frame(self.device.publishing, 11,
                          content=Content.REQUEST, type_=Type.FRIEND_REQUEST)
            self.device.node.send(frame)

    def on_receive(self, frame):
        """
        Does nothing.
        """
        if self.is_radio_active:
            self.device.on_receive(frame)
