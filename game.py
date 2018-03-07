#!/usr/bin/python

import pygame, sys, time, random, serial
from pygame.locals import *
from colors import *
import stars, spaceship, asteroid

FPS = 30
HEIGHT = 647
WIDTH = 400
MAX_STARS = 20
MAX_ASTEROIDS = 4
LEVEL = 0.5
s = serial.Serial("/dev/tty/ACM0")


def main():
    pygame.init()
    fpsClock = pygame.time.Clock()

    # Create Screen Object
    screen = pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption('Space Invaders')

    asteroid_group = pygame.sprite.Group()
    dead = []
    
    # Create Game Objects
    liststars = []
    for i in range(MAX_STARS):
        star = stars.Star()
        liststars.append(star)

    #asteroid_list = pygame.sprite.Group()
    the_ship = spaceship.Spaceship()

    for i in range(MAX_ASTEROIDS):
        the_asteroid = asteroid.Asteroid()
        asteroid_group.add(the_asteroid)

    while True:
        #make asteroids
        if(len(asteroid_group)<MAX_ASTEROIDS):
            the_asteroid = asteroid.Asteroid()
            asteroid_group.add(the_asteroid)

        velocity = serial_in()
        the_ship.Vx = velocity(0)
        the_ship.Vy = velocity(1)

        # Process Events
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit
                sys.exit()                
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
                elif event.key == pygame.K_SPACE:
                    the_ship.fire()
                    
        if len(dead) > 0:
            end_game(screen)
            pygame.quit
            sys.exit()
        else:
             # Update game logic
            map(lambda star: star.move(screen), liststars)
            pygame.sprite.groupcollide(the_ship.phasor_list, asteroid_group, True, True)
            for rock in asteroid_group:
                if rock.off_screen:
                    rock.kill
            dead = pygame.sprite.spritecollide(the_ship, asteroid_group, True)
            #draw world
            asteroid_group.update()
            the_ship.update()
        
            # Draw updated World
            draw(screen)
            the_ship.draw(screen)
            asteroid_group.draw(screen)
            pygame.display.update()
        fpsClock.tick(FPS)
    
    


def end_game(surf):
    draw(surf)
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    textSurfaceObj = fontObj.render('GAME OVER', True, WHITE)
    textRectObj = textSurfaceObj.get_rect()
    textRectObj.center = (WIDTH/2,HEIGHT/2)
    surf.blit(textSurfaceObj, textRectObj)
    pygame.display.update()
    time.sleep(2.0)
    
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
