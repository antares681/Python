from pokemon import Pokemon

class Trainer:
    def __init__(self, name):
        self.name = name
        self.pokemon = {}

    def add_pokemon(self, pokemon:Pokemon):
        if not pokemon.name in self.pokemon:
            self.pokemon[pokemon.name]=pokemon.health
            return f"Caught {pokemon.name} with health {pokemon.health}"
        return f"This pokemon is already caught"

    def release_pokemon(self, pokemon:str):
        for el in range(len(self.pokemon)):
            if pokemon in self.pokemon:
                released_pokemon = pokemon
                self.pokemon.pop(pokemon)
                return f"You have released {released_pokemon}"
        return f"Pokemon is not caught"

    def trainer_data(self):
        to_print = (f'Pokemon Trainer {self.name}\n'
                   f'Pokemoncount {len(self.pokemon)}\n')
        for p, d in self.pokemon.items():
            pokemon.name, pokemon.health = p, d
            to_print+= f'{pokemon.pokemon_details()}\n'
        return to_print

pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())