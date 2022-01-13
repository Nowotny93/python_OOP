class Hotel:

    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, stars_count):
        return cls(f'{stars_count} stars Hotel')

    def add_room(self, room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for room in self.rooms:
            if room.number == room_number:
                result = room.take_room(people)
                if not result:
                    self.guests += people

    def free_room(self, room_number):
        for room in self.rooms:
            if room.number == room_number:
                self.guests -= room.guests
                room.free_room()

    def status(self):
        numbers_free_rooms = [r.number for r in self.rooms if not r.is_taken]
        numbers_taken_rooms = [r.number for r in self.rooms if r.is_taken]
        output = f'Hotel {self.name} has {self.guests} total guests\n'
        output += f'Free rooms: {", ".join(map(str, numbers_free_rooms))}\n'
        output += f'Taken rooms: {", ".join(map(str, numbers_taken_rooms))}'
        return output
