from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


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
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        try:
            hrd = [h for h in System._hardware if h.name == hardware_name][0]
            sft = ExpressSoftware(name, capacity_consumption, memory_consumption)
            hrd.install(sft)
            System._software.append(sft)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)


    @staticmethod
    def register_light_software(hardware_name: str, name:str, capacity_consumption:int, memory_consumption:int):
        try:
            hrd = [h for h in System._hardware if h.name == hardware_name][0]
            sft = LightSoftware(name, capacity_consumption, memory_consumption)
            hrd.install(sft)
            System._software.append(sft)
        except IndexError:
            return "Hardware does not exist"
        except Exception as ex:
            return str(ex)

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hrd = [h for h in System._hardware if h.name == hardware_name][0]
            sft = [s for s in System._software if s.name == software_name][0]
            hrd.uninstall(sft)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        to_print = 'System Analysis\n'
        to_print += f'Hardware Components: {len(System._hardware)}\n'
        to_print += f'Software Components: {len(System._software)}\n'
        to_print += f'Total Operational Memory: {sum([comp.memory_consumption for comp in System._software])} / {sum([comp.memory for comp in System._hardware])}\n'
        to_print += f'Total Capacity Taken: {sum([comp.capacity_consumption for comp in System._software])} / {sum([comp.capacity for comp in System._hardware])}\n'
        return to_print

    @staticmethod
    def system_split():
        result = ""
        for h in System._hardware:
            result += f'Hardware Components - {h.name}'
            express_sofware_components = [s for s in h.software_components if s.__class__.__name__ == 'ExpressSoftware']
            result += f'Express Software Components: {len(express_sofware_components)}\n'
            light_sofware_components = [s for s in h.software_components if s.__class__.__name__ == 'LightSoftware']
            result += f'Express Software Components: {len(light_sofware_components)}\n'