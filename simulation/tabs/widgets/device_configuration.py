from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from simulation.nodes.elements import Element
from kivy.factory import Factory
# move in separate file


class DeviceConfigWindow(ScrollView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.newElement()

    def newElement(self):
        block = Factory.DeviceRaw()
        self.container.add_widget(block)


class DeviceRaw(BoxLayout):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.devices.values = Element.registered_elements.keys()
