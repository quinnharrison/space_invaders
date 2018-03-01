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

    all_sprites = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()
    
    # Create Game Objects
    liststars = []
    for i in range(MAX_STARS):
        star = stars.Star()
        liststars.append(star)

    #asteroid_list = pygame.sprite.Group()
    the_ship = spaceship.Spaceship()

    all_sprites.add(the_ship)

    for i in range(MAX_ASTEROIDS):
        the_asteroid = asteroid.Asteroid()
        all_sprites.add(the_asteroid)
        asteroid_group.add(the_asteroid)

    while True:
  #      shippos = serial_in()

        # Process Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                the_ship.fire()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    the_ship.Vy -= 1
                    if the_ship.Vy < -5:
                        the_ship.Vy = -5
                elif event.key == pygame.K_DOWN:
                    the_ship.Vy += 1
                    if the_ship.Vy > 5:
                        the_ship.Vy = 5
                elif event.key == pygame.K_LEFT:
                    the_ship.Vx -= 1
                    if the_ship.Vx < -5:
                        the_ship.Vx = -5
                elif event.key == pygame.K_RIGHT:
                    the_ship.Vx += 1
                    if the_ship.Vx > 5:
                        the_ship.Vx = 5

        hits = pygame.sprite.spritecollide(the_ship, asteroid_group, True)

        # Update game logic
        map(lambda star: star.move(screen), liststars)

        all_sprites.update()
       

        # Draw updated World
        draw(screen)
        all_sprites.draw(screen)

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
