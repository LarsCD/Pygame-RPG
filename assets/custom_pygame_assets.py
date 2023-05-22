import pygame
import time

class Lable:
    def __init__(self, text: str, size: int, text_color: str, clicked_color: str, hover_color: str, possition: tuple,
                 is_centered=False, is_clickable=True, bold_text=False, function=None, function_args=None):
        self.text = text
        self.size = size
        self.color = text_color
        self.def_color = text_color
        self.clicked_color = clicked_color
        self.hover_color = hover_color
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
        self.hover = False
        self.action = False
        self.release = True
        self.release_click = True

        self.function = function
        self.function_args = function_args

        # AUDIO
        self.hover_sound = pygame.mixer.Sound('assets/audio/menu/Menu2.wav')
        self.click_sound = pygame.mixer.Sound('assets/audio/menu/Menu4.wav')

        pygame.mixer.Sound.set_volume(self.hover_sound, 0.2)
        pygame.mixer.Sound.set_volume(self.click_sound, 0.2)


    def draw_text(self, surface):
        self.action = False
        self.hover = False

        if not self.clickable:
            surface.blit(self.text_surface, (self.rect.x, self.rect.y))
            return 0
        # get mouse pos
        pos = pygame.mouse.get_pos()

        # check mouse over and clicked conditions
        if self.rect.collidepoint(pos):
            self.hover = True
            if self.clicked == True:
                if pygame.mouse.get_pressed()[0] == 0:
                    self.clicked = False
                    self.action = True
                    if self.function != None:
                        self.function(self.function_args)
            elif pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
        else:
            self.clicked = False
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False

        # change color on click
        if self.clicked:
            if self.release_click:
                self.click_sound.play()
            self.color = self.clicked_color
            self.text_surface = self.font_text.render(self.text, False, self.color)
            self.release_click = False
        else:
            if self.hover:
                if self.release:
                    self.hover_sound.play()
                self.color = self.hover_color
                self.text_surface = self.font_text.render(self.text, False, self.color)
                self.release = False
            else:
                self.release_click = True
                self.release = True
                self.color = self.def_color
                self.text_surface = self.font_text.render(self.text, False, self.color)

        # display on screen
        surface.blit(self.text_surface, (self.rect.x, self.rect.y))
        return self.action


class Screen_Effect:
    def __init__(self):
        pass

    def fade_to_color(self, surface, duration: float, color: tuple, pos: tuple=(0,0), size: tuple=(1280, 720)):
        fade_speed = (1 / (255 / duration))*3
        gradient = 5
        my_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        for i in range(255):
            n = i*gradient + i
            if n >= 128:
                break
            s = pygame.Surface(size)  # the size of your rect
            s.set_alpha(n)  # alpha level
            s.fill(color)  # this fills the entire surface
            surface.blit(s, pos)  # (0,0) are the top-left coordinates

            pygame.display.update()
            # time.sleep(fade_speed)
            pygame.time.Clock().tick(60)


    def fade_to_screen(self, surface, duration: float, pos: tuple, size: tuple):
        fade_speed = (1 / (255 / duration)) * 3
        gradient = 5
        my_image = pygame.Surface((50, 50), pygame.SRCALPHA)
        for i in range(255):
            n = i * gradient + i
            if n >= 128:
                break
            s = pygame.Surface(size)  # the size of your rect
            s.set_alpha(128-n)  # alpha level
            s.fill(color)  # this fills the entire surface
            surface.blit(s, pos)  # (0,0) are the top-left coordinates

            pygame.display.update()
            # time.sleep(fade_speed)
            pygame.time.Clock().tick(60)



class Health_bar():
    def __init__(self):
        pass


