#!usr/bin/env python
#coding:gbk

"""
    Test Python str , sequence, list, ecode
"""
import json

def func1():
    print "string"
    str_hello = "hello"
    print str_hello
    list_hello = ['h','e','l','l','o']
    print list_hello        # print ��������ͻ��������ȵ���str(list_hello)����
    print str(list_hello)    # str����ڽ�����ֻ�ǰѶ���ת�������������ַ�����ʾ�������ǰ�
                            # ����ת�����ַ�������
    # ��Ȼstring��list������sequence���ͣ��������ǲ���ͬһ������
    # Դ�ļ�����ʹ��utf-8���룬����Windowsϵͳ��Ĭ�ϱ���
    # ��ʽ��GBK,�����ӱ����ʱ������utf8������
    # �����ʱ�����ϵͳĬ�ϵı��뷽ʽGBK,Ҳ����˵
    # �ַ����ڶ����ʱ�����û��ָ�������ʽ��������ϵͳ
    # Ĭ�ϵ�GBK��ʽ���룬����������ַ���ǰ��Ӹ�uǰ׺��
    # ��ʾ����ַ�����Unicode�ַ���, Unicode��str������
    # ��ͬ���͵��ַ���
    str_hello = "hello����"      # ��ͨ�ַ���
    u_str_hello = u"hello����"   # Unicode�ַ���
    u_str_hello2 = u"helloworld"   # Unicode�ַ���,����������
    
    # str����Ĭ��ʹ�õ�GBK��ʽ�����룬���str����һ���ֽ�
    # ��������ֵ����0~127��Χ�ڣ��ͻ�����һ���쳣
    str_a = str(str_hello) 
    #str_b = str(u_str_hello)  # �����������
    str_c = str(u_str_hello2)  # 
    
    # str.encode �ڽ�����
    print str_hello , type(str_hello)  #����
    print str_a       #����
    print str_c  , type(u_str_hello2) , type(str_c)    #
    
    #dict_a = {"name":str_c}
    dict_a = {"name":u_str_hello2}
    print "dict_a:", str(dict_a)
    #utf8_str_hello = u_str_hello.decode("utf8")
    #print type(utf8_str_hello)

def func2():
    u_str_a = u"hello����"
    u_str_b = u"helloworld"      # unicode����Ҫ���������������ֽ�����ʾһ���ַ�
    str_a = "hello����"
    
    str_b = u_str_a.encode("gbk")  # ���ַ��������GBK�ַ���
    #str_b = u_str_a.decode("gbk")  # ����,
    #str_b = u_str_b.decode("gbk")  #����д�������岻��
    
    #print dir(u_str_a)
    #print dir(str_a)
    
    #print str_b
    
    print str_a
    #str_a.encode("gbk")      # ����str_aʵ���ϻ���һ��utf8���룬ǿ��ת����gbk��������
                            # ����д���൱��str_a.decode("sys_codec").encode("gbk") ,sys_codec��"gbk"
    temp_a=str_a.decode("utf8")    # ת������unicode����
    print type(temp_a)
    temp_b=temp_a.encode("gbk")    # ����
    
    print temp_b    
    

    
    # ��Python��ַ�����ͷֳ�Unicode�������������������
    # ����ָ���ת��������UnicodeΪ�м�ý�顣Unicode������һ���ַ�����
    # �����ַ�������
    
    
    pass

def func3():
    dict_a = {}
    dict_a["name"]="�ܷ�"
    print dict_a["name"]
    print repr(dict_a["name"])
    print str(dict_a)
    print repr(dict_a)
    
    #encodeedjson = json.dumps(dict_a, encoding="utf8")
    encodeedjson = json.dumps(dict_a, ensure_ascii=False)
    print type(encodeedjson), encodeedjson
    
    try:
        jsonfile = open("test.json","w")
        jsonfile.write(encodeedjson)
        jsonfile.close()
    except:
        print "error"

def func4():
    str_a="�ܷ�"
    print len(str_a)    # �����4, Ҳ�����ַ�������(gbk)�ĳ���
    print "\\x%02x" % ord(str_a[1])
    
    # �ַ������������ֲ�ͬ�����ͣ��ַ�������ָ���ת����ϵ��
    # ͨ��ord()������chr()��unichr()��������������֮�������
    # ���ַ�Ҳ���Է�Ϊascii�ַ���unicode�ַ������࣬������֮��
    # 
    
    str_a="zf�ܷ�"
    print len(str_a)
    
    str_a=u"zf�ܷ�"
    print len(str_a)    # ������4��Unicode����
    
    print unicode("�ܷ�", "gbk")    #��ȷ
    #print unicode("�ܷ�", "utf8")    #����"�ܷ�"��gbk����ģ������utf8������ͻ����
    
    print ord(u'��')
    
    
if __name__ == "__main__":
    #func1()
    #func2()
    #func3()
    func4()
