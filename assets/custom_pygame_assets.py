import pygame
import time
import random

class Lable:
    def __init__(self, text: str, size: int, text_color: str, clicked_color: str, hover_color: str, possition: list,
                 is_centered=False, is_clickable=True, bold_text=False, class_module=None, class_method=None, method_args=None):
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

        self.class_module = class_module
        self.class_method = class_method
        self.method_args = method_args

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
                # self.text_surface = surface.draw.text(self.text, self.rect.x, self.rect.y, fontname=self.font_text, fontsize=self.size)
                # TODO: DO MAJOR REMODEL OF TEXT WRITING (26-5-2023)
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


class Health_bar:
    def __init__(self, hp_current: int, hp_max: int, pos, width, height, color, bg_color, title=None, show_numbers=True, color_gradient=False):
        self.health_bar_length = width
        self.color = color
        self.bg_color = bg_color
        self.pos = pos
        self.width = width
        self.height = height

        self.title = title
        self.show_numbers = show_numbers
        self.color_gradient = color_gradient


        self.current_hp = hp_current
        self.max_hp = hp_max

        self.health_ratio = self.max_hp / self.health_bar_length

    def update(self, surface, current_hp, max_hp):
        self.current_hp = current_hp
        self.max_hp = max_hp
        self.show_health(surface)

    def subtract(self, amount: int):
        if self.current_hp > 0:
            self.current_hp -= amount
        if self.current_hp <= 0:
            self.current_hp = 0

    def add(self, amout: int):
        if self.current_hp < self.max_hp:
            self.current_hp += amout
        if self.current_hp >= self.max_hp:
            self.current_hp = self.max_hp

    def show_health(self, surface):
        if self.color_gradient:
            hp_percentage = (self.current_hp/self.max_hp)

            if hp_percentage < 0.5:
                self.color = (255, (255*hp_percentage*2), 0)
            elif hp_percentage >= 0.5:
                self.color = ((255+127)-(255*hp_percentage), 255, 0)
            # TODO: doesnt work great.. :(   (24-5-2023)
            # print(self.color)
            # print(hp_percentage)

        # show bar title
        if self.title != None:
            offset_x = (self.height-6)*len(self.title)+4
            title_label = Lable(str(self.title).upper(), (self.height-6), 'white', 'black', 'black', (self.pos[0]+4, self.pos[1]+4), is_centered=False, is_clickable=False, bold_text=True)
            title_label.draw_text(surface)
        else:
            offset_x = 0
        # draw rects
        pygame.draw.rect(surface, self.color, (self.pos[0]+offset_x, self.pos[1], (self.current_hp/self.health_ratio), self.height))
        pygame.draw.rect(surface, self.bg_color, (self.pos[0]+offset_x, self.pos[1], self.health_bar_length,self.height), 4)
        # show numbers
        if self.show_numbers:
            health_label = Lable(f'{self.current_hp}/{self.max_hp}', (self.height-10), 'white', 'black', 'black', (self.pos[0]+4+offset_x, self.pos[1]+4), is_centered=False, is_clickable=False, bold_text=True)
            health_label.draw_text(surface)


class Custom_bar:
    def __init__(self, stat_current: int, stat_max: int, pos, width, height, color, bg_color, title=None, show_numbers=True):
        self.health_bar_length = width
        self.color = color
        self.bg_color = bg_color
        self.pos = pos
        self.width = width
        self.height = height

        self.title = title
        self.show_numbers = show_numbers

        self.current_stat = stat_current
        self.max_stat = stat_max

        self.health_ratio = self.max_stat / self.health_bar_length

    def update(self, surface, stat_current, stat_max):
        self.current_stat = stat_current
        self.max_stat = stat_max
        self.show_stat(surface)

    def subtract(self, amount: int):
        if self.current_stat > 0:
            self.current_stat -= amount
        if self.current_stat <= 0:
            self.current_stat = 0

    def add(self, amout: int):
        if self.current_stat < self.max_stat:
            self.current_stat += amout
        if self.current_stat >= self.max_stat:
            self.current_stat = self.max_stat

    def show_stat(self, surface):

        # show bar title
        if self.title != None:
            offset_x = (self.height-6)*len(self.title)+4
            title_label = Lable(str(self.title).upper(), (self.height-6), 'white', 'black', 'black', (self.pos[0]+4, self.pos[1]+4), is_centered=False, is_clickable=False, bold_text=True)
            title_label.draw_text(surface)
        else:
            offset_x = 0
        # draw rects
        pygame.draw.rect(surface, self.color, (self.pos[0]+offset_x, self.pos[1], (self.current_stat/self.health_ratio), self.height))
        pygame.draw.rect(surface, self.bg_color, (self.pos[0]+offset_x, self.pos[1], self.health_bar_length,self.height), 4)
        # show numbers
        if self.show_numbers:
            health_label = Lable(f'{self.current_stat}/{self.max_stat}', (self.height-10), 'white', 'black', 'black', (self.pos[0]+4+offset_x, self.pos[1]+4), is_centered=False, is_clickable=False, bold_text=True)
            health_label.draw_text(surface)


class Highlight_marker:
    def __init__(self, text: str, size: int, text_color: str, start_pos: list, time: float, vector: tuple, speed: float, spread=0):
        self.start_pos = list(start_pos)
        self.pos = self.start_pos
        self.label = Lable(text, size, text_color, 'black', 'black', self.pos, is_centered=True, is_clickable=False)
        self.spread = spread

        self.time_length = time
        self.time_step = (1/30) # renders at 30 fps

        self.speed = speed
        self.vector = vector

        self.step = 0
        self.time = 0
        self.time_remaining = 0

    def start(self, surface):
        if self.time_remaining <= 0:
            return
        else:
            self.step += 1
            self.time = self.step*self.time_step
            self.time_remaining = self.time_length - self.time

            # position and rendering
            label_pos_x = (self.label.pos[0] + (self.vector[0] * self.speed * self.step))
            label_pos_y = (self.label.pos[1] + (self.vector[1]*-1 * self.speed * self.step))
            self.label.rect.x = label_pos_x
            self.label.rect.y = label_pos_y
            self.label.draw_text(surface)
            # pygame.draw.rect(surface, 'red', pygame.Rect(label_pos_x, label_pos_y, 70, 20), 2)

    def animate(self, pos, text=None, color=None, time=None, vari_red=0, vari_grn=0, vari_blu=0):
        self.step = 0
        self.time = 0
        self.time_remaining = self.time_length - self.time

        self.label.pos[0] = pos[0] + random.randint(self.spread*-1, self.spread)
        self.label.pos[1] = pos[1] + random.randint(self.spread*-1, self.spread*0.5)


        if color != None:
            color[0] = color[0] + random.randint(vari_red*-1, vari_red)
            if color[0] > 255:
                color[0] = 255
            if color[0] <= 0:
                color[0] = 0
            color[1] = color[1] + random.randint(vari_grn * -1, vari_grn)
            if color[1] > 255:
                color[1] = 255
            if color[1] <= 0:
                color[1] = 0
            color[2] = color[2] + random.randint(vari_blu * -1, vari_blu)
            if color[2] > 255:
                color[2] = 255
            if color[2] <= 0:
                color[2] = 0
            self.label.def_color = color

        if text != None:
            self.label.text = text

        if time != None:
            self.time_length = time


