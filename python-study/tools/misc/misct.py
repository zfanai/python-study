# encoding:gbk
import os
import sys

class Debug(object):
    def trace(self, obj):
        print 'trace:', obj
debug=Debug()

# [1,0] ,第一个元素表示第几个槽， 第二个元素表示是下去（0，开始），
# 还是升起（1，结束）的信号。
def func1():
    res=[]
    for n in xrange(7):
        p=(n+1)
        stage=[]
        for i in xrange(p,0,-1):  # 1,2-1
            #if (i-1)!=0:stage.append([i-1, 1])
            #stage.append([i,0])
            if i==1:
                stage.append([i,0])
            elif i==7:
                stage.append([i-1,1])
            else:
                stage.append([i-1,1])
                stage.append([i,0])
        res.append(stage)
    
    #val_list=[]
    last_item=list(res[-1])
    res+=[last_item]*10
    for item in res:
        print item
        
    # 
    signal_val=[]
    signal_val2=[]
    for item in res:
        val=map(lambda x:x[0]*2 if x[1] else x[0]*2-1, item)
        print val
        val2=map(lambda x:"0x%02X"%(1<<(x-1)), val)
        print val2
        #val_list.append(val)
        signal_val += val
        signal_val2.append(val)
    print signal_val
        
    #for item in val_list:
    # 3A 30 31 30 32 30 32 30 31 30 30 46 42 0D 0A    
    #cmd_list=map(lambda x:'\':010202%02X%02XFB\\r\\n\','%(x%256, x/256), signal_val)
    #for cmd in cmd_list:print cmd
    #
    cmd_list2=[]
    for item in signal_val2:
        stage_cmd_list=map(lambda x:':010202%02X%02XFB\r\n'%((1<<(x-1))%256, (1<<(x-1))/256), item)
        cmd_list2.append(stage_cmd_list)
        #for cmd in cmd_list:print cmd
    print cmd_list2
        
    
if __name__=='__main__':
    func1()
