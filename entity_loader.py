from enemy import Enemy
from item import Weapon, Potion
from player import Player

class Entity_Loader:
    def __init__(self):
        pass

    def create_enemy(self, metadata):
        enemy_object = Enemy(metadata)
        return enemy_object

    def create_item(self, metadata):
        if metadata['item_type'] == 'weapon':
            item_object = Weapon(metadata)
        if metadata['item_type'] == 'potion':
            item_object = Potion(metadata)
        return item_object

    def create_player(self, metadata):
        player_object = Player(**metadata)
        return player_object


