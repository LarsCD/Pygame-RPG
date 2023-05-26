import pygame
import logging
from assets.custom_pygame_assets import Lable
from dev.dev_logger import DevLogger


class DevScreen:
    def __init__(self):
        self.dev_mode = False
        self.mode_button = 'F1'
        self.mode_key = pygame.K_F1
        self.log = DevLogger(Dev_screen).log


    def update(self):
        if pygame.key.get_pressed()[self.mode_key]:
            self.log(logging.DEBUG, 'dev_screen')

