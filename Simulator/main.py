#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
from contrl import *

screen_size=[600,500]

def draw():
    while(1):
            pygame.display.update()
            finised_event()


def main():
    pygame.init()
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Simulation")

    draw()

if __name__ == '__main__':
    main()