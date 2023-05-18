

class Player:
    def __init__(self, player_name: str, player_class_name: str, player_class_tag: str,
                 level: int, level_max: int, hp: int, hpMax: int, xp: int, xpMax: int, ep: int, epMax: int,
                 mp: int, mpMax: int, strength: int, agility: int, intelligence: int,
                 stealth: int, sorcery: int, hp_mult: float, xp_mult: float,
                 ep_mult: float, mp_mult: float, hpMax_mult: float, xpMax_mult: float,
                 epMax_mult: float, mpMax_mult: float):
        # GENERAL
        self.player_name = player_name
        self.player_class_name = player_class_name
        self.player_class_tag = player_class_tag
        # STATS
        self.level = level
        self.level_max = level_max
        self.hp = hp
        self.xp = xp
        self.ep = ep
        self.mp = mp
        self.hpMax = hpMax
        self.xpMax = xpMax
        self.epMax = epMax
        self.mpMax = mpMax
        # ATTRIBUTES
        self.strength = strength
        self.agility = agility
        self.intelligence = intelligence
        self.stealth = stealth
        self.sorcery = sorcery
        # STANDARD MULTIPLIERS
        self.hp_mult = hp_mult
        self.xp_mult = xp_mult
        self.ep_mult = ep_mult
        self.mp_mult = mp_mult
        # LEVEL-UP MULTIPLIERS
        self.hpMax_mult = hpMax_mult
        self.xpMax_mult = xpMax_mult
        self.epMax_mult = epMax_mult
        self.mpMax_mult = mpMax_mult
        # COMBAT FLAGS
        self.in_combat = False
        self.is_dead = False
        # LOADOUT
        self.weapon_equiped = None
        # INVENTORY
        self.inventory = {
            'weapon': []
        }
        self.inventory_cat_names = {
            'weapon': 'Weapons'
        }
        self.spells = {
            'attack_spell': []
        }
        self.spell_cat_names = {
            'attack_spell'
        }


    def give_item(self, item_object):
        if item_object.item_type == 'weapon':
            inventory['weapon'].update(item_object)


