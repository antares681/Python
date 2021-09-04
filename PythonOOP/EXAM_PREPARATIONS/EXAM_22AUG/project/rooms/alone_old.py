from project.rooms.room import Room


class AloneOld(Room):
    room_members_count = 1
    default_room_cost = 10
    def __init__(self, name, pension:float):
        super().__init__(name, pension, self.room_members_count)
        self.room_cost = self.default_room_cost

