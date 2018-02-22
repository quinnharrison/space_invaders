#!/usr/bin/python
import pygame
from pygame.locals import *
from colors import *

class Spaceship(pygame.sprite.Sprite):
    def __init__(self):
        super(Spaceship, self).__init__() #call the parent class contructor
        self.Vx = 0
        self.Vy = 0
        self.image = pygame.image.load('spaceship.png') #creates surface
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.image.set_colorkey(WHITE) #set 'colorkey' of surface, this lets the black parts of the picture be transparent
        self.rect = self.image.get_rect()
        self.rect.center = (200, 600) #initializes center of the spaceship


    def move(self, time):
        self.rect.move(self.Vx*time, -1*self.Vy*time)

    def isHit(self):
        #TODO
        return false
    def fire(self, phasor_list):
        phasor = Phasor(self.rect.midtop) #instanciates a new phasor at the top/middle of the spaceship
        phasor_list.add(phasor)
        
    def draw(self, surf):
        #draw image on surface
        surf.blit(self.image, self.rect)

class Phasor(pygame.sprite.Sprite):
    def __init__(self, x, y): #pass in the top middle of the spaceship
        super(Phasor, self).__init__()
        self.image = pygame.Surface([5,20])
        self.image.fill(PHASOR)
        self.rect = self.image.get_rect()
        self.rect.midbottom(x,y)
    def move(self): #moves 3 pixels per call
        self.rect.y -= 3
