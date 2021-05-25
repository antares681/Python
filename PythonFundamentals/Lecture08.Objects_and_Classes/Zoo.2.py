class Zoo:
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fish = []
        self.birds = []
        self.total_animals = 0



    def add_animal(self, species , name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fish.append(name)
        elif species == "bird":
            self.birds.append(name)
        self.total_animals += 1

    def get_info(self, species):
        result = None
        if species == "mammal":
            result = f'Mammals in {self.name}: {", ".join(self.mammals)}'
        elif species == "fish":
            result = f'Fishes in {self.name}: {", ".join(self.fish)}'
        elif species == "bird":
            result = f'Birds in {self.name}: {", ".join(self.birds)}'
        return result

    def get_final_info(self):
        return f'Total animals: {self.total_animals}'


name_of_zoo = input()
zoo = Zoo(name_of_zoo)
times = int(input())
for time in range(times):
    kind, animal = input().split()
    zoo.add_animal(kind, animal)
our_type = input()
print(zoo.get_info(our_type))
print(zoo.get_final_info())