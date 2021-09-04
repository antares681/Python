from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, 'Power', capacity = int(capacity * 0.25), memory= int(memory * 0.75))