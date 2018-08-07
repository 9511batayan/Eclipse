import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
from pygame.locals import *
import sys

def start_event():
    screen_size=[600,500]
    pygame.init()
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Simulation")

def finised_event():
     for event in pygame.event.get():
                if event.type=QUIT:
                    pygame.quit()
                    sys.exit()