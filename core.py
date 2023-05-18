import logging
from dev.dev_logger import DevLogger
from data_loader import DataLoader
from entity import Entity


class Core:
    def __init__(self):
        self.logger = DevLogger(Core)
        self.DataLoader = DataLoader()
        self.Entity = Entity()

    def update_game(self):
        # main update function
        self.logger.log(logging.INFO, 'update_game')
        enemy_data = self.DataLoader.load_data('data/enemy/enemies.json')
        weapon_data = self.DataLoader.load_data('data/items/weapons.json')

        enemy_object_1 = self.Entity.create_enemy(enemy_data['placeholder_enemy'])
        enemy_object_2 = self.Entity.create_enemy(enemy_data['placeholder_enemy'])
        weapon_object = self.Entity.create_weapon_item(weapon_data['enemy_weapons'][enemy_object_1.default_weapon])

        enemy_object_1.equip_weapon(weapon_object)

        enemy_object_1.name = 'Enemy 1'
        enemy_object_2.name  = 'Enemy 2'
        enemy_object_1.level_up(20)
        enemy_object_2.level_up(5)
