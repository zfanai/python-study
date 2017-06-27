#起3个线程
threadNum = 3                      
threads = []
for i in range(threadNum):
    data = 'test'
    for j in range(VALUENUMBER):
        data = data+' '+DataList[j][i]
    res = ProductsTest(i,data,para)
    threads.append(res)  
for i in range(threadNum):
    threads[i].start()
for i in range(threadNum):
    threads[i].join()
################################################################
import Tkinter
import traceback
tcl = Tkinter.Tcl()
class ProductsTest(threading.Thread): 
    def __init__(self, num, data,para):   
        threading.Thread.__init__(self)   
        self.thread_num = num   
        self.data = data
        self.para = para
         
    def run(self):      
        global tcl
        starttime = time.clock()
        returnFromTcl = ''
        SCRIPTPATH1= "test1.tcl"
        SCRIPTPATH2= "test2.tcl"
        SCRIPTPATH3= "test3.tcl"
        if self.thread_num == 1:
            tcl.eval('source '+ SCRIPTPATH1)
            returnFromTcl = tcl.eval(self.data)     
        elif self.thread_num == 2:
            tcl.eval('source '+ SCRIPTPATH2)
            returnFromTcl = tcl.eval(self.data)     
        else:
            tcl.eval('source '+ SCRIPTPATH3)
            returnFromTcl = tcl.eval(self.data)     
        Time= time.clock() - starttime