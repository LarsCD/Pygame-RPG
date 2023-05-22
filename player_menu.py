import pygame
from assets.custom_pygame_assets import Lable

class Player_Menu:
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
        self.display_sep_space = 250
        self.text_size = 15
        self.name_pos_x = 135
        self.background = pygame.image.load("assets/image/menu_background_1.png")

        # PLAYER
        self.player_object = None

        # ICON
        self.default_icon_size = (56, 56)
        self.tier_frame_pos = (128, 40)
        self.icon_pos = (130, 42)
        self.default_frame_size = (60, 60)
        self.tier_name_pos_y = 80

    def main_loop(self, player_object):
        self.static_text_lables = []
        self.player_object = player_object
        self.run_display = True
        self.build_static_text_lables()

        back_label = Lable('BACK', 20, 'white', 'gray', (153, 0, 28),
                           ((self.ROOT.DISPLAY_WIDTH / 2), (self.ROOT.DISPLAY_HEIGHT / 2) + 240),
                           is_centered=True, is_clickable=True)



        while self.run_display:
            self.ROOT.window.blit(pygame.transform.scale(self.background, self.ROOT.RESOLUTION), (0, 0))
            # TODO: make function for background ^
            self.check_quit_event()
            # self.set_background_color()
            self.draw_static_text_labels()


            if back_label.draw_text(self.ROOT.window):
                # quit out of view
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
        # build static labels
        title_label = Lable(self.title, self.text_size, self.ROOT.lable_col, self.ROOT.lable_click_col,
                            self.ROOT.lable_hover_col, (5, 5),
                            is_clickable=False)
        player_name = Lable(f'{str(self.player_object.player_name).upper()}', 35, 'white', black, black,
                            (self.name_pos_x + self.default_icon_size[1], 40), is_clickable=False)


        self.static_text_lables.append(title_label)
        self.static_text_lables.append(player_name)

        # make label for every attribute of weapon object (cluttered asf I know..)
        n = 0
        m = 0
        for attr, value in self.player_object.__dict__.items():
            row_length = 26
            offset_x = 0
            if m >= row_length:
                n = m - row_length
                offset_x = self.display_sep_space*2
            offset_y = 5

            pos_x = self.display_start_x_pos
            pos_y = self.display_start_y_pos + (n * (self.text_size + offset_y))

            attr_label = Lable(f'{attr}', self.text_size, self.ROOT.lable_hover_col, black, black,
                                (pos_x + offset_x, pos_y),
                                is_clickable=False)
            value_label = Lable(f'{value}', self.text_size, 'white', black, black,
                                (self.display_start_x_pos + self.display_sep_space + offset_x,
                                 self.display_start_y_pos + (n * (self.text_size + 5))), is_clickable=False)
            self.static_text_lables.append(attr_label)
            self.static_text_lables.append(value_label)
            n += 1
            m += 1

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.ROOT.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_display = False
