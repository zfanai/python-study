#encoding:gbk

import os
import ConfigParser

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1():
    if not os.environ.has_key('TCLD_CONF'):
        return
    conf=os.environ.get('TCLD_CONF')
    #
    cf=ConfigParser.ConfigParser() 
    cf.read(conf) 
    #
    port = cf.getint("server", "port")
    debug.trace(['port:', port])

if __name__=='__main__':
    func1()