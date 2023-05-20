import pygame
from assets.custom_pygame_assets import Lable

class Weapon_Display_Screen:
    def __init__(self, ROOT):
        self.ROOT = ROOT
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.ROOT.default_bg_color
        self.bg_color = self.ROOT.bg_color

        # SCENE LABELS
        self.static_text_lables = []
        self.title = ''

        # ITEM
        self.weapon_object = None

    def main_loop(self, weapon_object):
        self.weapon_object = weapon_object
        # self.title = f'Viewing {weapon_object.name}'
        self.run_display = True
        self.build_static_text_lables()
        back_label = Lable('BACK', 20, 'white', 'gray', 'red',
                           ((self.ROOT.DISPLAY_WIDTH / 2), (self.ROOT.DISPLAY_HEIGHT / 2) + 240),
                           is_centered=True, is_clickable=True)

        while self.run_display:
            self.check_quit_event()

            self.set_background_color()
            self.draw_static_text_labels()

            if back_label.draw_text(self.ROOT.window):
                self.run_display = False

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

        title_label = Lable(self.title, 25, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (5, 5),
                            is_clickable=False)
        about_0 = Lable(f'{str(self.weapon_object.name).upper()}', 35, 'white', black, black, (128, 40),
                        is_clickable=False)
        about_1 = Lable(f'tag: ', 25, def_color, black, black, (128, 120),
                        is_clickable=False)
        about_2 = Lable(f'name: ', 25, def_color, black, black, (128, 150),
                        is_clickable=False)
        about_3 = Lable(f'item_type', 25, def_color, black, black, (128, 180),
                        is_clickable=False)
        about_4 = Lable(f'weapon_type: ', 25, def_color, black, black, (128, 210),
                        is_clickable=False)
        about_5 = Lable(f'damage:', 25, def_color, black, black, (128, 240),
                        is_clickable=False)
        about_6 = Lable(f'tier:', 25, def_color, black, black, (128, 270),
                        is_clickable=False)
        about_7 = Lable(f'value:', 25, def_color, black, black, (128, 300),
                        is_clickable=False)
        about_8 = Lable(f'is_stackable:', 25, def_color, black, black, (128, 330),
                        is_clickable=False)
        about_9 = Lable(f'id:', 25, def_color, black, black, (128, 360),
                        is_clickable=False)
        about_10 = Lable(f'is_equipped:', 25, def_color, black, black, (128, 390),
                        is_clickable=False)

        stats_1 = Lable(f'{self.weapon_object.tag}', 25, 'white', black, black, (500, 120),
                        is_clickable=False)
        stats_2 = Lable(f'{self.weapon_object.name}', 25, 'white', black, black, (500, 150),
                        is_clickable=False)
        stats_3 = Lable(f'{self.weapon_object.item_type}', 25, 'white', black, black, (500, 180),
                        is_clickable=False)
        stats_4 = Lable(f'{self.weapon_object.weapon_type}', 25, 'white', black, black, (500, 210),
                        is_clickable=False)
        stats_5 = Lable(f'{self.weapon_object.damage}', 25, 'white', black, black, (500, 240),
                        is_clickable=False)
        stats_6 = Lable(f'{self.weapon_object.tier}', 25, 'white', black, black, (500, 270),
                        is_clickable=False)
        stats_7 = Lable(f'{self.weapon_object.value}', 25, 'white', black, black, (500, 300),
                        is_clickable=False)
        stats_8 = Lable(f'{self.weapon_object.is_stackable}', 25, 'white', black, black, (500, 330),
                        is_clickable=False)
        stats_9 = Lable(f'{self.weapon_object.id}', 25, 'white', black, black, (500, 360),
                        is_clickable=False)
        stats_10 = Lable(f'{self.weapon_object.is_equipped}', 25, 'white', black, black, (500, 390),
                        is_clickable=False)

        # package labels
        self.static_text_lables.append(title_label)
        self.static_text_lables.append(about_0)
        self.static_text_lables.append(about_1)
        self.static_text_lables.append(about_2)
        self.static_text_lables.append(about_3)
        self.static_text_lables.append(about_4)
        self.static_text_lables.append(about_5)
        self.static_text_lables.append(about_6)
        self.static_text_lables.append(about_7)
        self.static_text_lables.append(about_8)
        self.static_text_lables.append(about_9)
        self.static_text_lables.append(about_10)

        self.static_text_lables.append(stats_1)
        self.static_text_lables.append(stats_2)
        self.static_text_lables.append(stats_3)
        self.static_text_lables.append(stats_4)
        self.static_text_lables.append(stats_5)
        self.static_text_lables.append(stats_6)
        self.static_text_lables.append(stats_7)
        self.static_text_lables.append(stats_8)
        self.static_text_lables.append(stats_9)
        self.static_text_lables.append(stats_10)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_display = False
