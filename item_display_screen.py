import pygame
import logging

from assets.custom_pygame_assets import Lable
from dev.dev_logger import DevLogger
from dev.dev_screen import DevScreen

class Item_Display_Screen:
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
        self.display_sep_space = 300
        self.text_size = 15
        self.name_pos_x = 135
        self.background = pygame.image.load("assets/images/item_background_1.png")

        # ITEM
        self.weapon_object = None

        # ICON
        self.default_icon_size = (64, 64)
        self.tier_frame_pos = (128, 40)
        self.icon_pos = (130, 42)
        self.default_frame_size = (60, 60)
        self.tier_name_pos_y = 80

        # MODULES
        self.DevLogger = DevLogger(Item_Display_Screen)
        self.DevScreen = DevScreen(self.ROOT)


    def main_loop(self, weapon_object):
        self.static_text_lables = []
        self.weapon_object = weapon_object
        # self.title = f'Viewing {weapon_object.name}'
        self.run_display = True
        self.build_static_text_lables()

        back_label = Lable('BACK', 20, 'white', 'gray', (153, 0, 28),
                           ((self.ROOT.DISPLAY_WIDTH / 2), (self.ROOT.DISPLAY_HEIGHT / 2) + 240),
                           is_centered=True, is_clickable=True)

        icon = pygame.image.load(self.weapon_object.image).convert_alpha()
        tier_frame = pygame.image.load(self.weapon_object.tier_icon).convert_alpha()

        icon_scaled = pygame.transform.scale(icon, self.default_icon_size)
        tier_frame_scaled = pygame.transform.scale(tier_frame, self.default_frame_size)


        while self.run_display:
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.ROOT.RESOLUTION), (0, 0))
            self.check_quit_event()
            # self.set_background_color()
            self.draw_static_text_labels()

            # draw item icon and tier frame
            self.ROOT.window.blit(icon_scaled, self.icon_pos)
            # self.ROOT.window.blit(tier_frame_scaled, self.tier_frame_pos)

            if back_label.draw_text(self.ROOT.window):
                # quit out of view
                self.run_display = False

            # dev
            self.DevScreen.main()

            pygame.display.update()
            self.ROOT.clock.tick(self.ROOT.fps)


    def set_background_color(self):
        if self.bg_color != None:
            self.ROOT.window.fill(self.bg_color)
        else:
            self.ROOT.window.fill(self.default_bg_color)


    def build_static_text_lables(self):
        def_color = self.ROOT.lable_hover_col
        black = (0, 0, 0)
        # build static labels
        title_label = Lable(self.title, self.text_size, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (5, 5),
                            is_clickable=False)
        weapon_name = Lable(f'{str(self.weapon_object.name).upper()}', 35, 'white', black, black,
                            (self.name_pos_x + self.default_icon_size[1], 40), is_clickable=False)
        tier_text = Lable(str(self.weapon_object.tier_name).upper(), 20, self.weapon_object.tier_color,
                          black, black, (self.name_pos_x + self.default_icon_size[1], self.tier_name_pos_y),
                          is_clickable=False)

        self.static_text_lables.append(title_label)
        self.static_text_lables.append(weapon_name)
        self.static_text_lables.append(tier_text)

        self.build_metadata_labels() # builds static labels for every attribute of the item_object class


    def build_metadata_labels(self):
        # make label for every attribute of weapon object (cluttered asf I know..)
        n = 0
        black = (0, 0, 0)
        for attr, value in self.weapon_object.__dict__.items():
            attr_label = Lable(f'{attr}', self.text_size, self.ROOT.lable_hover_col, black, black,
                               (self.display_start_x_pos, self.display_start_y_pos + (n * (self.text_size + 5))),
                               is_clickable=False)
            value_label = Lable(f'{value}', self.text_size, 'white', black, black,
                                (self.display_start_x_pos + self.display_sep_space,
                                 self.display_start_y_pos + (n * (self.text_size + 5))), is_clickable=False)
            self.static_text_lables.append(attr_label)
            self.static_text_lables.append(value_label)
            n += 1


    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
