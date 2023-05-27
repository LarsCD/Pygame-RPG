import pygame
import time
import logging
from assets.custom_pygame_assets import Lable, Health_bar, Custom_bar
from weapon_display_screen import Weapon_Display_Screen
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
        self.title = ''
        self.display_start_x_pos = 128
        self.display_start_y_pos = 120
        self.display_sep_space = 250
        self.text_size = 20
        self.name_pos_x = 145
        self.background = pygame.image.load("assets/image/menu_background_1.png")

        # PLAYER
        self.player_object = None

        # ICON
        self.default_icon_size = (56, 56)
        self.tier_frame_pos = (128, 40)
        self.icon_pos = (130, 42)
        self.frame_pos = (128, 40)
        self.default_frame_size = (60, 60)

        # MODULES
        self.Weapon_Display_Screen = Weapon_Display_Screen
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

        back_label = Lable('BACK', 20, 'white', 'gray', (153, 0, 28),
                           ((self.ROOT.DISPLAY_WIDTH / 2), 675),
                           is_centered=True)

        damage_button = Lable('DAMAGE PLAYER', 15, 'white', 'gray', 'red',
                           (625, 575))
        heal_button = Lable('HEAL PLAYER', 15, 'white', 'gray', 'green',
                              (625, 600))

        health_bar = Health_bar(self.player_object.hp, self.player_object.hpMax, (625, 470), 200, 25,
                                (255, 0, 0), (255, 255, 255), title='health')
        energy_bar = Custom_bar(self.player_object.ep, self.player_object.epMax, (625, 505), 200, 25,
                                (255,178,0), (255, 255, 255), title='energy')
        mana_bar = Custom_bar(self.player_object.mp, self.player_object.mpMax, (625, 540), 200, 25,
                              (23,93,255), (255, 255, 255), title='mana  ')
        t2_main_loop_load = time.perf_counter()
        dt_main_loop_load = t2_main_loop_load-t1_main_loop_load
        self.log(logging.DEBUG, f'dt_main_loop_load: {round(dt_main_loop_load*1000, 3)}ms')


        while self.run_display:
            t7 = time.perf_counter()

            t1 = time.perf_counter()
            # self.ROOT.window.fill((64, 64, 64))   # <-- this bad boy adds 10ms of unnecessary shit >:(
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.ROOT.RESOLUTION), (0, 0)) # (performance cut: ~12ms)

            # prepare static text labels and put in list (performance cut: ~3.0 ms)
            self.build_static_text_lables()
            # prepare static text labels for player inventory (performance cut: ~9.0 ms)
            self.build_inventory()

            # TODO: make function for background ^
            # check if quit window (performance cut: ~0.02 ms)
            self.check_quit_event()

            # draw all static text labels from list (performance cut: ~0.06 ms)
            self.draw_static_text_labels()

            # draw player icon (performance cut: ~0.01 ms)
            self.ROOT.window.blit(frame_scaled, self.frame_pos)
            self.ROOT.window.blit(icon_scaled, self.icon_pos)

            # draw health, energy and mana bars
            health_bar.update(self.ROOT.window, self.player_object.hp, self.player_object.hpMax)
            energy_bar.update(self.ROOT.window, self.player_object.ep, self.player_object.epMax)
            mana_bar.update(self.ROOT.window, self.player_object.mp, self.player_object.mpMax)

            # player interaction (performance cut: ~0.07 ms)
            if self.player_object.hp <= 0:
                self.player_object.heal_full()
            if damage_button.draw_text(self.ROOT.window):
                self.player_object.take_damage(10)
            if heal_button.draw_text(self.ROOT.window):
                self.player_object.heal(10)
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
        inventory_start_pos_x = 128
        inventory_start_pos_y = 170
        offset_y = 100
        offset_x = 400
        between_space_y = 100
        black = (0, 0, 0)

        inventory_title = Lable(f'INVENTORY', 35, 'white', black, black,
                                ((inventory_start_pos_x), (inventory_start_pos_y - 45)), is_clickable=False)
        self.static_text_lables.append(inventory_title)
        n = 0
        for i, cat_name in enumerate(self.player_object.inventory):
            n += 1
            item_tag_labels_build = []
            for item in self.player_object.inventory[cat_name]:
                if item.tag in item_tag_labels_build:
                    pass
                else:
                    n += 1
                    item_tag_labels_build.append(item.tag)
                    pos_x = inventory_start_pos_x
                    pos_y = inventory_start_pos_y + n*(self.text_size+5)

                    quantity = self.player_object.get_item_quantity(item.tag, item.item_type)

                    item_label = Lable(f'{item.name}', self.text_size, item.tier_color, black, black,
                                       ((pos_x), (pos_y)), is_clickable=False)

                    quantity_label = Lable(f'x{quantity}', self.text_size, 'white', black, black,
                                        ((pos_x+offset_x), (pos_y)), is_clickable=False)

                    self.static_text_lables.append(item_label)
                    self.static_text_lables.append(quantity_label)


    def build_static_text_lables(self):
        def_color = self.ROOT.lable_hover_col
        black = (0, 0, 0)
        # build static labels
        title_label = Lable(self.title, self.text_size, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (5, 5),
                            is_clickable=False)
        player_name = Lable(f'{str(self.player_object.player_name).upper()}', 35, 'white', black, black,
                            (self.name_pos_x + self.default_icon_size[1], 40), is_clickable=False)


        self.static_text_lables.append(title_label)
        self.static_text_lables.append(player_name)

        # self.build_metadata_labels()


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


    def set_background_color(self):
        if self.bg_color != None:
            self.ROOT.window.fill(self.bg_color)
        else:
            self.ROOT.window.fill(self.default_bg_color)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
