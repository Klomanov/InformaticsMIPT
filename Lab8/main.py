import pygame
from pygame.draw import *
from random import randint
from dictionary import *
import numpy as np


def new_object():
    """Рисует новый шарик """
    coord = [randint(MAX_R, WIDTH - MAX_R), randint(MAX_R, HEIGHT - MAX_R)]
    r = randint(MIN_R, MAX_R)
    vel = [randint(MIN_SPEED, MAX_SPEED), randint(MIN_SPEED, MAX_SPEED)]
    color = COLORS[randint(0, 5)]
    circle(screen, color, coord, r)
    objects.append([])
    objects[-1].append(coord)
    objects[-1].append(r)
    objects[-1].append(vel)
    objects[-1].append(color)
    if it_is_time_for_special_target():
        objects[-1].append(True)
    else:
        objects[-1].append(False)  # Is special?


def is_catch(e, coord, r):
    """Проверяет, лежит ли эвент внутри круга"""
    return np.sqrt((coord[0] - e.pos[0]) ** 2 + (coord[1] - e.pos[1]) ** 2) <= r


def display_score():
    """Отображает счет на экране"""
    text_surface = my_font.render(f'{score}', False, (0, 0, 0))
    screen.blit(text_surface, (0, 0))


def move_objects():
    """Двигает шары"""
    screen.fill(WHITE)
    for object in objects:
        if not (object[1] <= object[0][0] <= WIDTH - object[1]):
            object[2][0] = - object[2][0]
        if not (object[1] <= object[0][1] <= HEIGHT - object[1]):
            object[2][1] = - object[2][1]
        object[0][0] += object[2][0]
        object[0][1] += object[2][1]
        if object[4]:
            object[3] = COLORS[randint(0, 5)]
        circle(screen, object[3], (object[0][0], object[0][1]), object[1])


def it_is_time_for_special_target():
    """Время ли для специальной цели?"""
    return randint(0, 100) <= CHANCE_SPECIAL_TARGET * 100


pygame.init()

pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)
clock = pygame.time.Clock()
pygame.display.update()

score = 0
objects = []
for i in range(MAX_OBJECTS):
    new_object()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for object in objects:
                if is_catch(event, object[0], object[1]):
                    if object[4]:
                        score += 5
                    else:
                        score += 1
                    objects.remove(object)
                    new_object()

    move_objects()
    display_score()
    pygame.display.update()

pygame.quit()
