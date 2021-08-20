class Integer:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_float(float_value):
        if type(float_value) is float:
            return float_value
        return 'wrong type'

    @staticmethod
    def from_roman(value):
        pass

    @staticmethod
    def from_string(value):
        if type(value) is str:
            return value
        return 'wrong type'