#encoding:gbk
import time  
  
st = time.time()  
a = 100.33  
b = 23.33  
ct = 100000  
dt = 10000  
  
for v in range(ct) :  
    for j in range(dt) :  
        c = a/++b  
  
print "total time:", time.time()-st  