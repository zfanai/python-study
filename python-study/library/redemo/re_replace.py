#encoding:gbk

import re

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1():
    # match�����Ǵӱ�ƥ����ַ�����ʼƥ��
    #m=re.match('foo', 'fooseafood')  # ƥ��ɹ�
    m=re.match('foo', 'seafood')   # ƥ��ʧ��
    #m=re.search('foo', 'seafood')  # ƥ��ɹ�����ӳmatch��search����������
    
    #
    debug.trace(['m:', m])
    if m is not None:
        debug.trace(['group:', m.group()])

# @note \wƥ����ĸ������
def func2():
    strtmp='CREATE TABLE pre_common_admincp_cmenu ('
    m=re.search('CREATE TABLE (\w+) \(', strtmp)
    debug.trace(['m:', m])
    if m is not None:
        debug.trace(['group:', m.group(1)])

def func3():
    strHtml='''
    <script>
    asdf
    </script>
    '''
    regExp='<script>([^<]*sd[^<]*(?<!</))</script>'
    repExp='<!--<script>\\1</script>-->'
    #regExp='<script>'
    rv=re.sub(regExp, repExp , strHtml)
    debug.trace(rv)
    
if __name__=="__main__":
    func3()
    