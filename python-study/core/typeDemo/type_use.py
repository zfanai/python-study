#!usr/bin/env python
# -*- coding: gbk -*

class Debug(object):
    def __init__(self):
        pass
    def trace(self, *msg):
        print "trace:", msg
debug=Debug()

class AnimalMeta(type):
    '''
    def __new__(cls, name, this_bases, d):
        debug.trace('__new__:', name, this_bases, d)
        return type.__new__(cls, name, this_bases, d)'''
    def __new__(cls, name, this_bases, d):
        debug.trace('__new__:AnimalMeta')
        return type.__new__(cls, name, this_bases, d)
        
        
    def __init__(cls, classname, bases, fields):
        debug.trace('__init__:', classname, bases, fields)
        type.__init__(cls, classname, bases, fields)

class AnimalClass(object):
    pass

def with_metacls(meta, *base):
    class metaclass(meta):
        def __new__(cls, name, this_bases, d):
            debug.trace('__new__:', name, this_bases, d)
            if this_bases is None:
                return type.__new__(cls, name, (), d)
            return meta(name, base, d)
    # ��Ȼ���Ǵ������͵��࣬������__new__���������п����ְ����ͻ��������͵ĸ��ࡣ        
    #return  metaclass('Animal', base, {})
    return  metaclass('temporary_class', None, {})
#    
def func1():
    #AnimalCls=AnimalMeta('Animal', (object,), {})
    AnimalCls=with_metacls(AnimalMeta, AnimalClass)
    # ����һ����ʱ����ʵҲ�Ǳ�ʾ����һ�������
    debug.trace('before Dog')
    class Dog(AnimalCls):
        pass
        #color=2
    debug.trace('before Taidi')
    class Taidi(Dog):
        pass
        
# type������ΪԪ��Ļ�����ʹ�õġ�
# AnimalMeta ��type�����࣬ Ҳ����ͨ�� AnimalMeta��������������һ���ࡣ
def func2():
    # 
    class AnimalMeta(type):
        def __new__(cls, name, bases, attrs):
            debug.trace('AnimalMeta,__new__')
            return type.__new__(cls, name, bases, attrs)
    
    def with_metaclass(meta, *bases):
        """Create a base class with a metaclass."""
        # This requires a bit of explanation: the basic idea is to make a dummy
        # metaclass for one level of class instantiation that replaces itself with
        # the actual metaclass.
        class metaclass(meta):
            def __new__(cls, name, this_bases, d):
                debug.trace('metaclass,__new__')
                return meta(name, bases, d)
        # type��һ������, __new__��һ��ʵ�������� ��ʵӦ��˵��Python��Բ�ͬ�ķ�����󶨲�ͬ�Ķ���
        # ��ͨ��ʵ��������ʵ�������෽�������Ͷ����ࣩ��    
        return type.__new__(metaclass, 'temporary_class', (), {})
    AnimalCls=with_metaclass(AnimalMeta)
    debug.trace('AnimalCls:', AnimalCls)
    class Dog(AnimalCls):
        def __init__(self, name):
            self.name=name
    d=Dog('kkk')
    print d
        
def func3():
    class AnimalMeta(type):
        # __new__�ṹ�� AnimalMeta ���Ԫ���ʵ���� Ԫ���ʵ��������
        def __new__(cls, name, bases, attrs):
            debug.trace('AnimalMeta,__new__')
            return type.__new__(cls, name, bases, attrs)
    
    def run(self):
        print 'run'
    dog_cls=AnimalMeta('Dog', (object,), {'a':1, 'run':run})
    d=dog_cls()
    d.run()
    
if __name__=='__main__':
    #func2()
    func3()