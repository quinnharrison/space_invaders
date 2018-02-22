import pygame, sys
from random import randrange
from pygame.locals import *
from colors import *

WIDTH = 400
HEIGHT = 648

class Star:
    def __init__(self):
        self.x = randrange(0,WIDTH - 1)
        self.y = randrange(0,HEIGHT - 1)
        self.vy = 2
        self.star = (self.x,self.y)

    def move(self, screen):
        self.y += self.vy # just change star pixel position by vy
        if(self.y >= HEIGHT):# Return the star if it crosses bottom border
            self.y = 0
            self.x = randrange(0,WIDTH-1)
        self.star = (self.x,self.y)
        screen.set_at(self.star,(WHITE))
        pygame.display.update()


        
