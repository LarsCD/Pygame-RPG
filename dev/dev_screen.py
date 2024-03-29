import pygame
import logging
import time
from datetime import datetime

from assets.custom_pygame_assets import Label
from dev.dev_logger import DevLogger


class DevScreen:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.dev_mode_enabled = False

        # config
        self.mode_key = pygame.K_F1
        self.color = 'green'

        self.log = DevLogger(DevScreen).log


        # data
        self.t1_start = time.perf_counter()
        self.t1_stop = time.perf_counter()
        self.t1_delta = 0
        self.fps = 0

        self.mouse_pos = (0, 0)

        self.game_time = 0

        # clock
        self.time_now = datetime.now()
        self.time_past = datetime.now()


    def main(self):
        self.t1_stop = time.perf_counter()
        self.update_key()

        # update self data
        self.calc_fps()
        self.get_mouse_pos()
        self.calc_game_time()

        # check clock
        self.clock()
        self.t1_start = time.perf_counter()

        if self.dev_mode_enabled:
            self.draw_dev_screen()



    def update_key(self):
        if pygame.key.get_pressed()[self.mode_key]:
            self.dev_mode_enabled = True
        else:
            self.dev_mode_enabled = False


    def clock(self):
        self.time_now = datetime.now()
        self.clock_delta = (self.time_now-self.time_past).total_seconds()
        if self.clock_delta > 1:
            self.update_fps()
            self.time_past = datetime.now()
            self.clock_delta = 0


    def calc_fps(self):
        self.t1_delta = self.t1_stop-self.t1_start
        fps = 1/self.t1_delta
        # print(fps)


    def update_fps(self):
        self.fps = 1/self.t1_delta


    def draw_dev_screen(self):
        title_label = Label(f'{self.ROOT.game_name} {self.ROOT.game_version} - by: LarsCD', 15,
                            self.color, 'black', 'black', (0, 0), is_clickable=False)

        fps_label = Label(f'fps: {round(self.fps, 1)} Hz  ({round((1 / self.fps + 0.1) * 1000, 2)}ms)', 15,
                          self.color, 'black', 'black', (0, 25), is_clickable=False)
        mouse_label = Label(f'mouse pos: {str(self.mouse_pos)}', 15,
                            self.color, 'black', 'black', (0, 50), is_clickable=False)

        game_time_label = Label(f'Game time: {str(self.game_time)}', 15,
                                self.color, 'black', 'black', (0, 75), is_clickable=False)

        # drawing all labels on the screen
        title_label.draw_text(self.ROOT.window)
        fps_label.draw_text(self.ROOT.window)
        mouse_label.draw_text(self.ROOT.window)
        game_time_label.draw_text(self.ROOT.window)

        pygame.display.update()


    def get_mouse_pos(self):
        self.mouse_pos = pygame.mouse.get_pos()


    def calc_game_time(self):
        self.game_time = (datetime.now() - self.ROOT.start_game)




