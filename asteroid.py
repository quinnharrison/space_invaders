#!/usr/bin/python
import pygame
from colors import *
from random import randrange

class Asteroid(pygame.sprite.Sprite):
	#create asteroid object and give it initial position and velocity
	def __init__(self):
          self.x = randrange(10,390)
          self.y = 0
          self.vy = randrange(1,10)
          self.vx = 0
          self.asteroid = pygame.Rect((0,0,10,10))
	
	#create how asteroid will move with time
	def move(self,time):
	  # Move in y direction
          self.y = self.y + self.vy*time
	  # No motion in x direction (vx == 0)
          self.x = self.x + self.vx*time

	#draw asteroid on surface
	def draw(self, surf):
          self.asteroid.center=(self.x,self.y)
          pygame.draw.rect(surf,(ASTEROID_COLOR),self.asteroid)
