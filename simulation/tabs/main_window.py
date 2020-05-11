from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.properties import ObjectProperty
from kivy.uix.button import Button
from kivy.factory import Factory
from kivy.uix.boxlayout import BoxLayout
import os.path
from simulation.network import Surface,Slot, Wall, Empty
from .widgets import FileChooser, DeviceConfigWindow
Builder.load_file("simulation/gui/main_window.kv")


class MainWindow(BoxLayout):
    map_area = ObjectProperty()
    config_panel = ObjectProperty()
    tab_panel = ObjectProperty()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def run(self, map_):
        """Simple demo, that prints file converted to tilemap into console."""
        surface = Surface(map_)
        self.map_area.clear_widgets()
        self.map_area.cols = surface.width
        # currently exists only one type on config 
        self.current_config = DeviceConfigWindow()
        for line in surface._surface:
            for tile in line:
                if isinstance(tile, Slot):
                    slot = Factory.Slot()
                    slot.bind(on_press=lambda _: self._open_current_config_window())
                    self.map_area.add_widget(slot)
                elif isinstance(tile, Wall):
                    self.map_area.add_widget(Factory.Wall())
                elif isinstance(tile, Empty):
                    self.map_area.add_widget(Factory.Empty())

    def upload_map(self):
        FileChooser(callback=self.run)

    def _open_current_config_window(self):
        self.config_panel.clear_widgets()
        self.config_panel.add_widget(self.current_config)



