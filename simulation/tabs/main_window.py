from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
import os.path
from simulation.network import Surface
from simulation.tiles import Slot
from .widgets import FileChooser, DeviceConfigWindow
Builder.load_file("simulation/gui/main_window.kv")


class MainWindow(BoxLayout):
    map_area = ObjectProperty()
    config_panel = ObjectProperty()
    tab_panel = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.device_config = DeviceConfigWindow(self.config_panel)

    def run(self, map_):
        """Simple demo, that prints file converted to tilemap into console."""
        surface = Surface(map_)
        self.map_area.clear_widgets()
        self.map_area.cols = surface.width
        for line in surface._surface:
            for tile in line:
                if isinstance(tile, Slot):
                    tile.bind(on_press=self._open_device_config)
                self.map_area.add_widget(tile)

    def upload_map(self):
        FileChooser(callback=self.run)

    def _open_device_config(self, slot):
        """
        Opens device config window for slot.

        :param slot: slot pressed by user.
        """
        self.device_config.open(slot)
