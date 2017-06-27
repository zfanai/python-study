#encoding:gbk
from tasks import add

def func1():
    # apply_async调用无效
    result = add.apply_async(args=[4,5], queue='laplace')
    print result.status
    print result.id
    print result.get(timeout=5)
    return result

def func2():
    result=add.delay(5,6)
    print result.status
    
if __name__ == '__main__':
    func2()