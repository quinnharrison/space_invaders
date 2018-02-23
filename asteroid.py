#!/usr/bin/python
import pygame
from colors import *
from random import randrange

class Asteroid(pygame.sprite.Sprite):
	#create asteroid object and give it initial position and velocity
	def __init__(self):
          super(Asteroid, self).__init__()
          self.Vy = randrange(1,10) #random y inital velocity
          self.Vx = randrange(-2,2)
          self.image = pygame.image.load('asteroid.png') #creates surface
          self.image = pygame.transform.scale(self.image, (10, 10))
          self.rect = self.image.get_rect()
          self.rect.center=(randrange(10,390),0)
          
        def move(self):
          self.rect = self.rect.move(self.Vx, self.Vy)

	#draw asteroid on surface
	def draw(self, surf):
          surf.blit(self.image, self.rect)
