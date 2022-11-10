from Constants import *
import pygame
import math
import Object
import Constants


class BallType(Object.ObjectType):
    def __init__(self, screen: pygame.Surface, spawn, r):
        """ Конструктор класса ball

        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        super().__init__()
        self.screen = screen
        self.x = spawn[0]
        self.y = spawn[1]
        self.r = r
        self.vx = 0
        self.vy = 0
        self.color = BLACK
        self.flex = Constants.FLEX

    def draw(self):
        pygame.draw.circle(
            self.screen,
            self.color,
            (self.x, self.y),
            self.r
        )

    def strike_ball(self, an, power, vx):
        self.vx = vx + power * math.cos(an)
        self.vy = power * math.sin(an)
