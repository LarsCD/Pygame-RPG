import random

class Enemy:
    def __init__(self, metadata):
        # general metadata
        self.tag = metadata['tag']
        self.name = metadata['name']
        self.type = metadata['type']
        # stats data
        self.hp = metadata['base_stats']['hpMax']
        self.hpMax = self.hp
        self.atk = metadata['base_stats']['atk']
        self.state_alive = True
        # inventory data
        self.weapon_equiped = None

    # inventory methods
    def equip_weapon(self, item_weapon_object):
        item_weapon_object.isEquiped = True
        self.weapon_equiped = item_weapon_object

    def unequip_weapon(self):
        self.weapon_equiped = None

    # health methods
    def heal(self, healing):
        self.hp += healing
        if self.hp > self.hpMax:
            self.hp = self.hpMax

    def heal_full(self):
        self.hp = self.hpMax

    def take_damage(self, damage):
        self.hp -= damage
        if self.hp <= 0:
            self.die()

    def die(self):
        self.hp = 0
        self.state_alive = False

    # combat methods
    def attack_bare(self):
        damage = random.randint(self.atk[0], self.atk[1])
        return damage

    def attack_weapon(self):
        damage = self.weapon_equiped.use()
        return damage





