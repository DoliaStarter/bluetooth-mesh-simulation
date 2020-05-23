import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.textinput import TextInput
from kivy.uix.popup import Popup


class ConfPopup(Popup):
    # conf_window = ObjectProperty()

    def __init__(self, conf_window, **kwargs):
        super().__init__(**kwargs)
        self.conf_window = conf_window
        self.add_pub_id()
        self.open()

    def add_new_elem(self):
        self.conf_window.new_element()
        self.dismiss()

    def add_pub_id(self):
        block = PubId(self)
        self.box_for_id.add_widget(block)


class PubId(TextInput):
    # open_conf =ObjectProperty()
    def __init__(self, popup, **kwargs):
        super().__init__(**kwargs)
        self.popup = popup

    def add_id_to_pop(self):
        self.popup.add_pub_id()
