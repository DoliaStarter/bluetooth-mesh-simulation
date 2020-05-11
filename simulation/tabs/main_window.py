from kivy.core.window import Window
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
import os.path
from simulation.network import Surface
from simulation.network import Slot, Wall, Empty



class MainWindow(Screen):
    map_area = ObjectProperty()
    config_panel = ObjectProperty()
    tab_panel = ObjectProperty()

    def __init__(self, screen_manager, **kwargs):
        kv_path = f"simulation/gui/{str.lower(self.__class__.__name__)}.kv"
        Builder.load_file(kv_path)
        super(MainWindow, self).__init__(**kwargs)
        self.sm = screen_manager

    def run(self, map_):
        """Simple demo, that prints file converted to tilemap into console."""
        surface = Surface(map_)
        self.map_area.clear_widgets()
        self.map_area.cols = surface.width
        self.device_config = DeviceConfig()
        for line in surface._surface:
            for tile in line:
                if isinstance(tile, Slot):
                    slot = Factory.Slot()
                    slot.bind(on_press=lambda _: self.open_device_config())
                    self.map_area.add_widget(slot)
                elif isinstance(tile, Wall):
                    self.map_area.add_widget(Factory.Wall())
                elif isinstance(tile, Empty):
                    self.map_area.add_widget(Factory.Empty())

    def open_device_config(self):
        self.config_panel.clear_widgets()
        self.config_panel.add_widget(self.device_config)


# move in separate file
class DeviceConfig(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
