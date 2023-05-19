import pygame
from Pygame_Tutorials.custom_pygame_assets import Lable

class Game_Loop:
    def __init__(self, Game_Main):
        self.Game_Main = Game_Main
        self.run_display = True

        # SCENE COLORS
        self.default_bg_color = self.Game_Main.default_bg_color
        self.bg_color = self.Game_Main.bg_color

        # SCENE LABELS
        self.static_text_lables = []


    def main_loop(self):
        # MAIN GAME LOOP
        # EVERYTHING GAME LOOP RELATED GOES HERE
        self.run_display = True
        self.build_static_text_lables()
        back_label = Lable('MAIN MENU', 20, 'white', 'gray', 'red',
                                        ((self.Game_Main.DISPLAY_WIDTH / 2), (self.Game_Main.DISPLAY_HEIGHT / 2) + 140),
                                        is_centered=True, is_clickable=True)

        while self.run_display:
            self.check_quit_event()

            self.set_background_color()
            self.draw_static_text_labels()

            if back_label.draw_text(self.Game_Main.window):
                self.run_display = False

            pygame.display.update()
            self.Game_Main.clock.tick(self.Game_Main.fps)



    def set_background_color(self):
        if self.bg_color != None:
            self.Game_Main.window.fill(self.bg_color)
        else:
            self.Game_Main.window.fill(self.default_bg_color)

    def build_static_text_lables(self):
        play_label = Lable('PLAYING GAME', 40, 'white', 'gray', 'green',
                           (self.Game_Main.DISPLAY_WIDTH / 2, self.Game_Main.DISPLAY_HEIGHT / 2),
                           is_centered=True, is_clickable=False)
        # package labels
        self.static_text_lables.append(play_label)

    def draw_static_text_labels(self):
        for label in self.static_text_lables:
            label.draw_text(self.Game_Main.window)

    def check_quit_event(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.run_display = False
