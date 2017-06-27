#encoding:utf8

"""
traceback demo
"""

import traceback

def func1():
    print "func1,001"
    
    traceback.print_stack()
    
    print "fun1,002"
    
def func2():
    func1()
    pass

def func3():
    func2()
    pass

def func4():
    func3()
    pass

def func5():
    #print "func5"
    func4()
    pass

def test():
    func5()

if __name__ == "__main__":
    print __doc__
    test()