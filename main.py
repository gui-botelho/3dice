from player import Player
from host import Controller
from room import Room
from handler import Dungeon


def game_loop():
    playing = True
    hero = Player()
    hero.roll_stats()
    dungeon = []

    def generate_dungeon(max_rooms):
        for slot in range(max_rooms):
            temp_room =


'''def staring_game():
    playing = True
    hero = Player()
    hero.roll_stats()
    dungeon = Dungeon.rooms
    host = Controller()

    def room_identifier():
        for room in dungeon:
            if room.active:
                room_index = dungeon.index(room)
        return room_index

    def generate_dungeon(number_of_rooms):
        for i in range(number_of_rooms):
            temp_room = Room()
            temp_room.roll_room()
            dungeon.append(temp_room)

    generate_dungeon(10)
    while playing:
        print(f'You are an adventurer, in such of fame and fortune.\n'
              f'You have come to this dungeon, carrying naught but {hero.inventory[0]}.\n')
        entry = input('Will you dare brave this dungeon, slay the monsters within and claim the forgotten '
                      'treasures?\n').lower()
        if entry in 'yes.':
            host.describe()
        elif entry in 'no.':
            print('You return home, empty handed and ashamed.\n')
            a = input('Press enter to exit.')
            playing = False
        else:
            print('I do not understand.\n')


staring_game()
'''
