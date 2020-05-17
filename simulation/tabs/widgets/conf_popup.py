import kivy
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.popup import Popup


class ConfPopup(Popup):
    def btn(self):
        show_popup()

class ConfPopup(FloatLayout):
    pass


class MyApp(App):
    def build(self):
        return ConfPopup()


def show_popup():
    show = ConfPopup()

    popupWindow = Popup(title="Popup Window", content=show, size_hint=(None,None),size=(400,400))

    popupWindow.open()


