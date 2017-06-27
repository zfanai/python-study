#encoding:utf8

import itertools

def func1():
    #rv=itertools.compress('ABCDEF', [1,0,1,0,1,1])
    # [1,2]只在于每个元素的布尔值。
    rv=itertools.compress('ABCDEF', [1,2])
    #for x in rv:
    #    print x
    #print rv
    b=[_ for _ in rv]
    print b

if __name__=='__main__':
    func1()