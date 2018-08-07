'''
Created on 2018/08/06

@author: NRL_User

グラフ上にプロットを表示し、ランダム移動させる
'''
import math
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
import random as rd

# 更新する内容
def update(i):

    plt.cla()
    # グラフの目盛範囲設定
    ax.set_xlim([0, 10])
    ax.set_ylim([0, 10])

    pos_r[0] +=rd.random()
    pos_r[1] +=rd.random()
    ax.scatter(pos_r[0],pos_r[1],color='red')
    ax.scatter(pos_s[0],pos_s[1],color='blue')

    ax.grid()

pos_r=[2,2]
pos_s=[4,4]

fig =  plt.figure()
    # グラフを中央に表示
ax = fig.add_subplot(1,1,1)
    # アニメーション作成
ani = animation.FuncAnimation(fig, update,frames = 360, interval = 1)

plt.show()
