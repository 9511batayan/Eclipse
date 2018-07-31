'''
Created on 2018/07/31

@author: NRL_User
'''

class MobileSensorNode(object):

    def __init__(self, Start_x,Start_y):
        self.current_x=Start_x
        self.current_y=Start_y

    def getx(self):
        return self.current_x

    def gety(self):
        return self.current_y

    def current_com_power_consum(self):
        self.Eelec=50 #nJ/bit
        self.e_amp=100 #pJ/bit/m^2
        self.bit_size=0.5*1000000 #0.5byte
        Et=(self.Eelec*self.bit_size)+(self.e_amp*self.bit_size)
        Er=self.Elec*self.bit_size
        return Et+Er

    def current_move_power_consum(self):
        v=5.0
        return v

    def init_stateofcharge(self,soc):
        return self.soc

    def state_of_Charge(self,value):
        SOC -=
        return SOC