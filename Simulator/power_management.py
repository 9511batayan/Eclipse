'''
Created on 2018/08/07

@author: NRL_User
'''
import math


def now_transmitpower_consum(dis):
    Eelec=50/math.pow(10,9) #50nJ/bit
    e_amp=100/math.pow(10,12) #100pJ/bit/m^2
    bit_size=0.5*math.pow(10,6) #0.5byte
    Et=bit_size(Eelec+e_amp*bit_size*dis*dis)
    Et=(Eelec*bit_size)+(e_amp*bit_size*dis*dis)
    return Et

def now_receivepower_consum():
        Eelec=50/math.pow(10,9) #nJ/bit
        e_amp=100/math.pow(10,12) #pJ/bit/m^2
        bit_size=0.5*math.pow(10,6) #0.5byte
        Er=Eelec*bit_size
        return Er

class MyClass(object):
    def __init__(self, params):
        '''
        Constructor
        '''
    def now_commu_consum(self,d):
        Et=now_transmitpower_consum(d)
        Er=now_receivepower_consum()
        return Et+Er

    def current_move_power_consum(self,v,dis):
        self.Em=v*dis
        return self.Em

    def init_stateofcharge(self):
        self.SOC=100
        return self.soc

    def print_SOC(self,soc):
        return print(soc)