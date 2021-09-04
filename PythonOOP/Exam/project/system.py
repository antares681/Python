from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name:str, capacity:int, memory:int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            hrd = [h for h in System._hardware if h.name == hardware_name][0]
            sft = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hrd.install(sft)
        except IndexError:
            raise "Hardware does not exist"
        except Exception as ex:
            return str(ex)


    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        pass

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        pass

    @staticmethod
    def analyze():
        pass

    @staticmethod
    def system_split():
        pass