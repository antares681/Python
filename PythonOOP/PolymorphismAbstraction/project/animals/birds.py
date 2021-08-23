from abc import ABC, abstractmethod

@abstractmethod
class Bird(ABC):
    def __init__(self):
        return

class Owl(Bird):
   super().__init__(self)

   def make_sound(self):
        return 'Hoot Hoot'

class Hen(Bird):
    def make_sound(self):
        return 'Cluck'