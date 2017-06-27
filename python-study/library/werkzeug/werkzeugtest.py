from werkzeug.local import *

def func1():
    s=LocalStack()
    s.push('a')
    print s
    print s.top
if __name__=='__main__':
    func1()