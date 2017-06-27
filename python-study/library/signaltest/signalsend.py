#encoding:gbk

import os    
import signal    
import sys

pid=int(sys.argv[1] )    
print 'pid:', pid
#发送信号，16175是前面那个绑定信号处理函数的pid，需要自行修改    
#os.kill(pid, signal.SIGTERM) 
#发送信号，16175是前面那个绑定信号处理函数的pid，需要自行修改    
#os.kill(pid, signal.SIGUSR1) 