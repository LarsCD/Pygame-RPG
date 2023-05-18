import random

class Enemy:
    def __init__(self, metadata):
        # general metadata
        self.tag = metadata['tag']
        self.name = metadata['name']
        self.type = metadata['type']
        # level up data
        self.level = 0
        self.hpMax_multiplier = metadata['level_up_multipliers']['hpMax_multiplier']
        self.atk_m_multiplier = metadata['level_up_multipliers']['atk_m_multiplier']
        # stats data
        self.hp = metadata['base_stats']['hpMax']
        self.hpMax = self.hp
        self.atk = metadata['base_stats']['atk']
        # stat multipliers
        self.atk_multiplier = metadata['stat_multipliers']['atk_multiplier']
        # states
        self.state_alive = True
        # inventory data
        self.default_weapon = metadata['default_weapon']
        self.weapon_equipped = None

    # config
    def default_config(self):
        self.hp = self.hpMax


    # inventory methods
    def equip_weapon(self, item_weapon_object):
        item_weapon_object.isEquiped = True
        self.weapon_equipped = item_weapon_object

    def unequip_weapon(self):
        self.weapon_equipped = None


    # level methods
    def level_up(self, levels):
        for _ in range(levels):
            self.level_up_stats()

    def level_up_stats(self):
        self.level += 1
        hpMax_old = self.hpMax
        self.hpMax = round(self.hpMax*self.hpMax_multiplier)
        hpAdd = self.hpMax-hpMax_old
        self.hp += hpAdd
        self.atk_multiplier *= self.atk_m_multiplier


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
        if self.weapon_equipped == None:
            damage = self.attack_bare()
        else:
            damage = round(self.weapon_equipped.use()*self.atk_multiplier)
        return damage





