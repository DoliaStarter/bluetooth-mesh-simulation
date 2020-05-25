

class Environment:
    """
    Class which should state of world.

    Provide interface to interaction between nodes and elements.
    """
    temperature = 30
    humidity = 0
    illuminance = 0

    heaters = []

    @staticmethod
    def heat():
        """
        Affect temperature and humidity.
        """
        # if zero heaters, than temperature will decrease
        coeficient = len(Environment.heaters) - 1
        Environment.temperature += coeficient * 0.01

    @staticmethod
    def turn_light():
        """
        Affect illuminance
        """
        pass
