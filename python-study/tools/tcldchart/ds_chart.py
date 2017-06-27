#encoding:utf8

import matplotlib.pyplot as plt
import numpy as np

class Debug(object):
    def trace(self, msg):
        print 'trace:',msg
debug=Debug()

# 最基本的画图功能。
def func1():
    plt.plot([1,2,3,4])
    plt.ylabel('Some numbers')
    plt.show()

def func2():
    f=open('ds_data.json', 'r')
    strdata=f.read(-1)
    exec 'jo='+strdata
    #debug.trace(['jo:', jo])
    debug.trace(jo['glucose_unit'])
    sgdata=jo['sensor_glucose']
    debug.trace(['size:', len(sgdata)])
    x=[]
    y=[]
    for p in sgdata:
        x.append(p[0])
        y.append(p[1])
    # 
    plt.plot(x,y)
    plt.show()
if __name__ == '__main__':
    func2()