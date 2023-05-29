import pygame
from assets.custom_pygame_assets import Lable, Screen_Effect
from game_loop import Game_Loop
import logging
from dev.dev_logger import DevLogger
import time


class Game_Setup:
    def __init__(self, resolution: tuple, default_font: str, bold_font: str, lable_col: tuple,
                 lable_click_col: tuple, lable_hover_col: tuple, bg_color: tuple=None):
        # PYGAME
        pygame.init()

        self.game_name = 'RPG3'
        self.game_version = 'v0.1.6'

        pygame.display.set_caption(self.game_name)
        self.clock = pygame.time.Clock()

        # GENERAL FLAGS
        self.running = True
        self.playing = False

        # SCREEN PARAMETERS
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = resolution
        self.RESOLUTION = resolution
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.default_font = default_font
        self.fps = 120

        # DEFAULT TEXT LABLE PARAMETERS
        self.bold_font = bold_font
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.lable_col = lable_col
        self.lable_click_col = lable_click_col
        self.lable_hover_col = lable_hover_col

        # SCENE COLORS
        self.default_bg_color = (64, 64, 64)
        self.bg_color = bg_color

        # SCENE LABELS
        self.static_text_lables = []
        self.background = pygame.image.load("assets/images/test_map.png")

        # DISPLAYS
        self.Game_Loop = Game_Loop(self) # MAIN GAME LOOP
        self.Options = Options(self)
        self.About = About(self)

        # DEV
        self.logger = DevLogger(Game_Setup)


    def main_menu_loop(self):
        # setup
        self.build_static_text_lables()

        play_label = Lable('PLAY GAME', 60, self.lable_col, self.lable_click_col, self.lable_hover_col,
                              ((self.DISPLAY_WIDTH / 2), (self.DISPLAY_HEIGHT / 2)-30), is_centered=True)
        options_label = Lable('OPTIONS', 40, self.lable_col, self.lable_click_col, self.lable_hover_col,
                              ((self.DISPLAY_WIDTH / 2), (self.DISPLAY_HEIGHT / 2)+60), is_centered=True)
        about_label = Lable('ABOUT', 40, self.lable_col, self.lable_click_col, self.lable_hover_col,
                              ((self.DISPLAY_WIDTH / 2), (self.DISPLAY_HEIGHT / 2) + 105), is_centered=True)
        exit_label = Lable('EXIT', 30, self.lable_col, self.lable_click_col, (153, 0, 28),
                            (int(self.DISPLAY_WIDTH / 2), int(self.DISPLAY_HEIGHT*0.9)), is_centered=True)
        fader_effect = Screen_Effect()
        while self.running:
            self.window.blit(pygame.transform.scale(self.background, self.RESOLUTION), (0, 0))
            self.check_quit_event()

            # self.set_background_color()
            self.draw_static_text_labels()

            if play_label.draw_text(self.window):
                # click play
                # RUN MAIN GAME LOOP
                self.logger.log(logging.INFO, f'starting Game_Loop')
                fader_effect.fade_to_color(self.window, 10, (self.default_bg_color))
                self.Game_Loop.main_loop()
                fader_effect.fade_to_color(self.window, 10, (self.default_bg_color))
            if options_label.draw_text(self.window):
                # click options
                self.logger.log(logging.INFO, f'starting Options')
                fader_effect.fade_to_color(self.window, 1, (self.default_bg_color))
                self.Options.main_loop()
                fader_effect.fade_to_color(self.window, 1, (self.default_bg_color))
            if about_label.draw_text(self.window):
                # click options
                self.logger.log(logging.INFO, f'starting About')
                fader_effect.fade_to_color(self.window, 1, (self.default_bg_color))
                self.About.main_loop()
                fader_effect.fade_to_color(self.window, 1, (self.default_bg_color))
            if exit_label.draw_text(self.window):
                fader_effect.fade_to_color(self.window, 0.5, (self.default_bg_color))
                self.running = False



            self.window.blit(self.window, (0,0))
            pygame.display.update()
            self.clock.tick(self.fps)


    def set_background_color(self):
        if self.bg_color != None:
            self.window.fill(self.bg_color)
        else:
            self.window.fill(self.default_bg_color)

    def build_static_text_lables(self):
        title_label = Lable('MAIN MENU', 25, self.lable_col, self.lable_click_col, self.lable_hover_col, (200, 30),
                            is_clickable=False)
        about_7 = Lable('BY: LarsCD', 25, 'white', self.lable_click_col, self.lable_hover_col, (200, int(self.DISPLAY_HEIGHT*0.93)),
                        is_clickable=False)
        # package labels
        self.static_text_lables.append(title_label)
        self.static_text_lables.append(about_7)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()



