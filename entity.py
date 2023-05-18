from enemy import Enemy
from item import Weapon
from player import Player

class Entity:
    def __init__(self):
        pass

    def create_enemy(self, metadata):
        enemy_object = Enemy(metadata)
        return enemy_object

    def create_weapon_item(self, metadata):
        item_weapon_object = Weapon(metadata)
        return item_weapon_object

    def create_player(self, metadata):
        player_object = Player(**metadata)
        return player_object


