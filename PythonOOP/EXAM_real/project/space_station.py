from project.planet.planet import Planet
from project.astronaut.biologist import Biologist
from project.astronaut.astronaut_repository import AstronautRepository


class SpaceStation:
    def __init__(self):
        self.astronaut_repository = []
        self.planet_repository = []


    def add_astronaut(self, astronaut_type:str, name:str):
        astr_types = ["Biologist", "Geodesist", "Meteorologist"]
        if not astr_types in astr_types:
            raise Exception("Astronaut type is not valid!")
        astronaut = astronaut_type(name)
        astr = [a for a in self.astronaut_repository if a.name == name]
        if not astr:
            self.astronauts.append(astronaut)
            return f"Successfully added {astronaut_type}: {name}."

    def add_planet(self, name:str, items:str):
        items = list(items)
        pln = [p.name for p in self.planet_repository]
        if not name in pln:
            planet = Planet(name, items)
            self.planet_repository.append(planet)
            return f"Successfully added Planet: {planet.name}."
        return f"{name} is already added."

    def retire_astronaut(self, name:str):
        astr = [a for a in self.astronaut_repository if a.name == name]
        if astr:
            self.astronaut_repository.remove(astr)
            return f"Astronaut {name} was retired!"
        return f"Astronaut {name} doesn't exists!"

    def recharge_oxygen(self):
        for a in self.astronaut_repository:
            a.oxygen += 10


    def send_on_mission(self, plane_name:str):
        pass

    def report(self):
        pass