#encoding:gbk

"""
property修改符的用法：
1.
"""

class Rabbit1(object):
    def __init__(self,name):
        self._name = name
    @classmethod
    def newClass(cls):
        return 'abc',cls,Rabbit('')
    
    # 如果只有property修饰的话，这个属性只有只读属性。
    @property
    def name(self):
        return self._name

class Rabbit2(object):
    def __init__(self,name):
        self._name = name
    @classmethod
    def newClass(cls):
        return 'abc',cls,Rabbit('')
    
    @property
    def name(self):
        return self._name
    
    # 给这个属性添加可写特性。
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


