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
    # Ĭ�����ı�ģʽ��ȡ����windowϵͳ���\r\n�����ַ�ת����һ��
    # \n�ַ���
    fo=open(f, 'r')
    
    lines=fo.readlines()
    fo.close()
    #debug.rprint(lines)
    index=0
    newlines=[]
    strContent=''
    for line in lines:
    #for line in ['123\n123\n','}123sdf']:
        #debug.rprint(line)
        #debug.trace(['size:', len(line)])
        #newlines.append(line)
        # stripֻ��ȥ�����˵Ļس�����
        #debug.rprint(line.strip())
        #debug.rprint(line.replace('\n', ''))
        strContent+=line.replace('\n','').replace('\r','')
        
        #
        index += 1
    # 
    #strContent='}sdf3123{}'
    strContent,n1=re.subn('}', '}\n', strContent)
    strContent,n2=re.subn('{', '{\n', strContent)
    strContent,n3=re.subn(';', ';\n', strContent)
    strContent,n3=re.subn('\*/', '*/\n', strContent)
    debug.trace(['strContent:',n1,n2,n3])
    
    #
    fo=open(output, 'w')
    #fo.writelines(newlines)
    fo.writelines(strContent)
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