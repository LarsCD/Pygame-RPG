import logging
import time
from random import uniform, randint

from dev.dev_logger import DevLogger
from entity_loader import Entity_Loader


class Level:
    def __init__(self, world_data):
        self.tag = world_data['tag']
        self.name = world_data['name']
        self.level = world_data['level']

        self.loot_init_data = self.init_loot_data(world_data['loot'])
        self.loot = []

        self.enemy_init_data = self.init_enemy_data(world_data['enemies'])
        self.enemies = []

        self.path_connections = world_data['path_connections']
        self.is_current_location = False   # is player in this level

        # data
        self.is_loaded = False
        self.no_enemies = False
        self.no_items = False

        # modules
        self.Entity_Loader = Entity_Loader()

        # dev tools
        self.log = DevLogger(Level).log

    # generate loot_init_data, acts as raw data for later generation use
    def init_loot_data(self, loot_data):
        loot_init_data = []
        for category in loot_data:
            for item in loot_data[category]:
                loot_init_data.append(item)
        return loot_init_data

    # generate enemy_init_data, acts as raw data for later generation use
    def init_enemy_data(self, enemy_data):
        enemy_init_data = []
        for enemy in enemy_data:
            enemy_init_data.append(enemy)
        return enemy_init_data

    # generate item objects from loot_init_data
    def generate_loot(self, static_item_data):
        t1 = time.perf_counter()
        category_data_index = {
            "weapons": "weapon_data",
            "healing_potions": "potion_data",
            "mana_potions": "potion_data"
        }
        for item in self.loot_init_data:
            for _ in range(item['quantity']):
                if item['chance'] >= uniform(0, 1):
                    category = category_data_index[item['category']]
                    item_object = self.Entity_Loader.create_item(static_item_data[category][item['category']][item['tag']])
                    self.loot.append(item_object)

        t2 = time.perf_counter()
        dt = t2-t1
        self.log(logging.INFO, f'{self.tag}: generated loot ({round(dt*1000, 2)} ms)')

    # generate enemy objects from enemy_init_data
    def generate_enemies(self, static_enemy_data):
        t1 = time.perf_counter()
        category_data_index = {
            "enemy": "enemy_data",
            "enemy_boss": "enemy_boss_data",
        }
        for enemy in self.enemy_init_data:
            for _ in range(enemy['quantity']):
                category = category_data_index[enemy['category']]
                enemy_object = self.Entity_Loader.create_enemy(static_enemy_data[category][enemy['tag']])
                enemy_object.level_up(randint(enemy['level'][0], enemy['level'][1]))
                self.enemies.append(enemy_object)

        t2 = time.perf_counter()
        dt = t2-t1
        self.log(logging.INFO, f'{self.tag}: generated enemies ({round(dt*1000, 2)} ms)')


    def load_level(self, static_item_data, static_enemy_data):
        self.log(logging.INFO, f'{self.tag}: loading level...')
        t1 = time.perf_counter()

        self.generate_loot(static_item_data)
        self.generate_enemies(static_enemy_data)
        self.is_loaded = True

        t2 = time.perf_counter()
        dt = t2 - t1
        self.log(logging.INFO, f'{self.tag}: loaded ({round(dt * 1000, 2)} ms)')


    # ATTRIBUTES

    # enter the level (set self.is_current_location = True)
    def enter_level(self):
        if not self.is_loaded:
            self.log(logging.WARNING, f'{self.tag}: could not be entered; level is not loaded! (self.loaded={self.is_loaded})')
        else:
            self.is_current_location = True

    def search(self):
        pass
