class Planet:
    def __init__(self, name):
        self.name = name
        self.items = []

    @property
    def name(self):
        return

    @name.setter
    def name(self, value):
        if value == "" or value.isspace():
            raise ValueError("Planet name cannot be empty string or whitespace!")
        self.__name = value