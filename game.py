import pygame
from Pygame_Tutorials.custom_pygame_assets import Lable

class Main_Menu:
    def __init__(self, resolution: tuple, default_font: str, bold_font: str, lable_col: tuple,
                 lable_click_col: tuple, lable_hover_col: tuple):
        # PYGAME
        self.clock = pygame.time.Clock()

        # GENERAL FLAGS
        self.running = True
        self.playing = False

        # SCREEN PARAMETERS
        self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT = resolution
        self.display = pygame.Surface((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.window = pygame.display.set_mode((self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        self.default_font = default_font
        self.fps = 60

        # DEFAULT TEXT PARAMETERS
        self.bold_font = bold_font
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.lable_col = lable_col
        self.lable_click_col = lable_click_col
        self.lable_hover_col = lable_hover_col


    def game_loop(self):
        pygame.init()
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running, self.playing = False, False

            self.window.fill('orange')
            text_button = Lable('RPG3: MAIN MENU', 25, self.lable_col, self.lable_click_col, self.lable_hover_col,(2,2), is_clickable=False)
            options_lable = Lable('OPTIONS', 40, self.lable_col, self.lable_click_col, self.lable_hover_col, (self.DISPLAY_WIDTH/2, self.DISPLAY_HEIGHT/2), is_centered=True)
            text_button.draw_text(self.window)
            options_lable.draw_text(self.window)
            if options_lable.action:
                print('OPTIONS')

            self.window.blit(self.window, (0,0))
            pygame.display.update()
            self.clock.tick(self.fps)

