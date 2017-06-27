#encoding:gbk

import re

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def func1():
    # match函数是从被匹配的字符串开始匹配
    #m=re.match('foo', 'fooseafood')  # 匹配成功
    m=re.match('foo', 'seafood')   # 匹配失败
    #m=re.search('foo', 'seafood')  # 匹配成功，反映match和search函数的区别。
    
    #
    debug.trace(['m:', m])
    if m is not None:
        debug.trace(['group:', m.group()])

# @note \w匹配字母和数字
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
    