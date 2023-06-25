import pygame
import logging

from assets.custom_pygame_assets import Lable
from dev.dev_logger import DevLogger
from dev.dev_screen import DevScreen

class Player_Inventory:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.ROOT.default_bg_color
        self.bg_color = self.ROOT.bg_color
        self.BLACK = (0, 0, 0)

        # SCENE LABELS
        self.static_text_lables = []
        self.title = 'PLAYER INVENTORY'
        self.display_start_x_pos = 128
        self.display_start_y_pos = 120
        self.display_sep_space = 300
        self.text_size = 15
        self.name_pos_x = 135
        self.background = pygame.image.load("assets/images/menu_background_1.png")

        # ICON DATA
        self.default_icon_size = (64, 64)
        self.tier_frame_pos = (128, 40)
        self.icon_pos = (130, 42)
        self.default_frame_size = (60, 60)
        self.tier_name_pos_y = 80

        # MODULES
        self.DevLogger = DevLogger(Player_Inventory)
        self.DevScreen = DevScreen(self.ROOT)


    def main_loop(self, player_object):
        self.run_display = True
        self.build_static_text_lables()
        back_label = Lable('BACK', 20, 'white', 'gray', (153, 0, 28),
                           ((self.ROOT.DISPLAY_WIDTH / 2), (self.ROOT.DISPLAY_HEIGHT / 2) + 240),
                           is_centered=True, is_clickable=True)


        while self.run_display:
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.ROOT.RESOLUTION), (0, 0))
            self.check_quit_event()
            # self.set_background_color()
            self.draw_static_text_labels()

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
        self.static_text_lables.append(title_label)


    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
