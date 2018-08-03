'''
Created on 2018/08/03

@author: 皓司
'''
from MobileSensorNode import MobileSensorNode
import math

def main():
    robot=MobileSensorNode(5,5)
    x=robot.getx()
    y=robot.gety()
    for i :
        dis=math.sqrt(i*i+y*y)
        output=robot.current_com_power_consum(dis)

        i +=2.5
        if(i>=10):
            break

        print(output)

if __name__ == '__main__':
    main()