import pygame
import time
import logging
from assets.custom_pygame_assets import Label, Health_bar, Custom_bar
from item_display_screen import Item_Display_Screen
from player_inventory import Player_Inventory
from dev.dev_logger import DevLogger
from dev.dev_screen import DevScreen

class Player_Menu:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.ROOT.default_bg_color
        self.bg_color = self.ROOT.bg_color
        self.BLACK = (0, 0, 0)

        # SCENE LABELS
        self.static_text_lables = []
        self.dynamic_text_lables = []
        self.title = ''
        self.display_start_x_pos = 128
        self.display_start_y_pos = 120
        self.display_sep_space = 250
        self.text_size = 15
        self.name_pos_x = 105
        self.name_pos_y = 53
        self.background = pygame.image.load("assets/images/menu_background_1.png")

        self.attr_start_pos_x = 70
        self.attr_start_pos_y = 400

        self.bar_text_size = 28
        self.attr_text_size = 22

        self.item_text_size = 17

        # PLAYER
        self.player_object = None

        # EQUIPED
        self.equiped_weapon_pos = (727, 295)
        self.equiped_armor_pos = (567, 295)
        self.equiped_helmet_pos = (567, 111)
        self.equiped_shield_pos = (407, 295)

        self.equiped_icon_size = (98, 98)
        self.background_color = (67, 67, 79)

        # ICON
        self.default_icon_size = (80, 80)
        self.tier_frame_pos = (128, 40)
        self.icon_pos = (130, 42)
        self.frame_pos = (128, 40)
        self.default_frame_size = (88, 88)

        # MODULES
        self.Item_Display_Screen = Item_Display_Screen
        self.Player_Inventory = Player_Inventory
        self.log = DevLogger(Player_Menu).log
        self.DevScreen = DevScreen(self.ROOT)


    def main_loop(self, player_object):
        t1_main_loop_load = time.perf_counter()

        self.run_display = True
        self.static_text_lables = []
        self.player_object = player_object

        # icon = pygame.image.load(self.player_object.image).convert_alpha()
        # icon_scaled = pygame.transform.scale(icon, self.default_icon_size)
        #
        # frame = pygame.image.load(self.player_object.frame).convert_alpha()
        # frame_scaled = pygame.transform.scale(frame, self.default_frame_size)


        inventory_label = Label(f'OPEN INVENTORY', 25, 'white', 'black', 'black',
                                ((900), (80)), bold_text=True, is_clickable=True)

        back_label = Label('BACK', 20, 'white', 'gray', (153, 0, 28),
                           (930, 590), bold_text=True)

        health_bar = Health_bar(self.player_object.hp, self.player_object.hpMax, (64, 215), 220, self.bar_text_size,
                                (255, 0, 0), (194, 194, 209), title='HP ')
        energy_bar = Custom_bar(self.player_object.ep, self.player_object.epMax, (64, 250), 220, self.bar_text_size,
                                (255,178,0), (194, 194, 209), title='EP ')
        mana_bar = Custom_bar(self.player_object.mp, self.player_object.mpMax, (64, 285), 220, self.bar_text_size,
                              (23,93,255), (194, 194, 209), title='MP ')
        xp_bar = Custom_bar(self.player_object.xp, self.player_object.xpMax, (64, 320),
                            220, self.bar_text_size, (102, 255, 227), (194, 194, 209), title='XP ')

        t2_main_loop_load = time.perf_counter()
        dt_main_loop_load = t2_main_loop_load-t1_main_loop_load
        self.log(logging.DEBUG, f'dt_main_loop_load: {round(dt_main_loop_load*1000, 3)}ms')

        self.dynamic_text_lables = []
        self.build_inventory()

        while self.run_display:

            self.check_quit_event()

            self.build_static_text_lables()
            self.build_attr_labels()

            t1 = time.perf_counter()
            self.ROOT.window.fill((64, 64, 64))   # <-- this bad boy adds 10ms of unnecessary shit >:(
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.ROOT.RESOLUTION), (0, 0)) # (performance cut: ~12ms)

            self.draw_static_text_labels()
            self.draw_dynamic_text_labels()
            self.draw_equiped_icons()

            # draw player icon (performance cut: ~0.01 ms)
            # self.ROOT.window.blit(frame_scaled, self.frame_pos)
            # self.ROOT.window.blit(icon_scaled, self.icon_pos)

            # draw health, energy and mana bars
            health_bar.update(self.ROOT.window, self.player_object.hp, self.player_object.hpMax)
            energy_bar.update(self.ROOT.window, self.player_object.ep, self.player_object.epMax)
            mana_bar.update(self.ROOT.window, self.player_object.mp, self.player_object.mpMax)
            xp_bar.update(self.ROOT.window, self.player_object.xp, self.player_object.xpMax)


            # player interaction (performance cut: ~0.07 ms)
            if inventory_label.draw_text(self.ROOT.window):
                self.Player_Inventory(self.ROOT).main_loop(self.player_object)
            if back_label.draw_text(self.ROOT.window):
                # quit out of view
                self.run_display = False
            # TODO: make function for player interaction? (25-5-2023)

            # runs dev info in background, enable with [F1]
            self.DevScreen.main()

            # update screen
            pygame.display.update()
            self.ROOT.clock.tick(self.ROOT.fps)

    # build static labels for whole inventory
    def build_inventory(self):

        inventory_start_pos_x = 900
        inventory_start_pos_y = 120
        offset_y = 100
        offset_x = 300
        between_space_y = 60

        max_items_shown = 10
        max_item_name_len = 16

        n = 0
        item_count = 0

        for i, cat_name in enumerate(self.player_object.inventory):
            n += 1
            item_tag_labels_build = []
            for index, item in enumerate(self.player_object.inventory[cat_name]):
                if item_count >= max_items_shown:
                    return
                if item.tag in item_tag_labels_build:
                    pass
                else:
                    item_count += 1
                    n += 1
                    item_tag_labels_build.append(item.tag)
                    pos_x = inventory_start_pos_x
                    pos_y = inventory_start_pos_y + n*(self.item_text_size+5)

                    quantity = self.player_object.get_item_quantity(item.tag, item.item_type)

                    # format item name to not be too long
                    ITEM_NAME = item.name
                    if len(item.name) >= max_item_name_len:
                        ITEM_NAME = str(item.name[:max_item_name_len]+'...')

                    item_object = self.player_object.inventory[cat_name.lower()][index]
                    item_label = Label(f'{ITEM_NAME}', self.item_text_size, item.tier_color, 'white', 'gray',
                                       ((pos_x), (pos_y)), bold_text=True, is_clickable=True, class_method=self.Item_Display_Screen(self.ROOT).main_loop, method_args=(item_object))

                    quantity_label = Label(f'x{quantity}', self.item_text_size, 'white', 'black', 'black',
                                           ((pos_x+offset_x), (pos_y)), bold_text=True, is_clickable=False)

                    self.dynamic_text_lables.append(item_label)
                    self.dynamic_text_lables.append(quantity_label)


    def build_static_text_lables(self):
        def_color = self.ROOT.lable_hover_col
        black = (0, 0, 0)
        # build static labels
        title_label = Label(self.title, self.text_size, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (5, 5),
                            is_clickable=False)
        player_name = Label(f'{str(self.player_object.player_name).upper()}', 23, 'white', black, black,
                            (self.name_pos_x, self.name_pos_y), is_clickable=False, bold_text=True)

        self.static_text_lables.append(title_label)
        self.static_text_lables.append(player_name)

        # self.build_metadata_labels()

    def draw_equiped_icons(self):

        # WEAPON
        offsetXY = 10
        if self.player_object.weapon_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color, (self.equiped_weapon_pos, self.equiped_icon_size))
            # WEAPON IMAGE
            weapon_icon = pygame.image.load(self.player_object.weapon_equiped.image).convert_alpha()
            weapon_icon_scaled = pygame.transform.scale(weapon_icon, (self.equiped_icon_size[0]-offsetXY, self.equiped_icon_size[1]-offsetXY))
            self.ROOT.window.blit(weapon_icon_scaled, (self.equiped_weapon_pos[0]+int(offsetXY/2), self.equiped_weapon_pos[1]+int(offsetXY/2)))
            # WEAPON TIER FRAME
            weapon_frame = pygame.image.load(self.player_object.weapon_equiped.tier_icon).convert_alpha()
            weapon_frame_scaled = pygame.transform.scale(weapon_frame, self.equiped_icon_size)
            self.ROOT.window.blit(weapon_frame_scaled, self.equiped_weapon_pos)

        # ARMOR
        if self.player_object.armor_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color, (self.equiped_armor_pos, self.equiped_icon_size))
            # ARMOR IMAGE
            armor_icon = pygame.image.load(self.player_object.armor_equiped.image).convert_alpha()
            armor_icon_scaled = pygame.transform.scale(armor_icon, (self.equiped_icon_size[0]-offsetXY, self.equiped_icon_size[1]-offsetXY))
            self.ROOT.window.blit(armor_icon_scaled, (self.equiped_armor_pos[0]+int(offsetXY/2), self.equiped_armor_pos[1]+int(offsetXY/2)))
            # ARMOR TIER FRAME
            armor_frame = pygame.image.load(self.player_object.armor_equiped.tier_icon).convert_alpha()
            armor_frame_scaled = pygame.transform.scale(armor_frame, self.equiped_icon_size)
            self.ROOT.window.blit(armor_frame_scaled, self.equiped_armor_pos)

        # HELMET
        if self.player_object.helmet_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color, (self.equiped_helmet_pos, self.equiped_icon_size))
            # HELMET IMAGE
            helmet_icon = pygame.image.load(self.player_object.helmet_equiped.image).convert_alpha()
            helmet_icon_scaled = pygame.transform.scale(helmet_icon, (self.equiped_icon_size[0]-offsetXY, self.equiped_icon_size[1]-offsetXY))
            self.ROOT.window.blit(helmet_icon_scaled, (self.equiped_helmet_pos[0]+int(offsetXY/2), self.equiped_helmet_pos[1]+int(offsetXY/2)))
            # HELMET TIER FRAME
            helmet_frame = pygame.image.load(self.player_object.helmet_equiped.tier_icon).convert_alpha()
            helmet_frame_scaled = pygame.transform.scale(helmet_frame, self.equiped_icon_size)
            self.ROOT.window.blit(helmet_frame_scaled, self.equiped_helmet_pos)

        # SHIELD
        if self.player_object.shield_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color,
                             (self.equiped_shield_pos, self.equiped_icon_size))
            # ARMOR IMAGE
            shield_icon = pygame.image.load(self.player_object.shield_equiped.image).convert_alpha()
            shield_icon_scaled = pygame.transform.scale(shield_icon, (self.equiped_icon_size[0]-offsetXY, self.equiped_icon_size[1]-offsetXY))
            self.ROOT.window.blit(shield_icon_scaled, (self.equiped_shield_pos[0]+int(offsetXY/2), self.equiped_shield_pos[1]+int(offsetXY/2)))
            # ARMOR TIER FRAME
            shield_frame = pygame.image.load(self.player_object.shield_equiped.tier_icon).convert_alpha()
            shield_frame_scaled = pygame.transform.scale(shield_frame, self.equiped_icon_size)
            self.ROOT.window.blit(shield_frame_scaled, self.equiped_shield_pos)


    def build_metadata_labels(self):
        # make label for every attribute of weapon object (cluttered asf I know..)
        n = 0
        m = 0
        black = (0, 0, 0)
        for attr, value in self.player_object.__dict__.items():
            row_length = 26
            offset_x = 0
            if m >= row_length:
                n = m - row_length
                offset_x = self.display_sep_space * 2
            offset_y = 5

            pos_x = self.display_start_x_pos
            pos_y = self.display_start_y_pos + (n * (self.text_size + offset_y))

            attr_label = Label(f'{attr}', self.text_size, self.ROOT.lable_hover_col, black, black,
                               (pos_x + offset_x, pos_y),
                               is_clickable=False)
            value_label = Label(f'{value}', self.text_size, 'white', black, black,
                                (self.display_start_x_pos + self.display_sep_space + offset_x,
                                 self.display_start_y_pos + (n * (self.text_size + 5))), is_clickable=False)
            self.static_text_lables.append(attr_label)
            self.static_text_lables.append(value_label)
            n += 1
            m += 1

    def build_attr_labels(self):
        strg_label = Label(f'STRENGTH', self.attr_text_size, 'gray', 'black', 'black',
                           (self.attr_start_pos_x, self.attr_start_pos_y), is_clickable=False, bold_text=True)
        agil_label = Label(f'AGILITY', self.attr_text_size, 'gray', 'black', 'black',
                           (self.attr_start_pos_x, self.attr_start_pos_y + 25), is_clickable=False, bold_text=True)
        intl_label = Label(f'INTELIGENCE', self.attr_text_size, 'gray', 'black', 'black',
                           (self.attr_start_pos_x, self.attr_start_pos_y + 50), is_clickable=False, bold_text=True)
        slth_label = Label(f'STEALTH', self.attr_text_size, 'gray', 'black', 'black',
                           (self.attr_start_pos_x, self.attr_start_pos_y + 75), is_clickable=False, bold_text=True)
        sorc_label = Label(f'SORCERY', self.attr_text_size, 'gray', 'black', 'black',
                           (self.attr_start_pos_x, self.attr_start_pos_y + 100), is_clickable=False, bold_text=True)

        sep_space = 250
        strg_value_label = Label(f'{self.player_object.strength}', self.attr_text_size, 'white', 'black', 'black',
                                 (self.attr_start_pos_x + sep_space, self.attr_start_pos_y), is_clickable=False, bold_text=True)
        agil_value_label = Label(f'{self.player_object.agility}', self.attr_text_size, 'white', 'black', 'black',
                                 (self.attr_start_pos_x + sep_space, self.attr_start_pos_y + 25), is_clickable=False, bold_text=True)
        intl_value_label = Label(f'{self.player_object.intelligence}', self.attr_text_size, 'white', 'black', 'black',
                                 (self.attr_start_pos_x + sep_space, self.attr_start_pos_y + 50), is_clickable=False, bold_text=True)
        slth_value_label = Label(f'{self.player_object.stealth}', self.attr_text_size, 'white', 'black', 'black',
                                 (self.attr_start_pos_x + sep_space, self.attr_start_pos_y + 75), is_clickable=False, bold_text=True)
        sorc_value_label = Label(f'{self.player_object.sorcery}', self.attr_text_size, 'white', 'black', 'black',
                                 (self.attr_start_pos_x + sep_space, self.attr_start_pos_y + 100), is_clickable=False, bold_text=True)

        self.static_text_lables.append(strg_label)
        self.static_text_lables.append(agil_label)
        self.static_text_lables.append(intl_label)
        self.static_text_lables.append(slth_label)
        self.static_text_lables.append(sorc_label)
        self.static_text_lables.append(strg_value_label)
        self.static_text_lables.append(agil_value_label)
        self.static_text_lables.append(intl_value_label)
        self.static_text_lables.append(slth_value_label)
        self.static_text_lables.append(sorc_value_label)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)
        self.static_text_lables = []

    def draw_dynamic_text_labels(self):
        for label in self.dynamic_text_lables:
            label.draw_text(self.ROOT.window)

    def set_background_color(self):
        if self.bg_color != None:
            self.ROOT.window.fill(self.bg_color)
        else:
            self.ROOT.window.fill(self.default_bg_color)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
