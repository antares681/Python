from project.astronaut.astronaut import Astronaut


class AstronautRepository:

    def __init__(self):
        self.astronauts = []

    def add(self, astronaut:Astronaut):
        if astronaut not in self.astronauts:
            self.astronauts.append(astronaut)

    def remove(self, astronaut: Astronaut):
        if astronaut in self.astronauts:
            self.astronauts.remove(astronaut)

    def find_by_name(self, name: str):
        astr = [a.name for a in self.astronauts if a.name == name]
        if astr:
            return astr[0]
