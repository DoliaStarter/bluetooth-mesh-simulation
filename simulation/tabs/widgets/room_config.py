from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty


class RoomConfigWindow(BoxLayout):

    temperature = ObjectProperty()

    def __init__(self, main_window: 'MainWindow', **kwargs):
        super().__init__(**kwargs)
        self._config_panel = main_window.config_panel
        self.temperature = str(0)

    def open(self):
        """
        Opens config window for slot.

        :param slot: slot with node for this config
        """
        self._config_panel.clear_widgets()
        self._config_panel.add_widget(self)
    
    def close(self):
        """Closing this window."""
