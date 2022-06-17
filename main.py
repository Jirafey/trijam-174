import pygame
from sys import exit

pygame.init()

screen = pygame.display.set_mode((500, 500), pygame.RESIZABLE)
clock = pygame.time.Clock()

run = True
while run:
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            run = False
            exit()

    pygame.display.update()
    clock.tick(60)
