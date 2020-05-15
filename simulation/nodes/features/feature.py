class Feature:
    """
    Base class for all features
    """
    def __init__(self, corresponding_node):
        super().__init__()
        self.node = corresponding_node