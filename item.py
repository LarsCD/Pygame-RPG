import logging
import random
from dev.dev_logger import DevLogger

class Weapon:
    def __init__(self, metadata):
        # import modules
        self.Tier = Tier()
        # general metadata
        self.tag = metadata['tag']
        self.name = metadata['name']
        self.item_type = metadata['item_type']
        self.weapon_type = metadata['weapon_type']
        self.damage = metadata['damage']
        self.tier = metadata['tier']
        self.tier_tag = self.Tier.get_tier_tag(self.tier)
        self.tier_name = self.Tier.get_tier_name(self.tier)
        self.tier_color = self.Tier.get_tier_color(self.tier)
        self.value = metadata['value']
        self.is_stackable = metadata['is_stackable']
        self.id = 0
        self.is_equipped = False
        self.image = str(f'assets/images/weapons/{self.tag}.png')
        self.tier_icon = str(f'assets/images/tiers/{self.tier_tag}_tier_frame.png')

    def use(self):
        if self.isEquiped:
            return random.randint(self.damage[0], self.damage[1])
        else:
            logger = DevLogger(Weapon)
            logger.log(logging.WARNING, f'{self.tag} cannot be used and returned 0; self.equipped: {self.isEquiped}')
            return 0

class Potion:
    def __init__(self, metadata):
        # import modules
        self.Tier = Tier()
        # general metadata
        self.tag = metadata['tag']
        self.name = metadata['name']
        self.item_type = metadata['item_type']
        self.potion_type = metadata['potion_type']
        if self.potion_type == 'healing_potion':
            self.healing = metadata['healing']
        if self.potion_type == 'mana_potion':
            self.mana = metadata['mana']
        self.tier = metadata['tier']
        self.tier_tag = self.Tier.get_tier_tag(self.tier)
        self.tier_name = self.Tier.get_tier_name(self.tier)
        self.tier_color = self.Tier.get_tier_color(self.tier)
        self.value = metadata['value']
        self.is_stackable = metadata['is_stackable']
        self.is_empty = False
        self.id = 0
        self.is_equipped = False
        self.image = str(f'assets/images/potions/{self.tag}.png')
        self.tier_icon = str(f'assets/images/tiers/{self.tier_tag}_tier_frame.png')

    def use(self):
        if is_empty is not True:
            self.is_empty = True
            if self.potion_type == ['healing_potion']:
                return self.healing
            if self.potion_type == ['mana_potion']:
                return self.mana
        else:
            logger = DevLogger(Potion)
            logger.log(logging.WARNING, f'{self.tag} cannot be used; self.is_empty={self.is_empty})')



class Tier:
    def __init__(self):
        self.tier_tag_index = {
            1: 'common',
            2: 'uncommon',
            3: 'rare',
            4: 'super_rare',
            5: 'ultra_rare',
            6: 'legendary'
        }
        self.tier_name_index = {
            1: 'Common',
            2: 'Uncommon',
            3: 'Rare',
            4: 'Super Rare',
            5: 'Ultra Rare',
            6: 'Legendary'
        }
        self.tier_color_index = {
            1: (166, 166, 166),
            2: (143, 222, 93),
            3: (77, 166, 255),
            4: (171, 0, 255),
            5: (188, 0, 0),
            6: (255, 187, 0)
        }

    def get_tier_tag(self, tier_nr):
        return self.tier_tag_index[tier_nr]

    def get_tier_name(self, tier_nr):
        return self.tier_name_index[tier_nr]

    def get_tier_color(self, tier_nr):
        return self.tier_color_index[tier_nr]