#encoding:gbk

# ������__all__Ҳ���Ƕ��������ģ��ͨ��from m import * ��ʽ�ܹ����������
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