import pygame
from button import Button

# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')

# load button image
start_img = pygame.image.load('button_frame_1.png').convert_alpha()
clicked_img = pygame.image.load('button_frame_1_clicked.png').convert_alpha()


# create buttons
start_button = Button(100, 200, start_img, 0.8)
clicked_button = Button(450, 200, start_img, 0.8)

run = True
while run:

    screen.fill((202, 228, 241))

    if start_button.draw(screen):
        start_button.raw_image = clicked_img
        print('clicked 1')
    if clicked_button.draw(screen):
        print('clicked 2')

    # event handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
pygame.quit()



