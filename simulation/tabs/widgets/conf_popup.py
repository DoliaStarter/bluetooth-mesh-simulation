import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class ConfPopup(Popup):

    def __init__(self, callback, **kwargs):
        super().__init__(**kwargs)
        self.open()

