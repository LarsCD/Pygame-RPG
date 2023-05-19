import logging
from dev.dev_logger import DevLogger
from data_loader import DataLoader
from entity import Entity
from sys import getsizeof
from game_main import Game_Main

class Core:
    def __init__(self):
        self.logger = DevLogger(Core)
        self.DataLoader = DataLoader()
        self.Entity = Entity()


    def start_game(self):
        # gets called before game starts
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


        game_metadata = ((1000, 600), 'fonts/dogicapixel.ttf', 'fonts/dogicapixelbold.ttf', 'white', 'gray', 'green')

        game = Game_Main(*game_metadata)
        game.main_menu_loop()


