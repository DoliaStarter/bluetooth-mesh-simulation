from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from simulation.nodes.elements import Element
from kivy.factory import Factory
# move in separate file


class DeviceConfigWindow(ScrollView):

    def __init__(self, config_panel, **kwargs):
        super().__init__(**kwargs)
<<<<<<< HEAD
        self.devices.values = Element.registered_elements.keys()
        self._config_panel = config_panel

    def _parse_slot(self):
        """
        Parse self.current_slot with devices and fill scroll view with them.
        """

    def open(self, slot):
        """
        Opens config window for slot.

        :param slot: slot with node for this config
        """
        self.current_slot = slot
        self._parse_slot()
        self._config_panel.clear_widgets()
        self._config_panel.add_widget(self)
=======
        self.newElement()

    def newElement(self):
        block = Factory.DeviceRaw()
        self.container.add_widget(block)


class DeviceRaw(BoxLayout):

        def __init__(self, **kwargs):
            super().__init__(**kwargs)
            self.devices.values = Element.registered_elements.keys()
>>>>>>> 67dd6113b8777cb2708ae6900e90bee4a89e3bbe
