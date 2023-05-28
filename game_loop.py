import os
import time

import pygame
import logging
from datetime import datetime

from data_loader import DataLoader
from dev.dev_logger import DevLogger
from entity_loader import Entity_Loader
from assets.custom_pygame_assets import Lable
from weapon_display_screen import Weapon_Display_Screen
from player_menu import Player_Menu
from dev.dev_logger import DevLogger
from dev.dev_screen import DevScreen
from world.level_loader import Level_Loader


class Game_Loop:
    def __init__(self, Game_Setup):
        self.Game_Setup = Game_Setup
        self.run_display = True
        self.clock = pygame.time.Clock()

        # DATA
        self.game_name = Game_Setup.game_name
        self.game_version = Game_Setup.game_version
        self.start_game = datetime.now()

        # SCENE COLORS
        self.default_bg_color = self.Game_Setup.default_bg_color
        self.bg_color = self.Game_Setup.bg_color

        self.lable_col = self.Game_Setup.lable_col
        self.lable_click_col = self.Game_Setup.lable_click_col
        self.lable_hover_col = self.Game_Setup.lable_hover_col

        # SCREEN PARAMETERS
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = self.Game_Setup.DISPLAY_WIDTH, self.Game_Setup.DISPLAY_HEIGHT
        self.RESOLUTION = self.Game_Setup.RESOLUTION
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.default_font = self.Game_Setup.default_font
        self.fps = self.Game_Setup.fps

        # SCENE LABELS
        self.static_text_lables = []

        # DEV
        self.logger = DevLogger(Game_Loop)

        # PLAYER
        self.player_object = None

        # MODULES
        self.DevLogger = DevLogger(Game_Loop)
        self.DevScreen = DevScreen(self)
        self.DataLoader = DataLoader()
        self.Entity_Loader = Entity_Loader()
        self.Level_Loader = Level_Loader()

        # DISPLAYS
        self.Weapon_Display_Screen = Weapon_Display_Screen(self)
        self.Player_Menu = Player_Menu(self)

        # DATA
        self.static_enemy_data = {}
        self.static_item_data = {}
        self.static_player_class_data = {}
        self.static_world_data = {}
        self.loaded_enemies = [] # TODO: use these later
        self.loaded_weapons = [] # TODO: use these later


    def main_loop(self):
        self.logger.log(logging.INFO, 'start Game.Loop:main_loop')
        # MAIN GAME LOOP

        # TESTING STUFF
        item_data = {}
        player_data = {}

        # EVERYTHING GAME LOOP RELATED GOES HERE
        self.run_display = True
        self.load_all_static_data()
        self.build_static_text_lables()

        #### ---------------------------- TESTING ---------------------------- ####
        t1 = time.perf_counter()

        level_1 = self.Level_Loader.load_level(self.static_world_data['level_1']['cave_level_1'])
        level_1.load_level(self.static_item_data, self.static_enemy_data)

        weapon_1 = self.Entity_Loader.create_item(self.static_item_data['weapon_data']['enemy_weapons']['placeholder_weapon'])
        weapon_2 = self.Entity_Loader.create_item(self.static_item_data['weapon_data']['weapons']['rare_sword'])
        weapon_3 = self.Entity_Loader.create_item(self.static_item_data['weapon_data']['weapons']['rare_sword'])
        weapon_4 = self.Entity_Loader.create_item(self.static_item_data['weapon_data']['enemy_weapons']['placeholder_weapon'])
        weapon_5 = self.Entity_Loader.create_item(self.static_item_data['weapon_data']['enemy_weapons']['placeholder_weapon'])
        potion_1 = self.Entity_Loader.create_item(self.static_item_data['potion_data']['healing_potions']['small_healing_potion'])
        potion_2 = self.Entity_Loader.create_item(self.static_item_data['potion_data']['healing_potions']['medium_healing_potion'])
        potion_3 = self.Entity_Loader.create_item(self.static_item_data['potion_data']['mana_potions']['small_mana_potion'])


        self.player_object = self.Entity_Loader.create_player(self.static_player_class_data['sorcerer_class'])
        self.player_object.give_item(weapon_1)
        self.player_object.give_item(weapon_2)
        self.player_object.give_item(weapon_3)
        self.player_object.give_item(weapon_4)
        self.player_object.give_item(weapon_5)
        self.player_object.give_item(potion_1)
        self.player_object.give_item(potion_2)
        self.player_object.give_item(potion_3)


        t2 = time.perf_counter()
        dt = t2-t1
        self.logger.log(logging.INFO, f'created testing entities ({round(dt*1000, 2)} ms)')
        #### ---------------------------- TESTING ---------------------------- ####

        # BUTTONS
        back_label = Lable('MAIN MENU', 20, self.lable_col, self.lable_click_col, (153, 0, 28),
                            ((self.DISPLAY_WIDTH / 2), (self.DISPLAY_HEIGHT / 2) + 240),
                            is_centered=True, is_clickable=True)
        display_item = Lable(f'View {str(weapon_1.name).upper()} ({weapon_1.tag})', 20, self.lable_col,
                             self.lable_click_col, self.lable_hover_col, (self.Game_Setup.DISPLAY_WIDTH * 0.1, 200),
                             is_clickable=True)
        display_item_2 = Lable(f'View {str(weapon_2.name).upper()} ({weapon_2.tag})', 20, self.lable_col,
                               self.lable_click_col,
                               self.lable_hover_col, (self.Game_Setup.DISPLAY_WIDTH * 0.1, 225), is_clickable=True)

        display_item_3 = Lable(f'View {str(potion_1.name).upper()} ({potion_1.tag})', 20, self.lable_col,
                               self.lable_click_col,
                               self.lable_hover_col, (self.Game_Setup.DISPLAY_WIDTH * 0.1, 275), is_clickable=True)

        display_item_4 = Lable(f'View {str(potion_2.name).upper()} ({potion_2.tag})', 20, self.lable_col,
                               self.lable_click_col,
                               self.lable_hover_col, (self.Game_Setup.DISPLAY_WIDTH * 0.1, 300), is_clickable=True)

        display_item_5 = Lable(f'View {str(potion_3.name).upper()} ({potion_3.tag})', 20, self.lable_col,
                               self.lable_click_col,
                               self.lable_hover_col, (self.Game_Setup.DISPLAY_WIDTH * 0.1, 325), is_clickable=True)

        display_player = Lable(f'View PLAYER ({self.player_object.player_class_name})', 20, self.lable_col,
                               self.lable_click_col,
                               self.lable_hover_col, (self.Game_Setup.DISPLAY_WIDTH * 0.1, 400), is_clickable=True)

        while self.run_display:
            self.check_quit_event()

            self.set_background_color()
            self.draw_static_text_labels()


            if display_item.draw_text(self.window):
                self.Weapon_Display_Screen.main_loop(weapon_1)
            if display_item_2.draw_text(self.window):
                self.Weapon_Display_Screen.main_loop(weapon_2)
            if display_item_3.draw_text(self.window):
                self.Weapon_Display_Screen.main_loop(potion_1)
            if display_item_4.draw_text(self.window):
                self.Weapon_Display_Screen.main_loop(potion_2)
            if display_item_5.draw_text(self.window):
                self.Weapon_Display_Screen.main_loop(potion_3)

            if display_player.draw_text(self.window):
                self.Player_Menu.main_loop(self.player_object)

            if back_label.draw_text(self.window):
                # quit out of game
                self.run_display = False
                self.logger.log(logging.INFO, f'exiting Game_Loop')

            # dev
            self.DevScreen.main()

            pygame.display.update()
            self.Game_Setup.clock.tick(self.Game_Setup.fps)

    # this method loads all necessary metadata for enemies, items, players, etc.
    def load_all_static_data(self):
        t1 = time.perf_counter()
        self.logger.log(logging.INFO, f'loading all game data...')
        exluded_data_folders = []
        cwd = os.getcwd()
        data_folder_path = 'data'
        for data_folder in os.listdir(data_folder_path):
            if data_folder not in exluded_data_folders:
                target_folder = f'{cwd}/{data_folder_path}/{data_folder}'
                if target_folder == f'{cwd}/{data_folder_path}/enemy':
                    for file in os.listdir(target_folder):
                        if file == 'enemy_data.json':
                            enemy_data = self.DataLoader.load_data(f'{data_folder_path}/{data_folder}/{file}')
                            self.static_enemy_data.update({'enemy_data': enemy_data})
                        if file == 'boss_enemy_data.json':
                            boss_enemy_data = self.DataLoader.load_data(f'{data_folder_path}/{data_folder}/{file}')
                            self.static_enemy_data.update({'boss_enemy_data': boss_enemy_data})
                if target_folder == f'{cwd}/{data_folder_path}/items':
                    for file in os.listdir(target_folder):
                        if file == 'weapon_data.json':
                            weapon_data = self.DataLoader.load_data(f'{data_folder_path}/{data_folder}/{file}')
                            self.static_item_data.update({'weapon_data': weapon_data})
                        if file == 'potion_data.json':
                            potion_data = self.DataLoader.load_data(f'{data_folder_path}/{data_folder}/{file}')
                            self.static_item_data.update({'potion_data': potion_data})
                if target_folder == f'{cwd}/{data_folder_path}/player_classes':
                    self.static_player_class_data = self.DataLoader.load_data(f'{data_folder_path}/{data_folder}/class_data.json')
                if target_folder == f'{cwd}/{data_folder_path}/world_data':
                    self.static_world_data = self.DataLoader.load_data(f'{data_folder_path}/{data_folder}/world_data.json')
        t2 = time.perf_counter()
        dt = t2-t1
        self.logger.log(logging.INFO, f'game data succesfully loaded ({round(dt*1000, 2)} ms)')



    def set_background_color(self):
        if self.bg_color != None:
            self.window.fill(self.bg_color)
        else:
            self.window.fill(self.default_bg_color)

    def build_static_text_lables(self):
        play_label = Lable('PLAYING GAME...', 40, 'white', 'gray', 'green',
                           (self.Game_Setup.DISPLAY_WIDTH * 0.1, self.Game_Setup.DISPLAY_HEIGHT * 0.1), is_clickable=False)
        # package labels
        self.static_text_lables.append(play_label)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
