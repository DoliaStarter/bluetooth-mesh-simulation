from kivy.uix.filechooser import FileChooserIconView
from kivy.uix.screenmanager import Screen, FadeTransition
from kivy.lang import Builder
from kivy.uix.relativelayout import RelativeLayout
from kivy.properties import ObjectProperty
from os.path import join, curdir, basename
from simulation.utils import FileManager


class ScreenFileChooser(Screen):
    """Provides interface for interaction with filesystem."""

    file_chooser = ObjectProperty()

    def __init__(self, screen_manager, simulation, **kwargs):
        kv_path = f"simulation/gui/widgets/{str.lower(self.__class__.__name__)}.kv"
        Builder.load_file(kv_path)
        super(ScreenFileChooser, self).__init__(**kwargs)
        self.file_chooser.filters = [lambda folder,
                                     filename: not filename.endswith('.sys')]
        self.file_chooser.path = join(curdir, "simulation/maps/")
        self.sm = screen_manager
        self.simulation = simulation

    def upload_map(self, filename):
        print(filename)
        map_ = FileManager.load(join(self.file_chooser.path, basename(filename)))
        self.simulation.run(map_)
        self.close()

    def close(self):
        self.sm.transition.duration = 1
        self.sm.transition = FadeTransition()
        self.sm.current = 'main'
