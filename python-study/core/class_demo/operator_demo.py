#!usr/bin/env python
# -*- coding: utf-8 -*

"""
operator demo
"""

class MyInteger(object):
    def __init__(self,value):
        self.value = value
        
    def __add__(self, a):
        return self.value + a + 2
    
    def __str__(self):
        return "%d" % self.value
    
    def __eq__(self, value):
        print "MyInteger:__eq__:"
        #return True
        return self.value==(value+1)
        #return self==value    # 无限嵌套

def test():
    obj = MyInteger(3)
    print obj
    print obj+3
    #print 3+obj  # 加号的重载只适用obj+3， 不适用3+obj
    print obj==2
    
    
if __name__ == "__main__":
    print __doc__
    test()