class Zoo():
    __animals = 0
    def __init__(self, name_of_the_zoo):
        self.name = name_of_the_zoo
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animals(self, species, name):
        if species == 'mammal':
            self.mammals.append(name)
        elif species == 'fish':
            self.fishes.append(name)
        elif species == 'bird':
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):

        if species == 'mammal':
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.mammals)}\nTotal animals: {Zoo.__animals}"

        elif species == 'fish':
            return f"{species.capitalize()}es in {self.name}: {', '.join(self.fishes)}\nTotal animals: {Zoo.__animals}"

        elif species == 'bird':
            return f"{species.capitalize()}s in {self.name}: {', '.join(self.birds)}\nTotal animals: {Zoo.__animals}"


zoo_name = input()
zoo = Zoo(zoo_name)

input_nmbr = int(input())

for _ in range(input_nmbr):
    species, name = input().split()
    zoo.add_animals(species, name)

species = input()

print(zoo.get_info(species))