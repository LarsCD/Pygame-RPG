import logging
import random
from dev.dev_logger import DevLogger
from entity_loader import Entity_Loader

class Level_Loader:
    def __init__(self, world_data):
        self.tag = world_data['tag']
        self.name = world_data['name']
        self.level = world_data['level']

        self.loot_init_data = self.init_loot_data(world_data['loot'])
        self.loot = []

        self.enemy_init_data = self.init_enemy_data(world_data['enemies'])
        self.enemies = []


    # generate loot_init_data, acts as raw data for later generation use
    def init_loot_data(self, loot_data):
        loot_init_data = []
        for cat in loot_data:
            for item in loot_data[cat]:
                loot_item_list.append(item)
        return loot_init_data


    # generate enemy_init_data, acts as raw data for later generation use
    def init_enemy_data(self, enemy_data):
        enemy_init_data = []
        for enemy in enemy_data:
            enemy_init_data.append(enemy)
        return enemy_init_data


    def generate_loot(self, static_item_data):
        loot_item_list = []
