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

                self.x = 0
                self.y = 0

                self.image = pygame.image.load('asteroid.png')
                self.image = pygame.transform.scale(self.image, (50,50))
                self.isHit = False
                self.rect = self.image.get_rect()
                
                pos = randrange(1,3)
                if pos == 1:
                        self.x = randrange(0,WIDTH)
                        self.rect.bottom = 0
                        mag = choice([-1, 1])
                elif pos == 2:
                        self.rect.right = 0 
                        self.y = randrange(0,HEIGHT)
                        mag = 1
                elif pos == 3:
                        self.rect.left = WIDTH 
                        self.y = randrange(0,HEIGHT)
                        mag = -1
                
                self.vy = randint(1,5) * mag
                self.vx = randint(1,2) * mag
                             
                
        def isHit(self):
                #TODO
                return false
        
	#create how asteroid will move with time
	def update(self):
                if not self.isHit:
                        self.x += self.vx
                        self.y += self.vy
                        self.rect.center=(self.x,self.y)
                        if(self.rect.right < 0 or self.rect.left > WIDTH or self.rect.top < 0 or self.rect.bottom > HEIGHT):
                                pos = randrange(1,3)
                                if pos == 1:
                                        self.x = randrange(0,WIDTH)
                                        self.rect.bottom = 0
                                        mag = choice([-1, 1])
                                elif pos == 2:
                                        self.rect.right = 0 
                                        self.y = randrange(0,HEIGHT)
                                        mag = 1
                                elif pos == 3:
                                        self.rect.left = WIDTH 
                                        self.y = randrange(0,HEIGHT)
                                        mag = -1
                
                                self.vy = randint(1,5)
                                self.vx = randint(1,2) * mag
                       

        def draw(self,surf):
                surf.blit(self.image, self.rect)


