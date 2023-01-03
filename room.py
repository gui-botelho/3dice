from monster import Monster
import random


class Room:
    possible_rooms = ['corridor', 'small room', 'large room', 'vault', 'temple', 'great hall']
    possible_treasures = ['no treasure', 'a healing potion', 'a magic sword', 'a tome of enlightenment',
                          'a spell scroll',
                          'a map fragment']
    mapping = []

    def __init__(self, room_type=None, monster=None, treasure=None, x_coord=0, y_coord=0, room_xp=0, active=False,
                 room_coord=(0, 0)):
        self.room_type = room_type
        self.monster = monster
        self.treasure = treasure
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.room_xp = room_xp
        self.active = active
        self.room_coord = room_coord

    def roll_room(self):
        self.room_type = self.possible_rooms[random.randint(0, len(self.possible_rooms) - 1)]
        self.monster = Monster(random.randint(0, 5))
        self.treasure = self.possible_treasures[random.randint(0, len(self.possible_treasures) - 1)]

        if not dungeon:
            self.x_coord += 0
            self.y_coord += 0
            self.room_coord = (self.x_coord, self.y_coord)
            self.active = True
        else:
            mapping = [room.room_coord for room in dungeon]

            self.x_coord, self.y_coord = mapping[-1]
            north_or_east = random.randint(1, 3)
            if north_or_east == 1:
                self.y_coord += 1
                self.room_coord = (self.x_coord, self.y_coord)
                while self.room_coord in mapping:
                    self.x_coord += 1
                    self.room_coord = (self.x_coord, self.y_coord)
            elif north_or_east == 2:
                self.x_coord += 1
                self.room_coord = (self.x_coord, self.y_coord)
                while self.room_coord in mapping:
                    self.y_coord += 1
                    self.x_coord -= 1
                    self.room_coord = (self.x_coord, self.y_coord)
            else:
                self.y_coord -= 1
                self.room_coord = (self.x_coord, self.y_coord)
                while self.room_coord in mapping:
                    self.y_coord -= 1
                    self.x_coord += 1
                    self.room_coord = (self.x_coord, self.y_coord)
