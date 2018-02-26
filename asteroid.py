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
                pos = randint(1,3)
                if pos == 1:
                        self.x = randrange(0,WIDTH)
                        self.y = 0
                        mag = randint(-1,1)
                elif pos == 2:
                        self.x = 0 
                        self.y = randrange(0,HEIGHT)
                        mag = 1
                elif pos == 3:
                        self.x = WIDTH 
                        self.y = randrange(0,HEIGHT)
                        mag = -1
                
                self.vy = randint(1,5) * mag
                self.vx = randint(1,5) * mag
            
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
                                pos = randrange(1,3)
                                if pos == 1:
                                        self.x = randrange(0,WIDTH)
                                        self.y = 0
                                        mag = randint(-1,1)
                                elif pos == 2:
                                        self.x = 0 
                                        self.y = randrange(0,HEIGHT)
                                        mag = 1
                                elif pos == 3:
                                        self.x = WIDTH 
                                        self.y = randrange(0,HEIGHT)
                                        mag = -1
                
                                        self.vy = randint(1,5) * mag
                                        self.vx = randint(1,2) * mag
                        else:
                                surf.blit(self.image, self.rect)
                        
                else:
                        #TODO
                        pass


