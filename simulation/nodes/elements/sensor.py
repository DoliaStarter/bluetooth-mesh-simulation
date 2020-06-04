from . import Element
from datetime import datetime
from simulation.environment import Environment
from simulation.network import Content

class Sensor(Element):
    def __init__(self, content, node):
        super().__init__(content, node, use_scheduler=True)
        now = Environment.time  
        light_on = content['time_on'].split(":")
        light_off = content['time_off'].split(":")
        self.on = now.replace(hour=int(light_on[0]), minute=int(light_on[1]), second=0)
        self.off = now.replace(hour=int(light_off[0]), minute=int(light_off[1]), second=0)

    def do_action(self, dt):
        time = Environment.time
        if time < self.on:
            self.send(Content.LIGHT_ON)
        else:
            self.send(Content.LIGHT_OFF)
