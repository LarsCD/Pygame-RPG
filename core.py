import logging
from dev.dev_logger import DevLogger
from data_loader import DataLoader
from entity import Entity
from sys import getsizeof


class Core:
    def __init__(self):
        self.logger = DevLogger(Core)
        self.DataLoader = DataLoader()
        self.Entity = Entity()


    def update_game(self):
        # main update function
        item_data = {}
        player_data = {}

        self.logger.log(logging.INFO, 'update_game')
        enemy_data = self.DataLoader.load_data('data/enemy/enemy_data.json')
        weapon_data = self.DataLoader.load_data('data/items/weapon_data.json')

        player_class_data = self.DataLoader.load_data('data/player_classes/class_data.json')
        for class_data_struct in player_class_data:
            player_data.update(dict({class_data_struct: player_class_data[class_data_struct]}))

        class_data_size = getsizeof(player_data)
        player_object = self.Entity.create_player(player_data['sorcerer_class'])


        enemy_object_1 = self.Entity.create_enemy(enemy_data['placeholder_enemy'])
        enemy_object_2 = self.Entity.create_enemy(enemy_data['placeholder_enemy'])
        weapon_object_1 = self.Entity.create_weapon_item(weapon_data['enemy_weapons'][enemy_object_1.default_weapon])
        weapon_object_2 = self.Entity.create_weapon_item(weapon_data['enemy_weapons']['placeholder_weapon'])

        player_object.give_item(weapon_object_1)
        player_object.give_item(weapon_object_2)
        player_object.remove_item('placeholder_weapon', 'weapon')

        # enemy_object_1.equip_weapon(weapon_object)
        #
        # enemy_object_1.name = 'Enemy 1'
        # enemy_object_2.name  = 'Enemy 2'
        # enemy_object_1.level_up(20)
        # enemy_object_2.level_up(5)
        print(player_object.hp)
        player_object.take_damage(23)
        print(player_object.hp)
        player_object.heal(3)
        print(player_object.hp)
        player_object.heal_full()
        print(player_object.hp)
        player_object.take_damage(100)


