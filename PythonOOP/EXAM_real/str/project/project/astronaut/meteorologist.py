from project.astronaut.astronaut import Astronaut

class Meteorologist(Astronaut):
    def __init__(self, name):
        super().__init__(name, 90)

    def breathe(self):
        self.oxygen -= self.breath

    @property
    def breath(self):
        return 15