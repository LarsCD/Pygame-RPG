import pygame

class Lable:
    def __init__(self, text: str, size: int, text_color: str, clicked_color: str, possition: tuple, is_centered=False, is_clickable=True, bold_text=False):
        self.text = text
        self.size = size
        self.color = text_color
        self.def_color = text_color
        self.clicked_color = clicked_color
        self.pos = possition
        if bold_text:
            self.font = 'fonts/dogicapixelbold.ttf'
        else:
            self.font = 'fonts/dogicapixel.ttf'
        # render text
        self.font_text = pygame.font.Font(self.font, self.size)
        self.text_surface = self.font_text.render(self.text, False, self.color)
        self.rect = self.text_surface.get_rect()
        if is_centered:
            self.rect.center = self.pos
        else:
            self.rect.topleft = self.pos
        self.clickable = is_clickable
        self.clicked = False


    def draw_text(self, surface):
        action = False

        if not self.clickable:
            surface.blit(self.text_surface, (self.rect.x, self.rect.y))
            return 0
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