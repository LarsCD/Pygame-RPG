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
        data = self.DataLoader.load_data('data/items/dev_items.json')
        enemy_data = self.DataLoader.load_data('data/enemy/enemies.json')
        weapon_data = self.DataLoader.load_data('data/items/weapons.json')
        enemy_object = self.Entity.create_enemy(enemy_data['placeholder_enemy'])
        item_weapon_object = self.Entity.create_weapon_item(weapon_data['enemy_weapons']['placeholder_weapon'])
        print(f'enemy: {enemy_object.name}')
        enemy_object.equip_weapon(item_weapon_object)
        print(f'weapon: {item_weapon_object.name}')
        print(f'damage: {enemy_object.attack_weapon()}')
