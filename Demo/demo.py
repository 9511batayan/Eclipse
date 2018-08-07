#coding=UTF-8
'''
Created on 2018/05/30

@author: NRL_User
'''


import numpy as np
import matplotlib.animation as animation
import matplotlib.pyplot as plt

fig = plt.figure()
x = np.arange(0, 10, 0.1)

ims = []
for a in range(50):
    y = np.sin(x - a)
    im = plt.plot(x, y, "r")
    ims.append(im)

ani = animation.ArtistAnimation(fig, ims)
plt.show()