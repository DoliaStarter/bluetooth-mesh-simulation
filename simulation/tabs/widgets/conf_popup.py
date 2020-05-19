import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class ConfPopup(Popup):
    #conf_window = ObjectProperty()

    def __init__(self, conf_window, **kwargs):
        super().__init__(**kwargs)
        self.conf_window = conf_window
        self.open()

    def add_new_elem(self):
        self.conf_window.new_element()
        self.dismiss()
