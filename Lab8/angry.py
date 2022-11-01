import pygame
from pygame.draw import *

pygame.init()

FPS = 30
screen = pygame.display.set_mode((400, 400))

circle(screen, (255, 204, 0), (200, 175), 100)
rect(screen, (0, 0, 0), (150, 220, 100, 20), 0)
circle(screen, (255, 0, 0), (160, 160), 20)
circle(screen, (0, 0, 0), (160, 160), 10)
circle(screen, (255, 0, 0), (235, 160), 15)
circle(screen, (0, 0, 0), (235, 160), 7)
line(screen, (0, 0, 0), (150, 120), (180, 140), 20)
line(screen, (0, 0, 0), (220, 140), (250, 120), 20)

pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()