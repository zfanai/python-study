from tasks import add

def func1():
    r=add.delay(4,4)
    v=r.get(timeout=2)
    print v
def func2():
    r=add.apply_async([5,6])
    v=r.get(timeout=2)
    print v
    
if __name__=='__main__':
    func2()