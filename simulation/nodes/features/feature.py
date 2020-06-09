from kivy.clock import Clock


class Feature:
    """
    Base class for all features
    """
    roles = {}

    def __init__(self, device, use_scheduler=False, freq=1, **kwargs):
        super().__init__()
        self.device = device
        self.event = None
        if use_scheduler:
            self.event = Clock.schedule_interval(self.do_action, freq)

    def __init_subclass__(cls):
        Feature.roles[cls.__name__.lower()] = cls

    @staticmethod
    def from_name(name, device):
        if name.lower() == 'low power device':
            return Feature.roles['lowpowernode'](device)
        elif not name:
            return None
        return Feature.roles[name.lower()](device)

    def on_receive(self, frame):
        """
        Called on frame receive
        """

    def do_action(self, dt):
        """
        Doing action.
        """

    def on_destroy(self):
        if self.event:
            Clock.unschedule(self.event)
