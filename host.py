class Controller:
    keyword = ''

    def describe(self):
        for room in dungeon:
            if hero.x_coord == room.x_coord and hero.y_coord == room.y_coord:
                print(f'You find yourself in a {room.room_type}. Looking around, you see there'
                      f' {room.monster.monster_type} inside.')
                choice = input('What would you like to do? \n'
                               '1. Move to another room.\n'
                               '2. Fight the monster.\n'
                               '3. Look for treasure.\n'
                               '4. Search for relics.\n'
                               '5. Use item.\n').lower()
                if choice in '1' or choice in 'move to another room':
                    hero.movement()
                elif choice in '2' or choice in 'fight the monster':
                    host.fighting()
                elif choice in '3' or choice in 'look for treasure':
                    host.treasure_hunting()
                elif choice in '4' or choice in 'search for relics':
                    host.relic_hunting()
                elif choice in '5' or choice in 'use item':
                    host.use_item()

    def fighting(self):
        for room in dungeon:
            if room.active is True:
                room_index = dungeon.index(room)

        if dungeon[room_index].monster.monster_type != 'is no monster':
            hero.combat = True
            while hero.combat:
                print(f'The monster has {dungeon[room_index].monster.monster_hp} hp. \n'
                      f'Your stats are: \n'
                      f'Body: {hero.curr_body}\n'
                      f'Mind: {hero.curr_mind}\n'
                      f'Spirit: {hero.curr_spirit} \n')

                fight_or_flight = input('What would you like to do? \n'
                                        '1. Attack with Body \n'
                                        '2. Attack with Mind \n'
                                        '3. Attack with Spirit \n'
                                        '4. Run away \n').lower()

                attack_roll = random.randint(1, 6)
                if fight_or_flight in '1.' or 'body' in fight_or_flight:
                    if attack_roll < hero.curr_body:
                        dungeon[room_index].monster.monster_hp -= 1
                        if dungeon[room_index].monster.monster_hp < 1:
                            print('You killed the monster!')
                            dungeon[room_index].monster.monster_type = 'is no monster'
                            dungeon[room_index].monster.monster_hp = 0
                            hero.combat = False
                            host.describe()
                        else:
                            print(f'You hit! The monster now has {dungeon[room_index].monster.monster_hp} hp.')

                    else:
                        hero.curr_body -= 1
                        print('The monster swipes at you.')

                elif fight_or_flight in '2.' or 'mind.' in fight_or_flight:
                    if attack_roll < hero.curr_mind:
                        dungeon[room_index].monster.monster_hp -= 1
                        if dungeon[room_index].monster.monster_hp < 1:
                            print('You killed the monster!')
                            dungeon[room_index].monster.monster_type = 'is no monster'
                            dungeon[room_index].monster.monster_hp = 0
                            hero.combat = False
                            host.describe()
                        else:
                            print(f'You hit! The monster now has {dungeon[room_index].monster.monster_hp} hp.')

                    else:
                        hero.curr_mind -= 1
                        print('The monster outwits you.')

                elif fight_or_flight in '3.' or 'spirit.' in fight_or_flight:
                    if attack_roll < hero.curr_spirit:
                        dungeon[room_index].monster.monster_hp -= 1
                        if dungeon[room_index].monster.monster_hp < 1:
                            print('You killed the monster!')
                            dungeon[room_index].monster.monster_type = 'is no monster'
                            dungeon[room_index].monster.monster_hp = 0
                            hero.combat = False
                            host.describe()
                            hero.movement()
                        else:
                            print(f'You hit! The monster now has {dungeon[room_index].monster.monster_hp} hp.')

                    else:
                        hero.curr_spirit -= 1
                        print('The monster frightens you.')

                elif fight_or_flight in '4.' or 'run away' in fight_or_flight:
                    escaping = input('How would you like to escape? \n'
                                     '1. Push monster (Body) \n'
                                     '2. Distract the monster (Mind) \n'
                                     '3. Intimidate the monster (Spirit)'
                                     '4. Go back to fighting.').lower()

                    if escaping in '1. Push monster'.lower():
                        if hero.curr_body > dungeon[room_index].monster.monster_hp:
                            print('You shove the monster aside and make your way to a nearby room.')
                            dungeon[room_index].active = False
                            hero.combat = False
                            hero.movement()

                    elif escaping in '2. Distract the monster'.lower():
                        if hero.curr_mind > dungeon[room_index].monster.monster_hp:
                            print('You make a feint and leave the monster dumbfounded.')
                            dungeon[room_index].active = False
                            hero.combat = False
                            hero.movement()

                    elif escaping in '3. Intimidate the monster'.lower():
                        if hero.curr_spirit > dungeon[room_index].monster.monster_hp:
                            print('You let out a mighty roar and the monster is taken aback.')
                            dungeon[room_index].active = False
                            hero.combat = False
                            hero.movement()

                    elif escaping in '4. go back':
                        host.fighting()

                    else:
                        print("I don't understand.")
                        host.fighting()

        else:
            print('There is no monster in the room.')
            host.describe()
            hero.movement()

    def use_item(self):
        print(f'Your inventory contains: {hero.inventory} .')
        item_to_use = input('Which item would you like to use? To return to your adventures,'
                            ' simply type "Go back"').lower()
        if item_to_use in hero.inventory:
            if item_to_use in 'a healing potion':
                self.healing()

            elif item_to_use in 'a magic sword':
                print('You feel mighty when the hilt is in your hand. This blade has seen many battles.')
                host.describe()
            elif item_to_use in 'a tome of enlightenment':
                read = input('It is a tome containing long lost knowledge. Will you read it?')
                if read in 'yes':
                    hero.mind += 1
                    hero.curr_mind = hero.mind + 0
                    print('As you finish reading the tome it crumbles to dust in your hand.')

                '''a healing potion', 'a magic sword', 'a tome of enlightenment', 'a spell scroll', 'a map fragment'''
    def healing(self):
        print('You drink a healing potion. It has a soothing effect.')
        to_heal = input(f'Your stats are: \n 1. Body:  {hero.curr_body} \n 2. Mind: {hero.curr_mind} \n 3. Spirit: '
                        f'{hero.curr_spirit} \n 4. Go back').lower()

        if to_heal in '1.' or to_heal in 'body':
            hero.curr_body += 2
            if hero.curr_body > hero.body:
                hero.curr_body = hero.body
        elif to_heal in '2.' or to_heal in 'mind':
            hero.curr_mind += 2
            if hero.curr_mind > hero.mind:
                hero.curr_mind = hero.mind
        elif to_heal in '3.' or to_heal in 'spirit':
            hero.curr_spirit += 2
            if hero.curr_spirit > hero.spirit:
                hero.curr_spirit = hero.spirit
        elif to_heal in '4.' or to_heal in 'go back':
            self.use_item()
        else:
            print('I do not understand. Please choose again.')
            self.healing()

    def spellcasting(self):
        pass

    def treasure_hunting(self):
        print(f'You search around the room and find {dungeon[room_identifier()].treasure}.')
        hero.inventory.append(dungeon[room_identifier()].treasure)
        dungeon[room_identifier()].treasure = ' no treasure'
        host.describe()

    def relic_hunting(self):
        if dungeon[room_identifier()].room_type == 'vault' and 'a map fragment' in hero.inventory:
            relic_list = ['Jade Idol', 'Crystal Pendant', 'Boots of Swiftness', 'Puzzle Box', 'Sleeping Salts',
                          'Shielding Charm']
            relic_roll = random.randint(1, len(relic_list))
            relic = relic_list[relic_roll - 1]
            hero.inventory.append(relic)
            host.describe()
        else:
            print('Nothing points you to this room.')
            host.describe()
