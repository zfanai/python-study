#encoding:utf8

class MyIterator(object):
    def __init__(self, step):
        self.step = step    
        
    def next(self):
        """Returns the next element."""
        print 'next:'
        if self.step==0:
            raise StopIteration
        self.step-=1
        return self.step
    
    # 返回这个对象的迭代器。 
    def __iter__(self):
        """Returns the iterator itself."""
        print '__iter__:'
        return self

# 在一个迭代的环境里面，会调用__iter__函数， 至于这个函数怎么写
# 你可以随意写，不一定要返回自身， 如果返回一个对象也有__iter__函数
# 那么下一次迭代就会调用这个对象的__iter__函数。
# 对于Python的容器，列表，字典等，在迭代时，是创建了一个它的迭代器对象。
# 并非容器自身。
# NOTE: zhouf, 170322, 上面的描述好像不太正确.在一个迭代的环境里面， 在迭代的开始，调用它的__iter__函数
#   一个对象要成为一个迭代器，必须同时实现next和__iter__函数。而调用next(obj)函数时只调用到obj的next函数， 不会调用__iter__函数。
#   迭代的入门是__iter__函数，迭代的过程是next函数。
def func1():
    # 迭代器语法调用的是next函数，所以迭代器必须要定义next函数。
    # next()函数是系统API
    it=MyIterator(4)
    print next(it)
    print '====================='
    #
    for el in it:
        print el
    print '====================='     
    for el in it:
        print el
    #print next(it)    
    
# for 碰到StopIteration就会停止。
# 在迭代列表，字典这些对象时，每次迭代都创建了一个新的迭代器对象。 
def func2():
    a=[1,2,3,4]
    for i in a:print i
    for i in a:print i
    
    #for i in iter(a):print i
    #print next(iter(a))
    
    a_it=iter(a)
    for i in a_it:print i
    print next(a_it)
    
if __name__=='__main__':
    #func1()
    func2()