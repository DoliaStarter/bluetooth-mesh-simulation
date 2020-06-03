from . import Element
from datetime import datetime, date, time


# TODO implement logic
class Sensor(Element):
    def __init__(self, content, node):
        super().__init__(content, node, use_scheduler=True)
        self.time_on = content['time_on']
        self.time_off = content['time_off']

    def do_action(self, dt):
        now = datetime.now()
        light_on = self.time_on.split(":")
        light_off = self.time_off.split(":")
        on = now.replace(hour=light_on[0], minute=light_on[1], second=0)
        off = now.replace(hour=light_off[0], minute=light_off[1], second=0)
        if now < on:
            print("Too Early to switch lights on")
        if on < now < off:
            print("Too early to switch lights down")
