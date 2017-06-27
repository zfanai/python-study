#encoding:gbk
import os    
import signal    
import sys

from time import sleep    
     
def onsignal_term(a,b):    
    print '收到SIGTERM信号'    

def onsignal_ctrlc(a,b):    
    print '收到CTRL+C信号'      

def onsignal_int(a,b):
    print '收到int信号'      
    sys.exit()
#这里是绑定信号处理函数，将SIGTERM绑定在函数onsignal_term上面    
#signal.signal(signal.SIGTERM,onsignal_term) 
#signal.signal(signal.SIGINT,onsignal_int)    
#signal.signal(signal.CTRL_C_EVENT1,onsignal_ctrlc) 
     
def onsignal_usr1(a,b):    
    print '收到SIGUSR1信号'    
#这里是绑定信号处理函数，将SIGUSR1绑定在函数onsignal_term上面    
# Window系统没有SIGUSR1信号， Linux系统有SIGUSR1信号。
#signal.signal(signal.SIGUSR1, onsignal_usr1)    

def func1():     
    try:
        while 1:    
            print '我的进程id是',os.getpid()    
            sleep(10)  
    except :
        print 'ddd'
    
if __name__=='__main__':
    func1()