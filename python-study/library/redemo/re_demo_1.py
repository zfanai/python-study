#encoding:gbk

import re
from zftrace import debug

def test_func1():
    m=re.match('^[a-zA-Z0-9._%+-]+@(?!.*\.\..*)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', "zf_sch@126.com")
    print m
    m=re.match('^[a-zA-Z0-9._%+-]+@(?!.*\.\..*)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', "zf%.+-sch@126.com")
    print m
    m=re.match('^[a-zA-Z0-9._%+-]+@(?!.*\.\..*)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$', "zf%.+-sch@!.126.com")
    print m    
    # *号是0次或多次
    m=re.match('(!.*\.\..*)$', "!.")
    print m


# *号的用法，匹配前面的表达式0次或多次
def test_func2():
    pass
    # 加一个括号可读性会更好
    m=re.match('!(.*)df(A*)$', "!.dfA")
    print m
    
    # 有问号就会出错 (?!)是一种语法，叫环视，如果没有(?)这样写就语法不对
    # (?!Expression)，表示所在位置右侧不能匹配Expression
    m=re.match('(?!(s*)\.\.(a*))123$', "!s..a")
    print m    
    
# .表示匹配任意字符，*表示匹配0次或多次
def test_func3():
    pass
    # 加一个括号可读性会更好
    m=re.match('.*$', "sasdasfefsdfsdf!2323rdf")
    print m

# 中国手机号的正则表达式
def test_func4():
    pass
    # [3|5|7|8|][0-9]{9} 
    m=re.match('^1[3|5|7|8|][0-9]{9}$', "13412345675")
    print m

# 匹配div元素
def func5(): 
    data=''
    with open('record.html') as f:
        data=f.read()
    # 环视表达式，默认是右侧，如果加上一个<表示右侧。 
    data='<div>kdf<div>jkejf</div>dfdfsdfef</div>'
    #m=re.search('<div([\s\S]*(?<!</))</', data)
    #m=re.search('<div(.*(?<!</))</', data)
    # 环视一般要搭配明确的特征字符串使用比较合理,如果搭配.*这样的模式使用
    # 意义不大，环视一般是用来删选，而不是用来排除。
    #m=re.search('<div.*(?<!</).*</', data)
    # 所以如果要实现div首尾标签不出现新的div标签的话，环视不是一个好的解决方案。
    m=re.search('<div[^<]*</div>', data)
    debug.trace('app', 'm:')
    print m.group(0)

def func6():
    data='b2233a'
    #m=re.search('<div([\s\S]*(?<!</))</', data)
    # (?<=\d{2})的右侧能够匹配两个数字
    #m=re.search('(?<=\d{2})a', data)
    #
    reg=['(?=\d{2}).*a', '(?!\d{2}).*a', '(?<=\d{2}).*a', '(?<!\d{2}).*a',
         '(?=\d{2})a', '(?!\d{2})a', '(?<=\d{2})a', '(?<!\d{2})a']
    for r in reg:
        m=re.search('b'+r, data)
        debug.trace('app', 'm:', m)
        print 'b'+r
        if m:print m.group(0)
    
if __name__=="__main__":
    #test_func1()
    #test_func2()
    #test_func3()
    #test_func4()
    func5()
    