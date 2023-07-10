import random

import pygame
from assets.custom_pygame_assets import Label, Health_bar, Custom_bar, Highlight_marker
from dev.dev_screen import DevScreen
from combat_menu import Combat_Menu

'''
NOTES: 
background resolution = 936x544
'''

class World_menu:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.run_display = True

        # SCENE DISPLAY
        self.scene_background_reso = (936, 544) # picture in the background resolution = 936x544
        self.right_up_screen_x = 1000
        self.left_down_screen_1_x = 60
        self.left_down_screen_2_x = 400
        self.right_down_screen_1_x = 695

        # SCENE COLORS
        self.default_bg_color = self.ROOT.default_bg_color
        self.bg_color = self.ROOT.bg_color

        # SCENE LABELS
        self.static_text_lables = []
        self.title = 'OVERWORLD_MENU'
        self.background = pygame.image.load("assets/images/test_map.png")
        self.menu_background = pygame.image.load("assets/images/combat_background_1.png")

        # MODULES
        self.Combat_Menu = Combat_Menu(self.ROOT)
        self.DevScreen = DevScreen(self.ROOT)

        # PLAYER
        self.player_object = None
        self.enemy_object = None


    def main_loop(self, player_object, enemy_object):
        self.player_object = player_object
        self.enemy_object = enemy_object

        self.run_display = True



        # MENU
        back_label = Label('BACK', 25, 'white', 'gray', (153, 0, 28),
                           (self.right_up_screen_x, 460), is_clickable=True, bold_text=True)
        combat_switch = Label('COMBAT', 25, 'red', 'gray', (153, 0, 28),
                           (self.right_up_screen_x, 430), is_clickable=True, bold_text=True)
        loot_label = Label('LOOT', 25, 'white', 'gray', (153, 0, 28),
                           (self.right_up_screen_x, 490), is_clickable=True, bold_text=True)

        # PLAYER
        health_bar = Health_bar(self.player_object.hp, self.player_object.hpMax, (self.left_down_screen_1_x, 600),
                                250, 25, (255, 0, 0), (194, 194, 209), title='HP ')
        energy_bar = Custom_bar(self.player_object.ep, self.player_object.epMax, (self.left_down_screen_1_x, 630),
                                250, 25, (255, 178, 0), (194, 194, 209), title='EP ')
        mana_bar = Custom_bar(self.player_object.mp, self.player_object.mpMax, (self.left_down_screen_1_x, 660),
                              250, 25, (23, 93, 255), (194, 194, 209), title='MP ')
        xp_bar = Custom_bar(self.player_object.xp, self.player_object.xpMax, (121, 580),
                              250, 15, (102, 255, 227), (194, 194, 209), show_numbers=False)

        loot_marker = Highlight_marker('+ RARE SWORD (1)', 20, (77, 166, 255), (40, 440), 1.5, (0, 1), 1)

        while self.run_display:
            self.ROOT.window.fill((0, 0, 0))
            # self.background.set_alpha(128)
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.scene_background_reso), (0, -1))
            self.ROOT.window.blit(pygame.transform.scale(self.menu_background, self.ROOT.RESOLUTION), (0, 0))

            self.check_quit_event()

            self.build_static_text_lables()
            self.build_attr_labels()

            self.draw_static_text_labels()


            # PLAYER
            health_bar.update(self.ROOT.window, self.player_object.hp, self.player_object.hpMax)
            # energy_bar.update(self.ROOT.window, self.player_object.ep, self.player_object.epMax)
            # mana_bar.update(self.ROOT.window, self.player_object.mp, self.player_object.mpMax)
            xp_bar.update(self.ROOT.window, self.player_object.xp, self.player_object.xpMax)

            # PLAYER INTERACTION
            if loot_label.draw_text(self.ROOT.window):
                random_item = self.player_object.inventory['weapon'][random.randint(0, len(self.player_object.inventory['weapon'])-1)]
                loot_marker.animate((40, 440), text=f'+ 1 {random_item.name} (1)', color=list(random_item.tier_color))

            # draw marker
            loot_marker.update(self.ROOT.window)

            # MENU
            if combat_switch.draw_text(self.ROOT.window):
                self.Combat_Menu.main_loop(self.player_object, self.enemy_object)
            if back_label.draw_text(self.ROOT.window):
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
        level_label = Label(f'LEVEL', 20, 'gray', 'black', 'black',
                            (50, 500), is_clickable=False, bold_text=True)
        level_label_value = Label(f'{self.player_object.level}', 20, 'white', 'black', 'black',
                                  (150, 500), is_clickable=False, bold_text=True)


        # package labels
        self.static_text_lables.append(level_label)
        self.static_text_lables.append(level_label_value)


    def build_attr_labels(self):
        strg_label = Label(f'STR', 20, 'gray', 'black', 'black',
                           (self.left_down_screen_2_x, 575), is_clickable=False, bold_text=True)
        agil_label = Label(f'AGI', 20, 'gray', 'black', 'black',
                           (self.left_down_screen_2_x, 600), is_clickable=False, bold_text=True)
        intl_label = Label(f'INT', 20, 'gray', 'black', 'black',
                           (self.left_down_screen_2_x, 625), is_clickable=False, bold_text=True)
        slth_label = Label(f'STL', 20, 'gray', 'black', 'black',
                           (self.left_down_screen_2_x, 650), is_clickable=False, bold_text=True)
        sorc_label = Label(f'SOR', 20, 'gray', 'black', 'black',
                           (self.left_down_screen_2_x, 675), is_clickable=False, bold_text=True)

        strg_value_label = Label(f'{self.player_object.strength}', 20, 'white', 'black', 'black',
                                 (self.left_down_screen_2_x + 65, 575), is_clickable=False, bold_text=True)
        agil_value_label = Label(f'{self.player_object.agility}', 20, 'white', 'black', 'black',
                                 (self.left_down_screen_2_x + 65, 600), is_clickable=False, bold_text=True)
        intl_value_label = Label(f'{self.player_object.intelligence}', 20, 'white', 'black', 'black',
                                 (self.left_down_screen_2_x + 65, 625), is_clickable=False, bold_text=True)
        slth_value_label = Label(f'{self.player_object.stealth}', 20, 'white', 'black', 'black',
                                 (self.left_down_screen_2_x + 65, 650), is_clickable=False, bold_text=True)
        sorc_value_label = Label(f'{self.player_object.sorcery}', 20, 'white', 'black', 'black',
                                 (self.left_down_screen_2_x + 65, 675), is_clickable=False, bold_text=True)

        self.static_text_lables.append(strg_label)
        self.static_text_lables.append(agil_label)
        self.static_text_lables.append(intl_label)
        self.static_text_lables.append(slth_label)
        self.static_text_lables.append(sorc_label)
        self.static_text_lables.append(strg_value_label)
        self.static_text_lables.append(agil_value_label)
        self.static_text_lables.append(intl_value_label)
        self.static_text_lables.append(slth_value_label)
        self.static_text_lables.append(sorc_value_label)




    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)
        self.static_text_lables = []

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
