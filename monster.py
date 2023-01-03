class Monster:
    possible_monsters = ['are goblins', 'are orcs', 'are ogres', 'are giants', 'is a dragon', 'is no monster']
    possible_hit_points = [1, 2, 3, 4, 5, 0]

    def __init__(self, index):
        self.monster_type = self.possible_monsters[index]
        self.monster_hp = self.possible_hit_points[index]
