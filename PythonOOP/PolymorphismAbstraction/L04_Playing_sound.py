class Guitar:
    def play(self):
        return "Playing the guitar"

class Children:
    def play(self):
        return "Children are playing"


def start_playing(insturment):
    return insturment.play()

children = Children()
print(start_playing(children))

guitar = Guitar()
print(start_playing(guitar))
