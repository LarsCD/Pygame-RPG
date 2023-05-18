import pygame
import time
import custom_pygame_assets
W, H = 1000, 600
fps = 60

display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('colored_text')
clock = pygame.time.Clock()


pygame.init()

run = True

text_button = custom_pygame_assets.Lable('Test', 40, 'white', 'green', (W/2, H/2), is_centered=True, is_clickable=True, bold_text=True)
text_lable_1 = custom_pygame_assets.Lable('Version: 0.0.1', 15, 'white', 'green', (5, 5), is_clickable=False)
text_lable_2 = custom_pygame_assets.Lable('HP ', 20, 'white', 'purple', (5, 135), bold_text=True)
text_lable_3 = custom_pygame_assets.Lable('[//////////////.....]', 20, 'red', 'white', (50, 135))



while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # main loop

    if text_button.draw_text(screen):
        print('clicked')
    text_lable_1.draw_text(screen)
    text_lable_2.draw_text(screen)
    text_lable_3.draw_text(screen)

    clock.tick(fps)

    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()