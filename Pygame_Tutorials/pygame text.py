import pygame
import colorama as clr
clr.init()

pygame.init()
clock = pygame.time.Clock()
fps = 60
font = pygame.font.Font('fonts/dogicapixel.ttf', 20)
# create display window
SCREEN_HEIGHT = 500
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Button Demo')


running = True
while running:
    clock.tick(fps)
    screen.fill((202, 228, 241))

    text_1 = font.render('Org:', False, 'black')
    text_2 = font.render(f'HP: [███████████████████......] (15/20)', False, 'black')
    inventory = '  [A]: Attack'
    text_3 = font.render(inventory, False, 'purple')
    screen.blit(text_1, (0, 0))
    screen.blit(text_2, (0, 30))
    screen.blit(text_3, (0, 60))


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

pygame.quit()

