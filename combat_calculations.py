import random

class Calculations:
    def __init__(self):
        pass


    def damage(self, player_level, weapon_power, strength, target_armor, critical):
        R = random.uniform(0.9, 1.1)
        damage = (((((2*player_level)/5)+2)*weapon_power*((strength*10)/(target_armor)/10)/50)*critical+2)*R
        return damage


    def XP(self, enemy_level, player_level, enemy_difficulity, game_difficulity):
        XP = ((enemy_level/player_level)/(game_difficulity*3.5))*enemy_difficulity*1100
        return XP