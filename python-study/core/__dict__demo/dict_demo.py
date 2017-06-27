#encoding:gbk

import datetime

# 这个文件讲__dict__相关的特性。
class Debug(object):
    def trace(self,msg):
        nt=datetime.datetime.now()
        print "[%s]:%s" % (nt.strftime('%Y%m%d%H%M%S'), msg)
debug = Debug()

# __dict__的作用没有那么大。用来维护实例的局部属性。
class Base1(object):
    pass
    __dict__={}  # 只会影响到Base1类的实例的__dict__属性，影响不到Base1类的__dict__属性。
    v__dict__={}
    @property
    def w__dict__(self):
        print 1
        return {}

def test_func1():
    b=Base1()
    b.x=2
    debug.trace(['b.x:', b.x])
    #b.__dict__()
    debug.trace(['b.__dict__:', b.__dict__, type(b.__dict__), dir(b)])
    debug.trace(['Base1.__dict__:', Base1.__dict__, Base1.v__dict__])
    
class Dog(object):
    pass

def func2():
    d=Dog()
    d.x=2
    # 实例的__dict__属性是字典类型
    print 'd.__dict__:', d.__dict__
    print 'type(d.__dict__):', type(d.__dict__)
    # 类的__dict__属性是dictproxy类型
    print 'Dog.__dict__:', Dog.__dict__
    print 'type(Dog.__dict__):', type(Dog.__dict__)
    print 'Dog.__dict__["__dict__"]:',  Dog.__dict__["__dict__"], type(Dog.__dict__["__dict__"])
    #print 'Dog.__dict__.__dict__:', Dog.__dict__.__dict__
    
    # 删除了 d.__dict__里面的属性x, 也就相当于删除了d的x属性
    del d.__dict__['x']
    print 'd.__dict__:', d.__dict__
    
    # 设置__dict__的值相当于更新d的属性
    d.__dict__={'a':1, 'b':2}
    print 'd.a,d.b:', d.a, d.b
    
    # 类的__dict__属性是不可行的， 前面的打印信息表明Dog.__dict__是一个属性， 
    #Dog.__dict__={'s':1, 'd':2}
    
def func3():
    # NOTE：zhouf, 170315, 类型的__dict__属性的类型是dictproxy， 这个属性是不可写的
    # 可以把这个属性当成字典来用， 但是其实不是字典类型. 它的值包含__dict__字段。
    print 'Dog.__dict__:', Dog.__dict__, type(Dog.__dict__)
    # NOTE： zhouf, 170315, 万物皆对象，下面的语句就涉及到 attribute， type, class, object
    #  类的类型是类型， 类型的类型也是类型， 类型就是万物之始了。 attribute应该是Python语言的一个内建事物。
    print Dog.__dict__['__dict__'], type(Dog.__dict__['__dict__']), Dog, Dog()
    # NOTE：zhouf, 170315, 下面这个语句会报错. 类型的实例（类）的__dict__属性是不可写的。
    #Dog.__dict__={}
    Dog.a=1
    d=Dog()
    print 'd.a:', d.a  # d并没有a这个属性， 之所以可以访问a这个属性， 是因为d是Dog的实例。d的属性访问机制决定的
    # 接上： d本身没有这个属性，于是就向它所属的类去找有没有这个属性。
    print 'd.__dict__:', d.__dict__

def func4():
    class Dog(object):
        def run(self):pass
    print 'Dog.__dict__:', Dog.__dict__    
    
    
if __name__ == "__main__":
    #test_func1()
    func4()
    
