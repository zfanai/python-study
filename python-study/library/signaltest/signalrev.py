#encoding:gbk
import os    
import signal    
import sys

from time import sleep    
     
def onsignal_term(a,b):    
    print '�յ�SIGTERM�ź�'    

def onsignal_ctrlc(a,b):    
    print '�յ�CTRL+C�ź�'      

def onsignal_int(a,b):
    print '�յ�int�ź�'      
    sys.exit()
#�����ǰ��źŴ���������SIGTERM���ں���onsignal_term����    
#signal.signal(signal.SIGTERM,onsignal_term) 
#signal.signal(signal.SIGINT,onsignal_int)    
#signal.signal(signal.CTRL_C_EVENT1,onsignal_ctrlc) 
     
def onsignal_usr1(a,b):    
    print '�յ�SIGUSR1�ź�'    
#�����ǰ��źŴ���������SIGUSR1���ں���onsignal_term����    
# Windowϵͳû��SIGUSR1�źţ� Linuxϵͳ��SIGUSR1�źš�
#signal.signal(signal.SIGUSR1, onsignal_usr1)    

def func1():     
    try:
        while 1:    
            print '�ҵĽ���id��',os.getpid()    
            sleep(10)  
    except :
        print 'ddd'
    
if __name__=='__main__':
    func1()