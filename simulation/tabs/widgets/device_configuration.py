from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from simulation.nodes.elements import Element


# move in separate file
class DeviceConfigWindow(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.devices.values = Element.registered_elements.keys()