#encoding:utf8

from werkzeug.local import *
import threading

# 线程本地化的栈
def func1():
    s=LocalStack()
    s.push('a')
    s.push('b')
    print s
    print s.top
    print s.pop()
    print s.pop()
    print s.pop(), s.pop()

# 测试线程本地化的栈在其他线程的访问情况
def func2():
    s=LocalStack()
    s.push('aaa')
    def e(*a):
        print 'e'
        print 'e:', s.top
    t=threading.Thread(target=e, args=(1,2))
    t.start()
    t.join()
    
# flask处理每个请求都会创建一个适配器    
def func3():
    from werkzeug.routing import Map,Rule
    # 先创建一个url的映射
    m=Map()
    print 'm:', m
    # url映射加入类容。
    r = Rule('/index', methods=['GET'], endpoint='index')
    print 'r:1:', r, str(r), repr(r)
    m.add(r)
    print 'm3:', m
    #adp=m.bind('onetrum.com')
    # 产生适配器
    adp = m.bind('onetrum.com', '', '', 'http', 'GET', '/index')
    print 'm2:', m, adp
    
    r,v=adp.match(return_rule=True)
    print 'r,v:', r,v

print 'func3:\n', func3()

if __name__=='__main__':
    #func1()
    #func2()
    #func3()
    pass