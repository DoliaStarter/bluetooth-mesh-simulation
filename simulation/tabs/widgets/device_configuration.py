from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from simulation.nodes.elements import Element


# move in separate file
class DeviceConfigWindow(BoxLayout):

    def __init__(self, config_panel, **kwargs):
        super().__init__(**kwargs)
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
