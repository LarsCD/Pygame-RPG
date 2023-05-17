import logging
import random
from dev.dev_logger import DevLogger

class Weapon:
    def __init__(self, metadata):
        # general metadata
        self.tag = metadata['tag']
        self.name = metadata['name']
        self.item_type = metadata['item_type']
        self.weapon_type = metadata['weapon_type']
        self.damage = metadata['damage']
        self.tier = metadata['tier']
        self.value = metadata['value']
        self.stackable = metadata['stackable']
        self.isEquipped = False

    def use(self):
        if self.isEquiped:
            return random.randint(self.damage[0], self.damage[1])
        else:
            logger = DevLogger(Weapon)
            logger.log(logging.WARNING, f'{self.tag} used > returned 0; self.equipped: {self.isEquiped}')
            return 0
