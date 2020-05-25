import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class ConfPopup(Popup):

    publishing_id = ObjectProperty()
    subcribed = StringProperty()

    def __init__(self, conf_window, device_row: 'DeviceRow', **kwargs):
        super().__init__(**kwargs)
        self.conf_window = conf_window
        self.device_row = device_row
        self.title = f"Configuring {self.device_row.chosen_device['device']}"
        self.publishing_id.text = self.device_row.chosen_device['publishing']
        for subscribed_id in self.device_row.chosen_device['subcribed']:
            self.box_for_id.add_widget(SubId(self, subscribed_id))
        self.box_for_id.add_widget(SubId(self, ''))
        self.open()

    def _parse(self):
        return {
            'device': self.device_row.chosen_device['device'],
            'publishing': self.publishing_id.text,
            'subcribed': [_id.text for _id in self.box_for_id.children]
        }

    def add_new_elem(self):
        self.device_row.save_config(self._parse())
        self.conf_window.new_element()
        self.dismiss()


class SubId(TextInput):

    def __init__(self, popup, subscribed_id, **kwargs):
        super().__init__(**kwargs)
        self.popup = popup
        self.text = subscribed_id

    def add_id_to_pop(self):
        self.parent.add_widget(SubId(self.popup, ''))
