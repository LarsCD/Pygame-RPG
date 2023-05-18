import pygame
import time
W, H = 800, 600
fps = 60

display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('colored_text')
clock = pygame.time.Clock()

black = (0, 0, 0)
white = (255, 255, 255)


class Lable:
    def __init__(self, text: str, size: int, text_color: str, clicked_color: str, possition: tuple, centered_pos: bool):
        self.text = text
        self.size = size
        self.color = text_color
        self.def_color = text_color
        self.clicked_color = clicked_color
        self.pos = possition
        self.font = 'fonts/dogicapixelbold.ttf'
        # render text
        self.font_text = pygame.font.Font(self.font, self.size)
        self.text_surface = self.font_text.render(self.text, False, self.color)
        self.rect = self.text_surface.get_rect()
        if centered_pos:
            self.rect.center = self.pos
        else:
            self.rect.topleft = self.pos
        self.clicked = False
        self.released = True


    def draw_text(self, surface):
        action = False
        # get mouse pos
        pos = pygame.mouse.get_pos()
        # check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if self.clicked == True:
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
                    action = True
            elif pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        else:
            self.clicked = False

        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False


        # change color on click
        if self.clicked:
            self.color = self.clicked_color
            self.text_surface = self.font_text.render(self.text, False, self.color)
        else:
            self.color = self.def_color
            self.text_surface = self.font_text.render(self.text, False, self.color)

        # display on screen
        surface.blit(self.text_surface, (self.rect.x, self.rect.y))
        return action

pygame.init()

run = True

text_lable = Lable('Test', 40, 'white', 'blue', (W/2, H/2), False)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # main loop

    if text.draw_text(screen):
        print('clicked')

    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()