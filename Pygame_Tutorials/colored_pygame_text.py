import pygame
import time
import custom_pygame_assets
W, H = 1600, 900
fps = 60

display = pygame.Surface((W, H))
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption('colored_text')
clock = pygame.time.Clock()


pygame.init()

run = True

text_button = custom_pygame_assets.Lable('Test', 40, 'purple', 'gray', 'white', (W/1.5, H/1.5), is_centered=True, is_clickable=True, bold_text=True)
text_lable_1 = custom_pygame_assets.Lable('Version: 0.0.1', 15, 'gray', 'gray', 'white', (5, 5), is_clickable=False)
text_lable_2 = custom_pygame_assets.Lable('HP ', 20, 'purple', 'gray', 'white', (5, 100), bold_text=True)
text_lable_3 = custom_pygame_assets.Lable('[//////////////.....]', 20, 'red', 'white', 'blue', (50, 100), is_clickable=True)
text_lable_7 = custom_pygame_assets.Lable(r'----------------------------------------', 20, 'white', 'white', 'blue', (5, 180), is_clickable=False)
text_lable_4 = custom_pygame_assets.Lable('Blob', 20, 'purple', 'gray', 'white', (5, 200))
text_lable_5 = custom_pygame_assets.Lable(r'Blobs will cause trouble everywhere they can,', 20, 'white', 'white', 'blue', (5, 230), is_clickable=False)
text_lable_6 = custom_pygame_assets.Lable(r'resulting in chaos around the farlands.', 20, 'white', 'white', 'blue', (5, 250), is_clickable=False)




while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # main loop

    if text_button.draw_text(screen):
        print('test')
    text_lable_1.draw_text(screen)
    text_lable_2.draw_text(screen)
    text_lable_3.draw_text(screen)
    if text_lable_4.draw_text(screen):
        print('blob')
    text_lable_5.draw_text(screen)
    text_lable_6.draw_text(screen)
    text_lable_7.draw_text(screen)

    clock.tick(fps)

    display.blit(screen, (0, 0))
    pygame.display.update()
pygame.quit()