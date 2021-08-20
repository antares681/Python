from Ex02_Movie_World.room import Room

class Hotel:
    def __init__(self, name:str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count:int):
        return cls(f"{stars_count} stars Hotel")

    def add_room(self, room:Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.take_room(people)
        if not result:
            self.guests += people

    def free_room(self, room_number):
        room = [r for r in self.rooms if r.number == room_number][0]
        result = room.free_room()
        if not result:
            self.guests -= self.guests

    def status(self):
        free_rooms = [r.number for r in self.rooms if not r.is_taken]
        taken_rooms = [r.number for r in self.rooms if r.is_taken]
        return f"Hotel {self.name} has {self.guests} total guests\n" \
        f"Free rooms: {', '.join(map(str, free_rooms))}\n" \
        f"Taken rooms: {', '.join(map(str, taken_rooms))}"
