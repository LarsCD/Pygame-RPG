from enemy import Enemy
from item import *
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
        if metadata['item_type'] == 'armor':
            item_object = Armor(metadata)
        if metadata['item_type'] == 'helmet':
            item_object = Helmet(metadata)
        if metadata['item_type'] == 'shield':
            item_object = Shield(metadata)
        return item_object

    def create_player(self, metadata):
        player_object = Player(**metadata)
        return player_object


