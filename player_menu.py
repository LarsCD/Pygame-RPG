import pygame
import time
import logging
from assets.custom_pygame_assets import Lable, Health_bar, Custom_bar
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
        self.background = pygame.image.load("assets/images/player_menu_background.png")

        # PLAYER
        self.player_object = None

        # EQUIPED
        self.equiped_weapon_pos = (736, 304)
        self.equiped_armor_pos = (576, 304)
        self.equiped_helmet_pos = (576, 120)
        self.equiped_shield_pos = (416, 304)

        self.equiped_icon_size = (80, 80)
        self.background_color = (67, 67, 79)

        # ICON
        self.default_icon_size = (56, 56)
        self.tier_frame_pos = (128, 40)
        self.icon_pos = (130, 42)
        self.frame_pos = (128, 40)
        self.default_frame_size = (60, 60)

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

        icon = pygame.image.load(self.player_object.image).convert_alpha()
        icon_scaled = pygame.transform.scale(icon, self.default_icon_size)

        frame = pygame.image.load(self.player_object.frame).convert_alpha()
        frame_scaled = pygame.transform.scale(frame, self.default_frame_size)


        inventory_label = Lable(f'OPEN INVENTORY', 25, 'white', 'black', 'black',
                                ((900), (80)), bold_text=True, is_clickable=True)

        back_label = Lable('BACK', 20, 'white', 'gray', (153, 0, 28),
                           (930, 590), bold_text=True)

        health_bar = Health_bar(self.player_object.hp, self.player_object.hpMax, (64, 215), 220, 28,
                                (255, 0, 0), (194, 194, 209), title='HP ')
        energy_bar = Custom_bar(self.player_object.ep, self.player_object.epMax, (64, 250), 220, 28,
                                (255,178,0), (194, 194, 209), title='EP ')
        mana_bar = Custom_bar(self.player_object.mp, self.player_object.mpMax, (64, 285), 220, 28,
                              (23,93,255), (194, 194, 209), title='MP ')
        t2_main_loop_load = time.perf_counter()
        dt_main_loop_load = t2_main_loop_load-t1_main_loop_load
        self.log(logging.DEBUG, f'dt_main_loop_load: {round(dt_main_loop_load*1000, 3)}ms')

        self.build_inventory()

        while self.run_display:
            t7 = time.perf_counter()

            t1 = time.perf_counter()
            # self.ROOT.window.fill((64, 64, 64))   # <-- this bad boy adds 10ms of unnecessary shit >:(
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.ROOT.RESOLUTION), (0, 0)) # (performance cut: ~12ms)

            self.check_quit_event()

            self.build_static_text_lables()

            self.draw_static_text_labels()
            self.draw_dynamic_text_labels()

            # draw player icon (performance cut: ~0.01 ms)
            self.ROOT.window.blit(frame_scaled, self.frame_pos)
            self.ROOT.window.blit(icon_scaled, self.icon_pos)

            # draw health, energy and mana bars
            health_bar.update(self.ROOT.window, self.player_object.hp, self.player_object.hpMax)
            energy_bar.update(self.ROOT.window, self.player_object.ep, self.player_object.epMax)
            mana_bar.update(self.ROOT.window, self.player_object.mp, self.player_object.mpMax)


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
        between_space_y = 50
        black = (0, 0, 0)
        max_items_shown = 10
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
                    pos_y = inventory_start_pos_y + n*(self.text_size+5)

                    quantity = self.player_object.get_item_quantity(item.tag, item.item_type)

                    item_object = self.player_object.inventory[cat_name.lower()][index]
                    item_label = Lable(f'{item.name}', self.text_size, item.tier_color, 'white', 'gray',
                                       ((pos_x), (pos_y)), bold_text=True, is_clickable=True, class_method=self.Item_Display_Screen(self.ROOT).main_loop, method_args=(item_object))

                    quantity_label = Lable(f'x{quantity}', self.text_size, 'white', black, black,
                                           ((pos_x+offset_x), (pos_y)), bold_text=True, is_clickable=False)

                    self.dynamic_text_lables.append(item_label)
                    self.dynamic_text_lables.append(quantity_label)


    def build_static_text_lables(self):
        def_color = self.ROOT.lable_hover_col
        black = (0, 0, 0)
        # build static labels
        title_label = Lable(self.title, self.text_size, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (5, 5),
                            is_clickable=False)
        player_name = Lable(f'{str(self.player_object.player_name).upper()}', 23, 'white', black, black,
                            (self.name_pos_x, self.name_pos_y), is_clickable=False, bold_text=True)

        self.static_text_lables.append(title_label)
        self.static_text_lables.append(player_name)

        # self.build_metadata_labels()

    def draw_equiped_icons(self):

        # WEAPON
        if self.player_object.weapon_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color, (self.equiped_weapon_pos, self.equiped_icon_size))
            # WEAPON IMAGE
            weapon_icon = pygame.image.load(self.player_object.weapon_equiped.image).convert_alpha()
            weapon_icon_scaled = pygame.transform.scale(weapon_icon, self.equiped_icon_size)
            self.ROOT.window.blit(weapon_icon_scaled, self.equiped_weapon_pos)
            # WEAPON TIER FRAME
            weapon_frame = pygame.image.load(self.player_object.weapon_equiped.tier_icon).convert_alpha()
            weapon_frame_scaled = pygame.transform.scale(weapon_frame, self.equiped_icon_size)
            self.ROOT.window.blit(weapon_frame_scaled, self.equiped_weapon_pos)

        # ARMOR
        if self.player_object.armor_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color, (self.equiped_armor_pos, self.equiped_icon_size))
            # ARMOR IMAGE
            armor_icon = pygame.image.load(self.player_object.armor_equiped.image).convert_alpha()
            armor_icon_scaled = pygame.transform.scale(armor_icon, self.equiped_icon_size)
            self.ROOT.window.blit(armor_icon_scaled, (self.equiped_armor_pos[0] + 3, self.equiped_armor_pos[1]))
            # ARMOR TIER FRAME
            armor_frame = pygame.image.load(self.player_object.armor_equiped.tier_icon).convert_alpha()
            armor_frame_scaled = pygame.transform.scale(armor_frame, self.equiped_icon_size)
            self.ROOT.window.blit(armor_frame_scaled, self.equiped_armor_pos)

        # HELMET
        if self.player_object.helmet_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color, (self.equiped_helmet_pos, self.equiped_icon_size))
            # HELMET IMAGE
            helmet_icon = pygame.image.load(self.player_object.helmet_equiped.image).convert_alpha()
            helmet_icon_scaled = pygame.transform.scale(helmet_icon, self.equiped_icon_size)
            self.ROOT.window.blit(helmet_icon_scaled, (self.equiped_helmet_pos[0] + 3, self.equiped_helmet_pos[1]))
            # HELMET TIER FRAME
            helmet_frame = pygame.image.load(self.player_object.armor_equiped.tier_icon).convert_alpha()
            helmet_frame_scaled = pygame.transform.scale(helmet_frame, self.equiped_icon_size)
            self.ROOT.window.blit(helmet_frame_scaled, self.equiped_helmet_pos)

        # SHIELD
        if self.player_object.shield_equiped != None:
            pygame.draw.rect(self.ROOT.window, self.background_color,
                             (self.equiped_shield_pos, self.equiped_icon_size))
            # ARMOR IMAGE
            shield_icon = pygame.image.load(self.player_object.shield_equiped.image).convert_alpha()
            shield_icon_scaled = pygame.transform.scale(shield_icon, self.equiped_icon_size)
            self.ROOT.window.blit(shield_icon_scaled, (self.equiped_shield_pos[0] + 3, self.equiped_shield_pos[1]))
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

            attr_label = Lable(f'{attr}', self.text_size, self.ROOT.lable_hover_col, black, black,
                               (pos_x + offset_x, pos_y),
                               is_clickable=False)
            value_label = Lable(f'{value}', self.text_size, 'white', black, black,
                                (self.display_start_x_pos + self.display_sep_space + offset_x,
                                 self.display_start_y_pos + (n * (self.text_size + 5))), is_clickable=False)
            self.static_text_lables.append(attr_label)
            self.static_text_lables.append(value_label)
            n += 1
            m += 1


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
