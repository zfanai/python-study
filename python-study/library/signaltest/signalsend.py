#encoding:gbk

import os    
import signal    
import sys

pid=int(sys.argv[1] )    
print 'pid:', pid
#�����źţ�16175��ǰ���Ǹ����źŴ�������pid����Ҫ�����޸�    
#os.kill(pid, signal.SIGTERM) 
#�����źţ�16175��ǰ���Ǹ����źŴ�������pid����Ҫ�����޸�    
#os.kill(pid, signal.SIGUSR1) 