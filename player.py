import random
from host import Controller


class Player:
    def __init__(self, spirit=0, mind=0, body=0, curr_spirit=0, curr_mind=0, curr_body=0,
                 inventory=['a healing potion'], current_xp=0, current_level=0, combat=False, x_coord=0, y_coord=0):
        self.spirit = spirit
        self.mind = mind
        self.body = body
        self.curr_spirit = curr_spirit
        self.curr_mind = curr_mind
        self.curr_body = curr_body
        self.inventory = inventory
        self.current_xp = current_xp
        self.current_level = current_level
        self.combat = combat
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.location = (self.x_coord , self.y_coord)

    def roll_stats(self):
        while self.spirit + self.mind + self.body < 10:
            self.spirit = random.randint(1, 6)
            self.mind = random.randint(1, 6)
            self.body = random.randint(1, 6)
            self.curr_spirit = self.spirit
            self.curr_mind = self.mind
            self.curr_body = self.body

    def level_up(self):
        if self.current_xp > 50:

            print('You have earned enough experience to level up. Your stats are restored.')
            self.curr_mind = 0 + self.mind
            self.curr_spirit = 0 + self.spirit
            self.curr_body = 0 + self.body

            print(f'Your stats are: \n Spirit = {self.spirit} \n Mind = {self.mind} \n Body = {self.body} \n ')
            leveling = input('Which skill would you like to increase by one point?').lower()
            if leveling == 'spirit':
                self.spirit += 1
                self.curr_spirit = 0 + self.spirit
                print(f'You feel your resolve strengthen. Your spirit is now {self.curr_spirit}\n')
                self.current_level += 1
                self.current_xp -= 50
            elif leveling == 'mind':
                self.mind += 1
                self.curr_mind = 0 + self.mind
                print(f'You notice your reaction speed grow. Your mind is now {self.curr_mind}\n')
                self.current_level += 1
                self.current_xp -= 50
            elif leveling == 'body':
                self.body += 1
                self.curr_body = 0 + self.body
                print(f'Your muscles are adjusting to the effort. Your body is now {self.curr_body}\n')
                self.current_level += 1
                self.current_xp -= 50
            else:
                print('I do not understand. Choose a skill to level up.')
                self.level_up()

    def death(self):
        if self.curr_body < 1 and self.curr_mind < 1 and self.curr_spirit < 1:
            print('Another adventurer has fallen on the path to glory.')

    def combat(self):
        pass

    def movement(self):
        player_mapping = [room.room_coord for room in dungeon]
        direction = input('Where would you like to move?').lower()
        if direction in 'up.' or direction in 'north.':
            self.y_coord += 1
            pl_coord = (self.x_coord, self.y_coord)
            if pl_coord in player_mapping:
                dungeon[player_mapping.index(pl_coord)].active = True
                host.describe()

            else:
                self.y_coord -= 1
                print('There is no door leading in that direction.')
                self.movement()

        elif direction in 'right.' or direction in 'east.':
            self.x_coord += 1
            pl_coord = (self.x_coord, self.y_coord)
            if pl_coord in player_mapping:
                dungeon[player_mapping.index(pl_coord)].active = True
                host.describe()

            else:
                self.x_coord -= 1
                print('There is no door leading in that direction.')
                self.movement()

        elif direction in 'down.' or direction in 'south.':
            self.y_coord -= 1
            pl_coord = (self.x_coord, self.y_coord)
            if pl_coord in player_mapping:
                dungeon[player_mapping.index(pl_coord)].active = True
                host.describe()

            else:
                self.y_coord += 1
                print('There is no door leading in that direction.')
                self.movement()

        elif direction in 'left.' or direction in 'west.':
            self.x_coord -= 1
            pl_coord = (self.x_coord, self.y_coord)
            if pl_coord in player_mapping:
                dungeon[player_mapping.index(pl_coord)].active = True
                host.describe()

            else:
                self.x_coord += 1
                print('There is no door leading in that direction.')
                self.movement()
