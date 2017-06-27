#encoding:gbk

# 定义了__all__也就是定义了这个模块通过from m import * 形式能够导入的属性
#__all__=['_VER']
_VER=0.2
VER=0.3
_NAME='ddd'

class Car(object):
    def __init__(self):
        self._color=1
car=Car()

for k,v in globals().items():print 'globals:', k 
for k,v in locals().items():print 'locals:', k 