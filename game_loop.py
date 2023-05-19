import pygame
from Pygame_Tutorials.custom_pygame_assets import Lable

class Game_Loop:
    def __init__(self, Game_Main):
        self.Game_Main = Game_Main
        self.run_display = True

    def main_loop(self):
        # MAIN GAME LOOP
        # EVERYTHING GAME RELATED GOES HERE
        self.run_display = True
        play_label = Lable('PLAYING GAME', 40, 'white', 'gray', 'green',
                           (self.Game_Main.DISPLAY_WIDTH / 2, self.Game_Main.DISPLAY_HEIGHT / 2),
                           is_centered=True, is_clickable=False)
        back_label = Lable('MAIN MENU', 20, 'white', 'gray', 'red',
                                        ((self.Game_Main.DISPLAY_WIDTH / 2), (self.Game_Main.DISPLAY_HEIGHT / 2) + 140),
                                        is_centered=True, is_clickable=True)
        while self.run_display:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run_display = False

            gray = (64, 64, 64)
            self.Game_Main.window.fill(gray)

            play_label.draw_text(self.Game_Main.window)
            if back_label.draw_text(self.Game_Main.window):
                self.run_display = False

            pygame.display.update()
            self.Game_Main.clock.tick(self.Game_Main.fps)

