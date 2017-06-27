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
    # *����0�λ���
    m=re.match('(!.*\.\..*)$', "!.")
    print m


# *�ŵ��÷���ƥ��ǰ��ı��ʽ0�λ���
def test_func2():
    pass
    # ��һ�����ſɶ��Ի����
    m=re.match('!(.*)df(A*)$', "!.dfA")
    print m
    
    # ���ʺžͻ���� (?!)��һ���﷨���л��ӣ����û��(?)����д���﷨����
    # (?!Expression)����ʾ����λ���Ҳ಻��ƥ��Expression
    m=re.match('(?!(s*)\.\.(a*))123$', "!s..a")
    print m    
    
# .��ʾƥ�������ַ���*��ʾƥ��0�λ���
def test_func3():
    pass
    # ��һ�����ſɶ��Ի����
    m=re.match('.*$', "sasdasfefsdfsdf!2323rdf")
    print m

# �й��ֻ��ŵ�������ʽ
def test_func4():
    pass
    # [3|5|7|8|][0-9]{9} 
    m=re.match('^1[3|5|7|8|][0-9]{9}$', "13412345675")
    print m

# ƥ��divԪ��
def func5(): 
    data=''
    with open('record.html') as f:
        data=f.read()
    # ���ӱ��ʽ��Ĭ�����Ҳ࣬�������һ��<��ʾ�Ҳࡣ 
    data='<div>kdf<div>jkejf</div>dfdfsdfef</div>'
    #m=re.search('<div([\s\S]*(?<!</))</', data)
    #m=re.search('<div(.*(?<!</))</', data)
    # ����һ��Ҫ������ȷ�������ַ���ʹ�ñȽϺ���,�������.*������ģʽʹ��
    # ���岻�󣬻���һ��������ɾѡ�������������ų���
    #m=re.search('<div.*(?<!</).*</', data)
    # �������Ҫʵ��div��β��ǩ�������µ�div��ǩ�Ļ������Ӳ���һ���õĽ��������
    m=re.search('<div[^<]*</div>', data)
    debug.trace('app', 'm:')
    print m.group(0)

def func6():
    data='b2233a'
    #m=re.search('<div([\s\S]*(?<!</))</', data)
    # (?<=\d{2})���Ҳ��ܹ�ƥ����������
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
    