#encoding:gbk

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1(p):
    rate=[0.9, 0.91, 0.92, 0.93, 0.94, 0.95, 0.96, 0.97, 0.98, 0.99, 1,
          1.01, 1.02, 1.03, 1.04, 1.05, 1.06, 1.07, 1.08, 1.09, 1.1,]
    percent=[-10, -9, -8, -7, -6, -5, -4, -3, -2, -1, 0, 
             1,2,3,4,5,6,7,8,9,10]
    
    for i in range(0,21):
        print "%d%%    %.2f" % (percent[i], rate[i]*p)

#
if __name__=='__main__':
    func1(9.21)
