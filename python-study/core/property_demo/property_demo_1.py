#encoding:gbk

"""
property�޸ķ����÷���
1.
"""

class Rabbit1(object):
    def __init__(self,name):
        self._name = name
    @classmethod
    def newClass(cls):
        return 'abc',cls,Rabbit1('')
    
    # ���ֻ��property���εĻ����������ֻ��ֻ�����ԡ�
    @property
    def name(self):
        return self._name

class Rabbit2(object):
    def __init__(self,name):
        self._name = name
    @classmethod
    def newClass(cls):
        return 'abc',cls,Rabbit2('')
    
    @property
    def name(self):
        return self._name
    
    # �����������ӿ�д���ԡ�
    @name.setter
    def name(self,newname):
        self._name= newname

def test_func1():
    pass 
    r = Rabbit1('abc')
    print r
    print r.name
    
    r.name = '1'

def test_func2():
    pass
    r = Rabbit2('abc')
    print r
    print r.name
    
    r.name = '1'
    print r.name
    
if __name__ == '__main__':
    #test_func1()
    test_func2()


