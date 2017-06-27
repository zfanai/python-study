#encoding:gbk
import sys
import re

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
    def rprint(self,msg):
        print msg
debug=Debug()

def func1(f, output):
    fo=open(f, 'r')
    lines=fo.readlines()
    fo.close()
    #debug.rprint(lines)
    index=0
    newlines=[]
    regpattern='(GKEYS\.([A-Z_0-9]+))'
    for line in lines:
    #for line in ['12${asdf_123[row].sg}34, 12${asdf_123[row].sg1}34', '${glucose.asdfef}']:
        
        #m=re.search('\$\{(\w+)\}', line)
        m=re.search(regpattern, line)
        #m=re.search('(\{% ([\w.]+) %})', line)
        
        #debug.rprint(line)
        #if m is not None:
        while m is not None:
            debug.rprint(m)
            debug.trace([m.group(1), m.group(2)])
            newline=line.replace(m.group(1), '\'%s\'' % m.group(2).lower())
            debug.trace(['newline:', newline])
            line=newline
            m=re.search(regpattern, line)
            
        newlines.append(line)    
        #
        index += 1
    #
    fo=open(output, 'w')
    fo.writelines(newlines)
    fo.close()
#    
if __name__=="__main__":
    if len(sys.argv)!=3:
        debug.trace(['args not correct!'])
        sys.exit(1)
    fmtpl=sys.argv[1]
    jjtpl=sys.argv[2]
    #
    func1(fmtpl, jjtpl)