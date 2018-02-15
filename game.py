#!/usr/bin/python

import pygame, sys, time, random, serial
from pygame.locals import *

FPS = 30
s = serial.Serial("/dev/tty/ACM0")

def main():
    pygame.init()
    
    
