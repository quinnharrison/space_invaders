#!/usr/bin/python

import pygame, sys, time, random, serial
from pygame.locals import *
from colors import *
import stars, spaceship, asteroid

FPS = 30
HEIGHT = 647
WIDTH = 400
MAX_STARS = 20
MAX_ASTEROIDS = 6
LEVEL = 0.5
#s = serial.Serial("/dev/tty/ACM0")


def main():
    pygame.init()
    fpsClock = pygame.time.Clock()

    # Create Screen Object
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Space Invaders')

    # Create Game Objects
    liststars = []
    for i in range(MAX_STARS):
        star = stars.Star()
        liststars.append(star)

    asteroid_list = pygame.sprite.Group()
    the_ship = spaceship.Spaceship()

    obj = [the_ship, asteroid_list]

    # create asteroid field
    for i in range(MAX_ASTEROIDS):
      if random.Random() > LEVEL:
        the_asteroid = asteroid.Asteroid()
        asteroid_list.add(the_asteroid)

    while True:
  #      shippos = serial_in()

        # Process Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                the_ship.fire()

        

        # Update game logic
        map(lambda star: star.move(screen), liststars)
        for asteroid in asteroid_list:
          asteroid.move()

       

        
        # Draw updated World
        draw(screen)
        for object in obj:
            object.draw(screen)

        fpsClock.tick(FPS)

def serial_in():
    s.write('p')
    l = s.readline()
    x = l.rstrip().split(',')
    velocity = [int(val) for val in x]
    return velocity

def draw(surf):
    #1 Draw the sky with a fill
    surf.fill(BLACK)
    #2 Add the game title
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('Space Invaders', True, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH/2,25)
    surf.blit(textSurfaceObj, textRectObj)

main()
