import re
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
    subscribed = StringProperty()

    def __init__(self, conf_window, device_row: 'DeviceRow', **kwargs):
        super().__init__(**kwargs)
        self.conf_window = conf_window
        self.device_row = device_row
        self.title = f"Configuring {self.device_row.chosen_device['device']}"
        if self.device_row.chosen_device['device'] == "light":
            self.add_light_conf(on=True)
            self.add_light_conf(on=False)
        self.publishing_id.text = self.device_row.chosen_device['publishing']
        for subscribed_id in self.device_row.chosen_device['subcribed']:
            self.add_id_to_pop(text=subscribed_id)
        if len(self.device_row.chosen_device['subcribed']) == 0:
            self.add_id_to_pop()
        self.open()

    def _parse(self):
        if self.validate_format():
            if self.device_row.chosen_device['device'] != "sensor":
                return {
                    'device': self.device_row.chosen_device['device'],
                    'publishing': self.publishing_id.text,
                    'subcribed': [_id.text for _id in self.box_for_id.children]
                }
            else:
                return {
                    'device': self.device_row.chosen_device['device'],
                    'publishing': self.publishing_id.text,
                    'subcribed': [_id.text for _id in self.box_for_id.children],
                    'time_on': self.box_light_on.children[0].text,
                    'time_off': self.box_light_off.children[0].text
                }

    def add_new_elem(self):
        self.device_row.save_config(self._parse())
        #if self.device_row.chosen_device['device'] == 'light':
        #    self.conf_window.add_widegt(LightConf())
        #    pass
        self.conf_window.new_element()
        self.dismiss()

    def add_id_to_pop(self, *args, text=""):
        text_input = TextInput(hint_text='Subscribed id:', height="45dp", multiline=False, size_hint_y=None)
        text_input.bind(on_text_validate=self.add_id_to_pop)
        text_input.text = text
        self.box_for_id.add_widget(text_input)

    def add_light_conf(self, *args, on= True):
        text_input = TextInput(hint_text="format HH:MM", height="45dp", multiline=False, size_hint_y=None)
        #buttoncallback = lambda _: self.validate_format(text_input.text)
        #text_input.bind(on_text_validate=buttoncallback)
        if on:
            self.box_light_on.add_widget(text_input)
            print("adding light on")
        else:
            self.box_light_off.add_widget(text_input)
            print("adding light off")

    def validate_format(self):
        time = r'\d{2}:\d{2}'
        ids = r'\d+'
        match_time_on = re.match(time, self.box_light_on.children[0].text)
        match_time_off = re.match(time, self.box_light_off.children[0].text)
        match_id_pub = re.match(ids, self.publishing_id.text)
        match_id_sub = None
        for sub in self.box_for_id.children:
            match_id_sub = re.match(ids, sub.text)
        if match_id_sub or match_id_pub or match_time_on or match_time_off:
            return True
        else:
            return False


