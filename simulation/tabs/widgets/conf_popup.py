import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.popup import Popup


class ConfPopup(Popup):

    device_label = ObjectProperty()
    publishing = StringProperty()
    subcribed = StringProperty()

    def __init__(self, conf_window, device: str, **kwargs):
        super().__init__(**kwargs)
        self.conf_window = conf_window
        self.device_label.text = f'Configuring {device}'
        self.device = device
        self.open()

    def _parse(self):
        return {
            'device': self.device,
            'publishing': self.publishing,
            'subcribed': self.subcribed,
        }

    def add_new_elem(self):
        self.conf_window.save_config(self._parse())
        self.conf_window.new_element()
        self.dismiss()
