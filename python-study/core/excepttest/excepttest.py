#encoding:utf8

class Debug(object):
    def trace(self, obj):
        print 'trace:',obj
debug=Debug()

def func1():
    try:
        fo=open('123.txt')
    except Exception as e:
        debug.trace(['except tp0', e, type(e)])

# @note 有finailly分支的话，try分支的return语句是不起作用的。
def func2():
    try:
        #fo=open('123.txt')
        debug.trace(['func2:tp0'])
        return 1    # return 语句不是不起作用。而是return的时候就跳到了finally块执行。
        # (接上)这样虽然没有发生异常，但是else块也不会执行了。
    except:
        debug.trace(['func2:tp1'])
    else:
        debug.trace(['func2:tp1.2'])
    finally:
        debug.trace(['func2:tp2'])
        return 2
    return 3
        
if __name__=='__main__':
    #func1()
    a=func2()
    debug.trace(['a:', a])