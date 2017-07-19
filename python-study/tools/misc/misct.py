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
    #print signal_val
    print signal_val2
        
    #for item in val_list:
    # 3A 30 31 30 32 30 32 30 31 30 30 46 42 0D 0A    
    #cmd_list=map(lambda x:'\':010202%02X%02XFB\\r\\n\','%(x%256, x/256), signal_val)
    #for cmd in cmd_list:print cmd
    #
    if False:    # 老机台的数据格式
        cmd_list2=[]
        for item in signal_val2:
            stage_cmd_list=map(lambda x:':010202%02X%02XFB\r\n'%((1<<(x-1))%256, (1<<(x-1))/256), item)
            cmd_list2.append(stage_cmd_list)
            #for cmd in cmd_list:print cmd
        print cmd_list2
    elif True:  # 新机台的数据格式
        cmd_list2 = []
        for item in signal_val2:   # 01000000000000000000
            '''
            
                '%s%s'%(''.join(map(lambda y:'0'+y, bin((1 << (x - 1)) % 256)[2:].rjust(8,'0')).reverse()),
                        ''.join(map(lambda y: '0' + y, bin((1 << (x - 1)) / 256)[2:].rjust(8, '0')).reverse()) )
            '''
            def transform(x):
                #print 'x:', x
                a=bin((1 << (x - 1)) % 256)[2:].rjust(8, '0')
                b=bin((1 << (x - 1)) / 256)[2:].rjust(8, '0')
                #print 'a,b:', a, b
                a=map(lambda c:'0'+c, a)  #.reverse()
                b = map(lambda c: '0' + c, b)#.reverse()
                a.reverse()
                b.reverse()
                a=''.join(a)
                b=''.join(b)
                
                #a= (''.join(map(lambda c: '0' + c, bin((1 << (x - 1)) % 256)[2:].rjust(8, '0'))) +
                # ''.join(map(lambda c: '0' + c, bin((1 << (x - 1)) / 256)[2:].rjust(8, '0'))))[0:20]
                #print 'a:', a
                #print 'a,b:', a, b
                
                return (a+b)[0:20]
                
            stage_cmd_list = map(lambda x: '@00FA004000000001010000%s43*\r' % (
                transform(x)
            ), item)   # ((1 << (x - 1)) % 256, (1 << (x - 1)) / 256)
            cmd_list2.append(stage_cmd_list)
            #break
            # for cmd in cmd_list:print cmd
        print cmd_list2

def func2():
    pass
    # 新机台状态数据
    '00FA004000000001010000123447'
    cmd_list=[]
    for i in xrange(24):
        v=i+1
        cmd_list.append('@00FA004000000001010000%02X%02X47*\r'%(v/256, v%256))
    print cmd_list

#  4个槽的情况
def func3():
    res = []
    slot_num=4
    for n in xrange(slot_num+1):
        p = (n + 1)
        stage = []
        for i in xrange(p, 0, -1):  # 1,2-1
            # if (i-1)!=0:stage.append([i-1, 1])
            # stage.append([i,0])
            if i == 1:
                stage.append([i, 0])
            elif i == slot_num+1:
                stage.append([i - 1, 1])
            else:
                stage.append([i - 1, 1])
                stage.append([i, 0])
        res.append(stage)

    # val_list=[]
    last_item = list(res[-1])
    res += [last_item] * 20
    for item in res:
        print item
    
    # 
    signal_val = []
    signal_val2 = []
    for item in res:
        val = map(lambda x: x[0] * 2 if x[1] else x[0] * 2 - 1, item)
        print val
        val2 = map(lambda x: "0x%02X" % (1 << (x - 1)), val)
        print val2
        # val_list.append(val)
        signal_val += val
        signal_val2.append(val)
    # print signal_val
    print signal_val2

    # for item in val_list:
    # 3A 30 31 30 32 30 32 30 31 30 30 46 42 0D 0A    
    # cmd_list=map(lambda x:'\':010202%02X%02XFB\\r\\n\','%(x%256, x/256), signal_val)
    # for cmd in cmd_list:print cmd
    #
    if False:  # 老机台的数据格式
        cmd_list2 = []
        for item in signal_val2:
            stage_cmd_list = map(lambda x: ':010202%02X%02XFB\r\n' % ((1 << (x - 1)) % 256, (1 << (x - 1)) / 256), item)
            cmd_list2.append(stage_cmd_list)
            # for cmd in cmd_list:print cmd
        print cmd_list2
    elif True:  # 新机台的数据格式
        cmd_list2 = []
        for item in signal_val2:  # 01000000000000000000
            '''

                '%s%s'%(''.join(map(lambda y:'0'+y, bin((1 << (x - 1)) % 256)[2:].rjust(8,'0')).reverse()),
                        ''.join(map(lambda y: '0' + y, bin((1 << (x - 1)) / 256)[2:].rjust(8, '0')).reverse()) )
            '''
            
            def transform(x):
                # print 'x:', x
                a = bin((1 << (x - 1)) % 256)[2:].rjust(8, '0')
                b = bin((1 << (x - 1)) / 256)[2:].rjust(8, '0')
                # print 'a,b:', a, b
                a = map(lambda c: '0' + c, a)  # .reverse()
                b = map(lambda c: '0' + c, b)  # .reverse()
                a.reverse()
                b.reverse()
                a = ''.join(a)
                b = ''.join(b)

                # a= (''.join(map(lambda c: '0' + c, bin((1 << (x - 1)) % 256)[2:].rjust(8, '0'))) +
                # ''.join(map(lambda c: '0' + c, bin((1 << (x - 1)) / 256)[2:].rjust(8, '0'))))[0:20]
                # print 'a:', a
                # print 'a,b:', a, b
                
                return (a + b)[0:20]
            
            stage_cmd_list = map(lambda x: '@00FA004000000001010000%s43*\r' % (
                transform(x)
            ), item)  # ((1 << (x - 1)) % 256, (1 << (x - 1)) / 256)
            cmd_list2.append(stage_cmd_list)
            # break
            # for cmd in cmd_list:print cmd
        print cmd_list2

if __name__=='__main__':
    #func1()
    func2()
    #func3()
