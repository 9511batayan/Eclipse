#!/usr/local/bin/python
# -*- coding: utf-8 -*-

#pygameシミュレータコード
'''
import pygame
from pygame.locals import *
import sys
from contrl import *

def draw():
    while(1):
            pygame.display.update()
            finised_event()

def main():
    start_event()

    draw()

if __name__ == '__main__':
    main()
'''

'''
グラフ上にプロットを表示し、ランダム移動させる
'''
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import math
import random as rd
from MSNs import *
from power_management import *
from animation import *

def move():

    pos_r[0] +=1
    pos_r[1] +=1
    if(pos_r[0]==40 and pos_r[1]==40):
        pos_r[0]=reader.getx()
        pos_r[1]=reader.gety()

# 更新する内容
def update(i):

    plt.cla()
    # グラフの目盛範囲設定
    ax.set_xlim([0, 40])
    ax.set_ylim([0, 40])
    ax.grid()

    move()

    ax.scatter(pos_r[0],pos_r[1],color='red')
    ax.scatter(pos_s[0],pos_s[1],color='blue')

reader=MSNs(4,1,1)
pos_r=[reader.getx(),reader.gety()]
#print(reader.id)
bs=MSNs(0,1,1)
pos_s=[bs.getx(),bs.gety()]

fig =  plt.figure()
    # グラフを中央に表示
ax = fig.add_subplot(1,1,1)
    # アニメーション作成
ani = animation.FuncAnimation(fig, update,frames = 360, interval = 1)
plt.show()

