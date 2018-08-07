'''
Created on 2018/07/31

@author: NRL_User
'''

import pygame
from pygame.locals import *
import sys
class MSNs(object):

    def __init__(self, id,Start_x,Start_y):
        self.id=id
        self.current_x=Start_x
        self.current_y=Start_y

    def shape_character(self,init_screen,color,):
        self.screen_info=init_screen
        self.color=color
        pygame.draw.circle(self.screen_info,self.color,(self.current_x,self.current_y),10,0)

    def getx(self):
        return self.current_x

    def gety(self):
        return self.current_y

'''
    def state_of_Charge(self,value):
        SOC -=
        return SOC
        '''