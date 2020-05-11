class Element:
    # dict with all registered elements
    registered_elements = {}
    def __init__(self):
        self._batery_level = 1

    def on_environment_change(self, environment_variable_value):
        """
        Reacts on changes in environment. Default implementation does nothing.
        :param environment_variable_value: new value of environment variable.
        """

    def __init_subclass__(cls):
        """Register created elements"""
        Element.registered_elements[str.lower(cls.__name__)] = cls

    @staticmethod
    def from_name(class_name, env):
        return Element.registered_elements[class_name](env)
