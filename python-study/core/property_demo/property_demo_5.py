#encoding:gbk

"""
property�޸ķ����÷���
1.����ʹ��property���η�
2.x.setter��x.deleter�������Ե����ú�ɾ������
"""

class Parrot:  
    def __init__(self):  
        self._voltage = 100000  
  
    @property  
    def voltage(self):  
        """Get the current voltage."""  
        return self._voltage  

def test_func1():
    pass
    # instance  
    p = Parrot()  
    # similarly invoke "getter" via @property  
    print p.voltage  
    # update, similarly invoke "setter"  
    p.voltage = 12
    print p.voltage

    
if __name__ == '__main__':
    test_func1()
    #test_func2()


