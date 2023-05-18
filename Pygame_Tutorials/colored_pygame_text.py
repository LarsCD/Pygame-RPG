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

col_spd = 1
col_dir = [1, 1, 1]
def_col = [0, 0, 0]


def draw_text(text, size, col, x, y):
    font = 'fonts/dogicapixelbold.ttf'
    font = pygame.font.Font(font, size)
    text_surface = font.render(text, False, col)
    text_rect = text_surface.get_rect()
    text_rect.center = (x, y)
    screen.blit(text_surface, text_rect)


class Lable:
    def __init__(self, text, size, col, x, y, clicked_color):
        self.text = text
        self.size = size
        self.color = col
        self.def_color = col
        self.clicked_color = clicked_color
        self.pos = (x, y)
        self.font = 'fonts/dogicapixelbold.ttf'
        # render text
        self.font_text = pygame.font.Font(self.font, self.size)
        self.text_surface = self.font_text.render(self.text, False, self.color)
        self.rect = self.text_surface.get_rect()
        self.rect.center = self.pos
        self.clicked = False
        self.released = True


    def draw_text(self, surface):
        action = False
        # get mouse pos
        pos = pygame.mouse.get_pos()
        # check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.released = False
                # action = True
                if pygame.mouse.get_pressed()[0] == 0 and self.clicked == True:
                    self.released = True

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


def col_change(col, dir):
    for i in range(3):
        col[i] += col_spd * dir[i]
        if col[i] >= 255 or col[i] <= 0:
            dir[i] *= -1

pygame.init()

run = True

text = Lable('Test', 40, 'white', W/2, H/2, 'blue')

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # main loop

    if text.draw_text(screen):
        print('clicked')
    # draw_text('PREVIEW TEXT', 40, def_col, W/2, H/2)
    # col_change(def_col, col_dir)

    # clock.tick()

    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()