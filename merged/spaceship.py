#/usr/bin/python
import pygame
from pygame.locals import *
from colors import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() #call the parent class contructor
        self.Vx = 0
        self.Vy = 0
        self.image = pygame.image.load('spaceship.png') #creates surface
        self.image.set_colorkey(BLACK) #set 'colorkey' of surface, this lets the black parts of the picture be transparent
        self.rect = self.image.get_rect()
        self.rect.center = (200, 629) #initializes center of the spaceship
    def move(self, time):
        self.rect.move(self.Vx*time, -1*self.Vy*time)
        
    def isHit(self):
        #TODO
        return false
    def fire(self):
        #TODO
        pass
    def draw(self, surf):
        #draw image on surface
        surf.blit(self.image, self.rect)
    