class Options:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.ROOT.default_bg_color
        self.bg_color = self.ROOT.bg_color

        # SCENE LABELS
        self.static_text_lables = []

        # DEV
        self.logger = DevLogger(Options)

    def main_loop(self):
        self.run_display = True
        self.build_static_text_lables()
        back_label = Lable('MAIN MENU', 20, 'white', 'gray', (153, 0, 28),
                                        ((self.ROOT.DISPLAY_WIDTH / 2), (self.ROOT.DISPLAY_HEIGHT / 2) + 240),
                                        is_centered=True, is_clickable=True)
        reso_3 = Lable('1280x720', 25, self.ROOT.lable_col, self.ROOT.lable_click_col, self.ROOT.lable_hover_col,(200, 180))

        while self.run_display:
            self.ROOT.window.blit(self.ROOT.background, (0, 0))
            self.check_quit_event()


            # self.set_background_color()
            self.draw_static_text_labels()

            if back_label.draw_text(self.ROOT.window):
                self.run_display = False
                self.logger.log(logging.INFO, f'exiting Options')
            if reso_3.draw_text(self.ROOT.window):
                Game_Setup.DISPLAY_WIDTH, Game_Setup.DISPLAY_HEIGHT = (1280, 720)
                self.logger.log(logging.INFO, f'resolution changed: 1280x720')

            pygame.display.update()
            self.ROOT.clock.tick(self.ROOT.fps)


    def set_background_color(self):
        if self.bg_color != None:
            self.ROOT.window.fill(self.bg_color)
        else:
            self.ROOT.window.fill(self.default_bg_color)

    def build_static_text_lables(self):
        title_label = Lable('OPTIONS', 25, self.ROOT.lable_col, self.ROOT.lable_click_col, self.ROOT.lable_hover_col, (200, 30),
                            is_clickable=False)
        reso_label = Lable('RESOLUTION: ', 25, self.ROOT.lable_col, self.ROOT.lable_click_col, self.ROOT.lable_hover_col, (200, 145),
                            is_clickable=False)
        # package labels
        self.static_text_lables.append(title_label)
        self.static_text_lables.append(reso_label)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()



class About:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.ROOT.default_bg_color
        self.bg_color = self.ROOT.bg_color

        # SCENE LABELS
        self.static_text_lables = []
        self.title = 'ABOUT'

        # DEV
        self.logger = DevLogger(About)

    def main_loop(self):
        self.run_display = True
        self.build_static_text_lables()
        back_label = Lable('MAIN MENU', 20, 'white', 'gray', (153, 0, 28),
                           ((self.ROOT.DISPLAY_WIDTH / 2), (self.ROOT.DISPLAY_HEIGHT / 2) + 240),
                           is_centered=True, is_clickable=True)

        while self.run_display:
            self.ROOT.window.blit(self.ROOT.background, (0, 0))
            self.check_quit_event()

            # self.set_background_color()
            self.draw_static_text_labels()

            if back_label.draw_text(self.ROOT.window):
                self.run_display = False
                self.logger.log(logging.INFO, f'exiting About')

            pygame.display.update()
            self.ROOT.clock.tick(self.ROOT.fps)

    def set_background_color(self):
        if self.bg_color != None:
            self.ROOT.window.fill(self.bg_color)
        else:
            self.ROOT.window.fill(self.default_bg_color)

    def build_static_text_lables(self):
        # "My eyes burn looking at this but Im not gonna change it lol" ~L
        def_color = self.ROOT.lable_hover_col
        black = (0, 0, 0)
        title_label = Lable(self.title, 25, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (200, 30),
                            is_clickable=False)
        about_1 = Lable('This is an RPG game where you play as a ', 25, def_color, black, black, (200, 120),
                            is_clickable=False)
        about_2 = Lable('character exploring the world and fighting', 25, def_color, black, black, (200, 150),
                        is_clickable=False)
        about_3 = Lable('enemies. For now you can only play as a select ', 25, def_color, black, black, (200, 180),
                        is_clickable=False)
        about_4 = Lable('few classes like Knight and Sorcerer. More ', 25, def_color, black, black, (200, 210),
                        is_clickable=False)
        about_5 = Lable('content will be added to enhance the ', 25, def_color, black, black, (200, 240),
                        is_clickable=False)
        about_6 = Lable('gaming experience.', 25, def_color, black, black, (200, 270),
                        is_clickable=False)
        about_7 = Lable('BY: LarsCD', 25, 'white', black, black, (200, int(self.ROOT.DISPLAY_HEIGHT*0.93)),
                        is_clickable=False)
        # package labels
        self.static_text_lables.append(title_label)
        self.static_text_lables.append(about_1)
        self.static_text_lables.append(about_2)
        self.static_text_lables.append(about_3)
        self.static_text_lables.append(about_4)
        self.static_text_lables.append(about_5)
        self.static_text_lables.append(about_6)
        self.static_text_lables.append(about_7)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()