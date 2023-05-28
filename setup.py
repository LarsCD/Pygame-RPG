import logging
from dev.dev_logger import DevLogger
from game_setup import Game_Setup


class Setup:
    def __init__(self):
        pass

    def start_game(self):

        game_metadata = ((1280, 720), 'fonts/dogicapixel.ttf', 'fonts/dogicapixelbold.ttf', 'white', 'gray', (102, 255, 227))

        game = Game_Setup(*game_metadata)
        game.main_menu_loop()


