#!/usr/local/bin/python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
import sys
from MSNs import *
#import numpy as np
#import matplotlib.pyplot as plt

#import random
#from MSNs import *

screen_size=[800,600]
red=(255,0,0)
black=(0,0,0)
white=(255,255,255)
'''
def update():

    return
'''
def main():
    pygame.init()
    screen=pygame.display.set_mode(screen_size)
    pygame.display.set_caption("Simulation")

    robot=MSNs(200,200)
    sn1=MSNs(100,100)

    robot_x=robot.getx()
    robot_y=robot.gety()
    sn1_x=sn1.getx()
    sn1_y=sn1.gety()

    while (1):
        screen.fill(white)
        #イベント処理
        #update(screen):
        robot.shape_character(screen, red)
        sn1.shape_character(screen, black)
        pygame.display.update()
        pygame.time.wait(30)

        for event in pygame.event.get():
            if event.type == QUIT:  # 閉じるボタンが押されたら終了
                pygame.quit()       # Pygameの終了(画面閉じられる)
                sys.exit()

if __name__ == '__main__':
    main()