from Constants import *
from random import randint as rnd
import pygame
import Object


class TargetType(Object.ObjectType):
    def __init__(self, screen, x=0, y=0, vx=0, vy=0):
        super().__init__()
        self.points = 1
        self.r = rnd(MIN_R_TARGET, MAX_R_TARGET)
        if x == 0 and y == 0:
            self.x = rnd(self.r, WIDTH - self.r)
            self.y = rnd(20, HEIGHT - self.r - 40)
        else:
            self.x = x
            self.y = y
        self.color = RED
        self.screen = screen
        self.vx = vx
        self.vy = vy

    def draw(self):
        if self.color != WHITE:
            pygame.draw.circle(
                self.screen,
                BLACK,
                (self.x, self.y),
                self.r
            )
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r * 0.9
        )




