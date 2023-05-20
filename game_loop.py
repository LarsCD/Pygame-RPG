import pygame
from assets.custom_pygame_assets import Lable
import logging
from dev.dev_logger import DevLogger
from data_loader import DataLoader
from entity import Entity


class Game_Loop:
    def __init__(self, Game_Main):
        self.Game_Main = Game_Main
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.Game_Main.default_bg_color
        self.bg_color = self.Game_Main.bg_color

        self.lable_col = self.Game_Main.lable_col
        self.lable_click_col = self.Game_Main.lable_click_col
        self.lable_hover_col = self.Game_Main.lable_hover_col

        # SCENE LABELS
        self.static_text_lables = []

        # DEV
        self.logger = DevLogger(Game_Loop)

        # MODULES
        self.DataLoader = DataLoader()
        self.Entity = Entity()

        # DATA
        self.static_enemy_data = None
        self.static_weapon_data = None
        self.static_player_class_data = None
        self.loaded_enemies = []
        self.loaded_weapons = []


    def main_loop(self):
        self.logger.log(logging.INFO, 'start Game.Loop:main_loop')
        # MAIN GAME LOOP

        # TESTING STUFF
        item_data = {}
        player_data = {}

        # for class_data_struct in player_class_data:
        #     player_data.update(dict({class_data_struct: player_class_data[class_data_struct]}))
        #
        # class_data_size = getsizeof(player_data)
        # player_object = self.Entity.create_player(player_data['sorcerer_class'])
        #
        # enemy_object_1 = self.Entity.create_enemy(enemy_data['placeholder_enemy'])
        # enemy_object_2 = self.Entity.create_enemy(enemy_data['placeholder_enemy'])
        # weapon_object_1 = self.Entity.create_weapon_item(
        #     weapon_data['enemy_weapons'][enemy_object_1.default_weapon])
        # weapon_object_2 = self.Entity.create_weapon_item(weapon_data['enemy_weapons']['placeholder_weapon'])
        #
        # player_object.give_item(weapon_object_1)
        # player_object.give_item(weapon_object_2)
        # player_object.remove_item('placeholder_weapon', 'weapon')



        # EVERYTHING GAME LOOP RELATED GOES HERE
        self.run_display = True
        self.load_static_data()
        self.build_static_text_lables()

        # TESTING
        weapon_1 = self.Entity.create_weapon_item(self.static_weapon_data['enemy_weapons']['placeholder_weapon'])

        # BUTTONS
        back_label = Lable('MAIN MENU', 20, self.lable_col, self.lable_click_col, self.lable_hover_col,
                                        ((self.Game_Main.DISPLAY_WIDTH / 2), (self.Game_Main.DISPLAY_HEIGHT / 2) + 240),
                                        is_centered=True, is_clickable=True)
        display_item = Lable(f'View {weapon_1.name} ({weapon_1.tag})', 20, 'white', 'gray', (153, 0, 28),
                                        ((self.Game_Main.DISPLAY_WIDTH / 2), (self.Game_Main.DISPLAY_HEIGHT / 2) + 240),
                                        is_centered=True, is_clickable=True)

        while self.run_display:
            self.check_quit_event()

            self.set_background_color()
            self.draw_static_text_labels()

            if back_label.draw_text(self.Game_Main.window):
                self.run_display = False
                self.logger.log(logging.INFO, f'exiting Game_Loop')


            pygame.display.update()
            self.Game_Main.clock.tick(self.Game_Main.fps)


    def load_static_data(self):
        self.enemy_data = self.DataLoader.load_data('data/enemy/enemy_data.json')
        self.weapon_data = self.DataLoader.load_data('data/items/weapon_data.json')
        self.player_class_data = self.DataLoader.load_data('data/player_classes/class_data.json')


    def set_background_color(self):
        if self.bg_color != None:
            self.Game_Main.window.fill(self.bg_color)
        else:
            self.Game_Main.window.fill(self.default_bg_color)

    def build_static_text_lables(self):
        play_label = Lable('PLAYING GAME...', 40, 'white', 'gray', 'green',
                           (self.Game_Main.DISPLAY_WIDTH*0.1, self.Game_Main.DISPLAY_HEIGHT*0.1), is_clickable=False)
        # package labels
        self.static_text_lables.append(play_label)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.Game_Main.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_display = False
