import random

import Object
import Target
import Constants
import pygame


class BomberType(Object.ObjectType):
    def __init__(self, screen):
        super(BomberType, self).__init__()
        self.screen = screen
        self.r = 40
        self.x = random.randint(self.r, Constants.WIDTH - self.r)
        self.y = Constants.BOMBER_SPAWN_Y
        self.vx = 5
        self.vy = 0

    def strike(self):
        return Target.TargetType(self.screen, self.x, self.y, self.vx*random.random(), 0)

    def draw(self):
        pygame.draw.ellipse(self.screen, Constants.GREY, (self.x - self.r, self.y,
                                                          2*self.r, self.r))
        pygame.draw.ellipse(self.screen, Constants.BLUE, (self.x - 0.5*self.r, self.y-10,
                                                          self.r, self.r-10))


