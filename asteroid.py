#!/usr/bin/python
import pygame
from pygame.locals import *
from colors import *
from random import *

WIDTH = 400
HEIGHT = 647

class Asteroid(pygame.sprite.Sprite):
	#create asteroid object and give it initial position and velocity
	def __init__(self):
                super(Asteroid, self).__init__()
                self.x = randrange(10,WIDTH-10)
                self.y = randrange(10,HEIGHT-10)
                self.vy = uniform(-5,5)
                self.vx = uniform(-5,5)
            
                self.image = pygame.image.load('asteroid.png')
                self.image = pygame.transform.scale(self.image, (50,50))
                self.isHit = False
                self.rect = self.image.get_rect()
                self.asteroid_list = pygame.sprite.Group()

        def isHit(self):
                #TODO
                return false
        
	#create how asteroid will move with time
	def move(self,surf):
                if not self.isHit:
                        self.x += self.vx
                        self.y += self.vy
                        self.rect.center=(self.x,self.y)
                        if(self.x < 0 or self.x > WIDTH or self.y < 0 or self.y > HEIGHT):
                                self.x = randrange(10,WIDTH-10)
                                self.y = randrange(10,HEIGHT-10)
                                self.vy = randrange(1,10)
                                self.vx = randrange(1,10)
                        else:
                                surf.blit(self.image, self.rect)
                        
                else:
                        #TODO
                        pass
