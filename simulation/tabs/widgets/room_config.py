from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from simulation.environment import Environment
from kivy.clock import Clock

class RoomConfigWindow(BoxLayout):

    temperature = ObjectProperty()
    illuminance = ObjectProperty()
    time_string = ObjectProperty()

    def __init__(self, main_window: 'MainWindow', **kwargs):
        super().__init__(**kwargs)
        self._config_panel = main_window.config_panel
        self.temperature = Environment.temperature
        self.illuminance = Environment.illuminance
        self.time_string = Environment.time.strftime("%H:%M")
        Clock.schedule_interval(self.affect_temperature, 1)
        Clock.schedule_interval(self.current_time, 0.1)
        #illum_affect ???

    def affect_temperature(self, dt):
        Environment.heat()
        self.temperature = Environment.temperature

    def affect_illuminance(self):
        Environment.turn_light()
        self.illuminance = Environment.illuminance

    def current_time(self, dt):
        Environment.set_time()
        self.time_string = Environment.time.strftime("%H:%M")
        

    def open(self):
        """
        Opens config window for slot.
        :param slot: slot with node for this config
        """
        self._config_panel.clear_widgets()
        self._config_panel.add_widget(self)

    def close(self):
        """Closing this window."""
