#!/usr/bin/python
import pygame
from colors import *

#give asteroid inheritance from sprite 
class Asteroid(pygame.sprite.Sprite):
	#create asteroid object and give it initial position and velocity
	def __init__(self):
          self.x = random.randint(10,390)
          self.y = 0
          self.vy = random.randint(1,10)
	
	#create how asteroid will move with time
	def move(self,time):
	  # Move in y direction
          self.y = self.y + self.vy*time


	#draw asteroid on surface
	def draw(self, surf):
	  self.asteroid = pygame.Rect((0,0,10,10))
          self.asteroid.center=(self.x,self.y)
          pygame.draw.rect(surf,(ASTEROID_COLOR),self.asteroid)
