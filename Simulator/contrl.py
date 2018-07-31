import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import pygame
from pygame.locals import *
import sys

def finised_event():
     for event in pygame.event.get():
                if event.type=QUIT:
                    pygame.quit()
                    sys.exit()