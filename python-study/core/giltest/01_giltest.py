#encoding:gbk

import threading

def dead_loop():
    while True:
        pass
        
def func2():
    t = threading.Thread(target=dead_loop) 
    t.start()

    dead_loop()

    t.join() 
        
if __name__=='__main__':
    #func1()
    func2()