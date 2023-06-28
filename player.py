import logging
from dev.dev_logger import DevLogger

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
        self.armor_equiped = None
        self.helmet_equiped = None
        self.shield_equiped = None
        # INVENTORY
        self.inventory = {
            'weapon': [],
            'potion': [],
            'armor': [],
            'helmet': [],
            'shield': [],
            'key_item': [],
        }
        self.inventory_cat_names = {
            'weapon': 'Weapons',
            'potion': 'Potions',
            'armor': 'Armor',
            'helmet': 'Helmet',
            'shield': 'Shield',
            'key_item': 'Keys',
        }
        self.spells = {
            'attack_spell': []
        }
        self.spell_cat_names = {
            'Attack Spells'
        }
        # SPRITES
        self.image = str(f'assets/images/player_model/player_icon_{self.player_class_tag}.png')
        self.frame = str(f'assets/images/player_model/player_icon_frame_{self.player_class_tag}.png')
        # DEBUG
        self.logger = DevLogger(Player)


    # INVENTORY FUNCTIONS
    # TODO: make this more modular
    def give_item(self, item_object):
        if item_object.item_type == 'weapon':
            item_exists_in_inventory = False
            for inventory_item in self.inventory[item_object.item_type]:
                if inventory_item.tag == item_object.tag:
                    item_exists_in_inventory = True
                    break
            if not item_object.is_stackable and item_exists_in_inventory:
                self.logger.log(logging.WARNING, f'{item_object.tag} cannot be added to inventory player: {self.player_class_tag} (not stackable)')
                return
            else:
                self.inventory['weapon'].append(item_object)
                self.logger.log(logging.DEBUG, f'{item_object.tag} added to inventory player: {self.player_class_tag}')

        if item_object.item_type == 'potion':
            self.inventory['potion'].append(item_object)

        if item_object.item_type == 'armor':
            item_exists_in_inventory = False
            for inventory_item in self.inventory[item_object.item_type]:
                if inventory_item.tag == item_object.tag:
                    item_exists_in_inventory = True
                    break
            if not item_object.is_stackable and item_exists_in_inventory:
                self.logger.log(logging.WARNING, f'{item_object.tag} cannot be added to inventory player: {self.player_class_tag} (not stackable)')
                return
            else:
                self.inventory['armor'].append(item_object)
                self.logger.log(logging.DEBUG, f'{item_object.tag} added to inventory player: {self.player_class_tag}')

        if item_object.item_type == 'helmet':
            item_exists_in_inventory = False
            for inventory_item in self.inventory[item_object.item_type]:
                if inventory_item.tag == item_object.tag:
                    item_exists_in_inventory = True
                    break
            if not item_object.is_stackable and item_exists_in_inventory:
                self.logger.log(logging.WARNING, f'{item_object.tag} cannot be added to inventory player: {self.player_class_tag} (not stackable)')
                return
            else:
                self.inventory['helmet'].append(item_object)
                self.logger.log(logging.DEBUG, f'{item_object.tag} added to inventory player: {self.player_class_tag}')

        if item_object.item_type == 'shield':
            item_exists_in_inventory = False
            for inventory_item in self.inventory[item_object.item_type]:
                if inventory_item.tag == item_object.tag:
                    item_exists_in_inventory = True
                    break
            if not item_object.is_stackable and item_exists_in_inventory:
                self.logger.log(logging.WARNING, f'{item_object.tag} cannot be added to inventory player: {self.player_class_tag} (not stackable)')
                return
            else:
                self.inventory['shield'].append(item_object)
                self.logger.log(logging.DEBUG, f'{item_object.tag} added to inventory player: {self.player_class_tag}')



    def remove_item(self, item_tag, item_type):
        item_exists_in_inventory = False
        for inventory_item in self.inventory[item_type]:
            if inventory_item.tag == item_tag:
                item_exists_in_inventory = True
                break
        else:
            self.logger.log(logging.WARNING, f'{item_tag} cannot be removes to inventory player: {self.player_class_tag} (not in inventory)')
            return
        if item_exists_in_inventory:
            # to delete dictionary in list
            for index, inventory_item in enumerate(self.inventory[item_type]):
                if inventory_item.tag == item_tag:
                    del self.inventory[item_type][index]
                    self.logger.log(logging.DEBUG,f'{item_tag} removed from inventory player: {self.player_class_tag}')
                    break


    def get_item_quantity(self, item_tag, item_type):
        quantity = 0
        for item in self.inventory[item_type]:
            if item.tag == item_tag:
                quantity += 1
        return quantity

    def equip_first_weapon(self):
        self.weapon_equiped = self.inventory['weapon'][0]

    def equip_first_armor(self):
        self.armor_equiped = self.inventory['armor'][0]

    def equip_first_helmet(self):
        self.helmet_equiped = self.inventory['helmet'][0]

    def equip_first_shield(self):
        self.shield_equiped = self.inventory['shield'][0]


    # HEALTH FUNCTIONS
    def heal(self, healing):
        self.hp += healing
        if self.hp > self.hpMax:
            self.hp = self.hpMax
        self.logger.log(logging.DEBUG, f'player: {self.player_class_tag} healed (+{healing} hp)')

    def heal_full(self):
        hp_old = self.hp
        self.hp = self.hpMax
        hp_change = self.hpMax - hp_old
        self.logger.log(logging.DEBUG, f'player: {self.player_class_tag} fully healed')

    def take_damage(self, damage):
        self.hp -= damage
        self.logger.log(logging.DEBUG, f'player: {self.player_class_tag} took damage (-{damage} dmg)')
        if self.hp <= 0:
            self.die()

    def die(self):
        self.hp = 0
        self.is_dead = True
        self.logger.log(logging.DEBUG, f'player: {self.player_class_tag} died (hp: {self.hp})')


    # LEVEL UP FUNCTIONS
    def level_up(self, levels):
        for _ in range(levels):
            self.level_up_stats()

    def level_up_stats(self):
        self.level += 1

        hpMax_old = self.hpMax
        self.hpMax = round(self.hpMax * self.hpMax_mult)
        hpAdd = self.hpMax - hpMax_old
        self.hp += hpAdd

        xpMax_old = self.xpMax
        self.xpMax = round(self.xpMax * self.xpMax_mult)
        xpAdd = self.xpMax - xpMax_old
        self.xp += xpAdd

        epMax_old = self.epMax
        self.epMax = round(self.epMax * self.epMax_mult)
        epAdd = self.epMax - epMax_old
        self.ep += epAdd

        mpMax_old = self.mpMax
        self.mpMax = round(self.mpMax * self.mpMax_mult)
        epAdd = self.mpMax - mpMax_old
        self.mp += epAdd

