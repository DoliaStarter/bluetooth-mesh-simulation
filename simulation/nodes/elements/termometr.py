from . import Element

class Termometr(Element):
    def __init__(self, env):
        self.__threshold = None
        self.__env = env

    @property
    def threshold(self):
        return self.__threshold

    @threshold.setter
    def threshold(self, value):
        self.__threshold = value

    def on_environment_change(self, newvalue):
        if newvalue > self.__threshold:
            print("newvalue > threshhold")









