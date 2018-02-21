#/usr/bin/python
import pygame
from pygame.locals import *
from colors import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.Vx = 0
        self.Vy = 0
        self.X = 200 #initial position
        self.Y = 629 #initial postiion
        self.image = pygame.image.load('spaceship.png')
        self.r = self.image.get_rect() #get the attributes for constructor
    def move(self):
        #TODO
        pass
    def isHit(self):
        #TODO
        return false
    def fire(self):
        #TODO
        pass
    def draw(self):
        #TODO
        pass
    
