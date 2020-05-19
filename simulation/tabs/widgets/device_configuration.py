from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView
from kivy.properties import ObjectProperty
from functools import partial
from simulation.nodes.elements import Element

from kivy.factory import Factory

from simulation.tabs.widgets.conf_popup import ConfPopup


class DeviceConfigWindow(ScrollView):

    def __init__(self, config_panel, **kwargs):
        super().__init__(**kwargs)
        self.new_element()
        self._config_panel = config_panel

    def new_element(self):
        block = DeviceRow(self)
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

    def save_config(self, config_record: dict):
        """
        Saves configuration for current device
        :param config_record: dict, that describes configuration for current device
        {
            'device': self.device,
            'publishing': self.publishing,
            'subcribed': self.subcribed,
        }
        """
        self.current_slot.save_device(config_record)


class DeviceRow(BoxLayout):
    open_conf = ObjectProperty()

    def __init__(self, conf_window, **kwargs):
        super().__init__(**kwargs)
        self.devices.values = Element.registered_elements.keys()
        self.open_conf.bind(on_press=lambda _: ConfPopup(
            conf_window, self.devices.text))

    def remove(self):
        if len(self.parent.children) > 1:
            self.parent.remove_widget(self)
