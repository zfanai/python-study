#encoding:utf8

import os
import sys

################################################################################
# 
# 
################################################################################
def bin2hex(binfile, hexfile=None):
    
    #print os.getcwd()
    #print os.path.join(os.getcwd() , sys.argv[1])
    #binFileName = sys.argv[1]
    #hexFileName = sys.argv[1] + '.hex'
    binFileName = binfile
    hexFileName = "temp_hex.txt" if hexfile == None else hexfile
    
    outputBufferStr = ''
    
    try:
        binfile = open(binFileName,'rb')
        hexFile = open(hexFileName , 'w')
    except IOError:
        print "The file does not exist"
        sys.exit(0)
    
    binFileStr = binfile.read(-1)
    binFileLen = len(binFileStr)
    
    print binFileLen
    
    for i in range(0 , binFileLen):
        if (i % 16) == 0:
            outputBufferStr += "%08Xh(%08d):" % (i,i)
        
        val = ord(binFileStr[i])
        char_val = val if (val>=0x20 and val <=0x7f) else ord(".")
        outputBufferStr += "%02x(%c) " % (ord(binFileStr[i]), char_val)
        
        if (i % 16) == 15:
            outputBufferStr += '\n'
        #print i
    
    #hexFileName.write(outputBufferStr)
    hexFile.write(outputBufferStr)
    
    binfile.close()
    hexFile.close()
    #print "finish"

if __name__ == "__main__":
    trace_prefix = "bin2hex:main:"
    args_num = len(sys.argv)
    print trace_prefix,"args num:",args_num
    
    binfile = None
    hexfile = None

    if args_num>2:
        hexfile = sys.argv[2]    
    if args_num>1:
        binfile = sys.argv[1]
    if args_num==1:
        print "Usage:bin2hex binfile [hexfile]"
        sys.exit(0)
    
    bin2hex(binfile,hexfile)  
    
    
    


