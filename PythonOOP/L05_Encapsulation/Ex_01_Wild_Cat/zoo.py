from Ex_01_Wild_Cat.keeper import Keeper
from Ex_01_Wild_Cat.caretaker import Caretaker
from Ex_01_Wild_Cat.vet import Vet

class Zoo:
    def __init__ (self, name: str, budget: int, animal_capacity: int, workers_capacity:int):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.__budget -= price
            self.animals.append(animal)
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        if self.__budget < price:
            return 'Not enough budget'
        return 'Not enough space for animal'

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        workers_to_fire = [worker_to_fire for worker_to_fire in self.workers if worker_to_fire.name == worker_name]
        if workers_to_fire:
            self.workers.remove(workers_to_fire[-1])
            return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        workers_salaries = sum([worker.salary for worker in self.workers])
        if self.__budget >= workers_salaries:
            self.__budget -= workers_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_money = sum([animal.money_for_care for animal in self.animals])
        if self.__budget >= tending_money:
            self.__budget -= tending_money
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        tigers_info = [repr(animal) for animal in self.animals if animal.__class__.__name__ == 'Tiger']
        cheetahs_info = [repr(animal) for animal in self.animals if animal.__class__.__name__ == 'Cheetah']
        lions_info = [repr(animal) for animal in self.animals if animal.__class__.__name__ == 'Lion']

        result = f"You have {len(lions_info) + len(tigers_info) + len(cheetahs_info)} animals\n"
        result += f'----- {len(lions_info)} Lions:' + '\n' + "\n".join(lions_info) + '\n'
        result += f'----- {len(tigers_info)} Tigers:'+ '\n' + "\n".join(tigers_info) + "\n"
        result += f'----- {len(cheetahs_info)} Cheetahs:' + '\n' + "\n".join(cheetahs_info)

        return result

    def workers_status(self):
        result = f'You have {len(self.workers)} workers\n'
        keepers_info = [repr(worker) for worker in self.workers if type(worker) == Keeper]
        caretakers_info = [repr(worker) for worker in self.workers if type(worker) == Caretaker]
        vetes_info = [repr(worker) for worker in self.workers if type(worker) == Vet]
        result += f'----- {len(keepers_info)} Keepers:' + '\n' + "\n".join(keepers_info) + '\n'
        result += f'----- {len(caretakers_info)} Caretakers:' + '\n' + "\n".join(caretakers_info) + "\n"
        result += f'----- {len(vetes_info)} Vets:' + '\n' + "\n".join(vetes_info)
        return result

#TODO DETAILED CODE BELOW
        # def workers_status(self):
    #     result = f'You have {len(self.workers)} workers\n'
    #
    #     amount_of_keepers = 0
    #     keepers_info = []
    #     for worker in self.workers:
    #         if type(worker) == Keeper:
    #             amount_of_keepers += 1
    #             keepers_info.append(repr(worker))
    #
    #     amount_of_caretakers = 0
    #     caretakers_info = []
    #     for worker in self.workers:
    #         if type(worker) == Caretaker:
    #             amount_of_caretakers += 1
    #             caretakers_info.append(repr(worker))
    #
    #     amount_of_vetes = 0
    #     vetes_info = []
    #     for worker in self.workers:
    #         if type(worker) == Vet:
    #             amount_of_vetes += 1
    #         vetes_info.append(repr(worker))
    #
    #
    #     result += f'----- {amount_of_keepers} Keepers:'
    #     keepers_result = "\n".join(keepers_info)
    #     result += keepers_result + '\n'
    #
    #     result += f'----- {amount_of_caretakers} Caretakers:'
    #     caretakers_result = "\n".join(caretakers_info)
    #     result += caretakers_result + '\n'
    #
    #     result += f'----- {amount_of_vetes} Vetes:'
    #     vetes_result = "\n".join(vetes_info)
    #     result += vetes_result + '\n'
    #     return result


