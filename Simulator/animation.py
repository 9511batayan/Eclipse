'''
Created on 2018/08/06

@author: NRL_User
'''
import matplotlib.pyplot as plt
class Animation(object):
    '''
    classdocs
    '''


    def __init__(self, fig):
        self.fig=plt.figure()

    def graph_axis(self,min_x,max_x,min_y,max_y):
        self.now_min_x=min_x
        self.now_max_x=max_x
        self.now_min_y=min_y
        self.now_max_y=max_y

