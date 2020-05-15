class Environment:
    """
    Class which should state of world.

    Provide interface to interaction between nodes and elements.
    """
    temperature = 0
    humidity = 0
    illuminance = 0

    @staticmethod
    def heat():
        """
        Affect temperature and humidity.
        """
        pass

    @staticmethod
    def turn_light():
        """
        Affect illuminance
        """
        pass
    
