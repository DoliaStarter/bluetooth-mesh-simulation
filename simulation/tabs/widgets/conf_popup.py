import re
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty, StringProperty
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class BadDeviceDescription(Exception):
    pass


class ConfPopup(Popup):
    publishing_id = ObjectProperty()
    subscribed = StringProperty()

    def __init__(self, conf_window, device_row: 'DeviceRow', **kwargs):
        super().__init__(**kwargs)
        self.conf_window = conf_window
        self.device_row = device_row
        self.title = f"Configuring {self.device_row.chosen_device['device']}"
        if self.device_row.chosen_device['device'] == "sensor":
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
        else:
            raise BadDeviceDescription()

    def add_new_elem(self):
        try:
            self.device_row.save_config(self._parse())
            self.conf_window.new_element()
            self.conf_window.save_previous_slot()
            self.dismiss()
        except BadDeviceDescription:
            print("Bad device description provided")

    def add_id_to_pop(self, *args, text=""):
        text_input = TextInput(hint_text='Subscribed id:',
                               height="45dp", multiline=False, size_hint_y=None)
        text_input.bind(on_text_validate=self.add_id_to_pop)
        text_input.text = text
        self.box_for_id.add_widget(text_input)

    def add_light_conf(self, *args, on=True):
        text_input = TextInput(hint_text="format HH:MM",
                               height="45dp", multiline=False, size_hint_y=None)
        if on:
            self.box_light_on.add_widget(text_input)
        else:
            self.box_light_off.add_widget(text_input)

    def validate_format(self):
        time = r'\d{2}:\d{2}'
        ids = r'\d+'
        match_time_on = re.match(time, self.box_light_on.children[0].text)
        match_time_off = re.match(time, self.box_light_off.children[0].text)
        match_id_pub = re.match(ids, self.publishing_id.text)
        match_id_sub = None
        for sub in self.box_for_id.children:
            match_id_sub = re.match(ids, sub.text)
        return bool(match_id_sub and match_id_pub and ((self.device_row.chosen_device['device'] == "sensor"
                                                        and match_time_on and match_time_off) or self.device_row.chosen_device['device'] != "sensor"))
