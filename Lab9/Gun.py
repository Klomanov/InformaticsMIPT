import math
import pygame
import Constants
import Object
import Ball


class GunType(Object.ObjectType):
    def __init__(self, screen, spawn):
        super().__init__()
        self.screen = screen
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.color = Constants.TANK_COLOR
        self.x = spawn[0]
        self.y = spawn[1]
        self.length = 40
        self.width = 10
        self.r = self.length
        self.vx = 0
        self.vy = 0
        self.invincible = False

    def fire2_start(self, event):
        self.f2_on = 1

    def fire2_end(self):
        """Выстрел мячом.

        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event):
        """Прицеливание. Зависит от положения мыши."""
        if event and event.pos[0] - 20 != 0:
            if event.pos[0] > self.x:
                self.an = math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x))
            elif event.pos[0] < self.x:
                self.an = -(math.pi - math.atan((event.pos[1] - self.y) / (event.pos[0] - self.x)))

    def draw(self):
        pygame.draw.rect(self.screen, self.color, (self.x-20, self.y, 40, 15))
        if self.color == Constants.RED:
            c = Constants.RED
        else:
            c = Constants.BLACK
        pygame.draw.polygon(self.screen, c, [[self.x-45, self.y+15], [self.x+45, self.y+15],
                                                           [self.x+35, self.y+30], [self.x-35, self.y+30]])
        pygame.draw.line(self.screen, self.color,
                         [self.x, self.y],
                         [self.x + self.length * math.cos(self.an), self.y + self.length * math.sin(self.an)],
                         self.width)

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1

    def strike(self, r,  power):
        newBall = Ball.BallType(self.screen, (self.x, self.y), r)
        newBall.strike_ball(self.an, self.f2_power*power, self.vx)
        self.fire2_end()
        return newBall

    def hit(self):
        self.color = Constants.RED
        self.invincible = True




