from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from simulation.nodes.elements import Element

from kivy.factory import Factory

from simulation.tabs.widgets.conf_popup import ConfPopup


class DeviceConfigWindow(ScrollView):

    def __init__(self, config_panel, **kwargs):
        super().__init__(**kwargs)
        self.new_element()
        self._config_panel = config_panel

    def new_element(self):
        block = DeviceRow()
        self.container.add_widget(block)

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





class DeviceRow(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.devices.values = Element.registered_elements.keys()

    def __init__(self):
        self.open_conf.bind(on_press=ConfPopup)



