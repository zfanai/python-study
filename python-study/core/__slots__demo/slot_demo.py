#encoding:gbk

import datetime

class Debug(object):
    def trace(self,msg):
        nt=datetime.datetime.now()
        print "[%s]:%s" % (nt.strftime('%Y%m%d%H%M%S'), msg)
debug = Debug()

"""
正常情况下，Python允许动态绑定属性，既可以给实例绑定属性，也可以给类绑定属性，
给实例绑定属性只对某个实例起作用，给类绑定属性可以对该类的所有实例起作用，
但是有时候希望限制绑定属性的范围，就可以使用__slots__属性定义可以动态绑定的属性的元组
__slots__=("name","age")
表示只允许动态绑定name属性和age属性

NOTE:170316, 上面的认识是不对的， 给类绑定属性就只是给类绑定了一个属性， 并不是给这个类的实例都绑定了这个属性，
只是类的实例可以访问这个属性（在自身没有定义这个属性的情况下，这个有对象的属性访问的内部机制实现的，如果实例没有某个属性，就向它的类搜索这个属性。）
"""
class Base1(object):
    v = 1
    def __init__(self):
        pass

def test_func1():
    b = Base1()
    print b.__dict__
    b.x = 2
    print b.__dict__

class Base2(object):
    __slots__ = ('y')
    v = 1
    a=2
    def __init__(self):
        pass

def test_func2():
    b = Base2()
    #print b.__dict__    #这句就会出错了，Base2类定义了__slots__属性，就没有了__dict__属性
    debug.trace(["dir(b):", dir(b)])
    debug.trace(["Base2.y:", type(Base2.y), Base2.y])    # y属性不知道是什么
    debug.trace(["b.a,Base2.a:", b.a,Base2.a])   # 类属性，实例和类都可以访问。
    
    #b.x = 2              #error,不能增加新的变量
    #print b.__dict__

# __dict__是类的默认内置属性，每一个对象实例化时都分配一个字典，类增加属性时都向字典里面
# 增加值。定义__slots__的内部作用还是归结到影响__dict__属性上，因为定义了__slot__属性否，
# 实例就没有了__dict__属性，实例之所以可以增加属性是因为__dict__属性在其作用，这是其Python
# 的内部机制。所以如果在__slot__里面增加了__dict__属性后，实例就可以增加属性了。但是，这样
# 定义了__slots__属性并且包含了__dict__变量，和不定义__slots__属性有什么区别呢。定义了__slots__
# 属性的变量多了__slots__属性，但是少了__weakref__属性。
'''
__dict__是类的默认内置属性，每一个对象实例化时都分配一个字典，类增加属性时都向字典里面
增加值 ---- 这句话是不对的。 (类增加属性时，只是类增加了属性，实例可以访问到这个属性是由于属性访问机制决定的)

'''
class Base3(object):
    __slots__=('__sdf', 'y', '_y', '_x')   # 抑制了__dict__属性, 没有下划线的属性就是只读的属性。
    #__slots__=('__sdf', 'y', "__dict__")   # 定义了__dict__属性就可以使用随意绑定属性了
                        # __sdf属性，以两个下划线开头的属性会自动加上_ClaaName前缀。
    y = 2
    v = 1
    def __init__(self):
        pass
    
    def setY(self, y):
        pass
        debug.trace(["setY:y:",y])
        #object.__setattr__(self, 'y', y) # 这种方式设置y的属性也是不行的
        #self.y=y    # 会报错， y是只读属性。JavaScript语言的属性的配置相似，只不过平时很少用到。
        # 每一个对象可以给它定义很多的属性， 每个属性有它的配置属性（可读，可写等）。
        self._y=y
        self.__sdf=y
        #self.__x=y+1    # 同样的属性名__x在内部写和在外部写是不一样的，在内部写会自动的加上'_类名'的前缀
        #self._z=y
        
def test_func3():
    b = Base3()
    #print b.__dict__
    #b.x = 2   # 定义了__slots__， 没有x属性， 不能给这个属性赋值。我的理解是Python默认情况下对象调用点操作符的时候
    # 如果发现这个对象没有这个属性， 就会给这个对象创建一个属性。但是如果定义了__slots__，就会改变这个终止默认的行为。
    # 没有给这个对象创建属性， 也不能给这个属性赋值了。 
    #b.y = 3   #read only, __slots__里面声明了y, y就变成了只读属性了。
    b.setY(4)
    debug.trace(["b.y:", b.y])
    debug.trace(["b._y:", b._y])
    debug.trace(["b.__sdf:", b._Base3__sdf])
    
    # 
    # 只有双下划线具有特殊的意义，单下划线类似于普通的字符。
    # 上句也有问题，单下划线的变量是可以修改的，不带下划线的
    # 变量是只读的属性(如果定义了__slots__)，不能赋值。
    b._x=2  #
    debug.trace(["b._x:", b._x])
    #b.a=123
    
    #b.y=3
    #debug.trace(["b.y:", b.y])   
    
    debug.trace(["dir(b):", dir(b)])
    
"""

"""
class LocalProxy(object):
    __slots__ = ('__local', '__dict__', '__name__', 'dfg') # 这里定义的就是类属性

    def __init__(self, local, name=None):
        pass
        object.__setattr__(self, '_LocalProxy__local', local)
        #object.__setattr__(self, '_LocalProxy__locael', local)
        #object.__setattr__(self, '__name__', name)

    def _get_current_object(self):
        pass
        debug.trace([ "_get_current_object"])
        debug.trace([ "self.__local", self.__local])
        #print dir(self)
        #print dir(LocalProxy)
        #print self.__name__
        
        #if not hasattr(self.__local, '__release_local__'):
        #    return self.__local()
        #try:
        #    return getattr(self.__local, self.__name__)
        #except AttributeError:
        #    raise RuntimeError('no object bound to %s' % self.__name__)

def test_func4():
    proxy=LocalProxy("local-val2", "local-name")
    proxy._get_current_object()
    proxy.__localw = "sdf"
    
    #print dir(proxy)  # 实例属性
    #print dir(LocalProxy) #类属性
    #print proxy.__localw
    #print proxy._LocalProxy__local
    debug.trace(["dir(proxy)", dir(proxy)])   # 实例属性
    debug.trace(["dir(LocalProxy)", dir(LocalProxy)]) #类属性
    debug.trace(["proxy.__localw", proxy.__localw])
    debug.trace(["proxy._LocalProxy__local", proxy._LocalProxy__local])
    #print proxy.__local      # 在外部不能引用以双划线开头的属性，因为属性名已经被替换了一个另外的名字,加上了_ClassName前缀

class Animal(object):
    pass

def test_func5():
    a=Animal()
    # 实例没有__name__属性，但是类有此属性。
    #debug.trace(['__name__:', a.__name__])
    debug.trace(['__name__:', Animal.__name__])

def func6():
    class Dog(object):
        a=1
    d=Dog()
    print 'getattr:', getattr(d, 'a')
    print 'hasattr:', hasattr(d, 'a')
    Dog.b=3
    print 'dir(d):', dir(d)   #列出所有d这个实例可以访问到的对象。
    print 'd.__dict__:', d.__dict__
    
if __name__ == "__main__":
    #test_func1()
    #test_func2()
    test_func3()
    #test_func4()
    #test_func5()
    #func6()
    
