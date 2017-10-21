#encoding:utf8
from heapq import heappush, heappop

def heapsort(iterable):
     'Equivalent to sorted(iterable)'
     h = []
     for value in iterable:
         heappush(h, value)
     return [heappop(h) for i in range(len(h))]

def func1():
    a=heapsort([1,3,2,9,-1])
    print a
    
def func2():
    h=[]
    heappush(h, 3)
    heappush(h, 1)
    heappush(h, 2)
    print h
    #
    print heappop(h)
    print heappop(h)
    print heappop(h)
    print 'h:', h

if __name__=='__main__':
    #func1()
    func2()