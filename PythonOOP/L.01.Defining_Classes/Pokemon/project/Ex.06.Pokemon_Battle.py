class Pokemon:
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def pokemon_details(self):
        return f"{self.name} with health {self.health}"

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = []


    def add_pokemon(self, pokemon:str):
        if not pokemon in self.pokemon:
            return f"Caught {pokemon} with health {Pokemon(pokemon)}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon):
        if not pokemon in self.pokemon:
            return f"Pokemon is not caught"
        return f"You have released {Pokemon(pokemon.name)}"
    #
    # def trainer_data(self):
    #     pass
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
# print(trainer.trainer_data())
