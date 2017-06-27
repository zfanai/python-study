#!usr/bin/env python
#coding:utf-8

"""
    Test Python str , sequence, list, ecode
"""
import json

def func1():
    print "string"
    str_hello = "hello"
    print str_hello
    list_hello = ['h','e','l','l','o']
    print list_hello        # print 这个函数就会隐含地先调用str(list_hello)函数
    print str(list_hello)    # str这个内建函数只是把对象转换成这个对象的字符串表示，而不是把
                            # 对象转换成字符串对象。
    # 虽然string和list都属于sequence类型，但是它们不是同一种类型
    # 源文件编码使用utf-8编码，但是Windows系统的默认编码
    # 方式是GBK,这样子编码的时候是用utf8，但是
    # 解码的时候会用系统默认的编码方式GBK,也就是说
    # 字符串在定义的时候，如果没有指定编码格式，就是用系统
    # 默认的GBK方式编码，但是如果在字符串前面加个u前缀就
    # 表示这个字符串是Unicode字符串, Unicode和str是两种
    # 不同类型的字符串
    str_hello = "hello世界"      # 普通字符串
    u_str_hello = u"hello世界"   # Unicode字符串
    u_str_hello2 = u"helloworld"   # Unicode字符串,不包含中文
    
    # str函数默认使用的GBK方式来解码，如果str读到一个字节
    # ，发现码值不在0~127范围内，就会引发一个异常
    str_a = str(str_hello) 
    #str_b = str(u_str_hello)  # 所以这句会出错
    str_c = str(u_str_hello2)  # 
    
    # str.encode 内建函数
    print str_hello , type(str_hello)  #乱码
    print str_a       #乱码
    print str_c  , type(u_str_hello2) , type(str_c)    #
    
    #dict_a = {"name":str_c}
    dict_a = {"name":u_str_hello2}
    print "dict_a:", str(dict_a)
    #utf8_str_hello = u_str_hello.decode("utf8")
    #print type(utf8_str_hello)

##########################################################
## @note str和Unicode之间的转换
##          (encode)
## unicode ----------> str
##
##          (decode)
##    str  ----------> unicode
## 
##########################################################
def func2():
    u_str_a = u"hello世界"
    u_str_b = u"helloworld"      # unicode的重要特征就是用两个字节来表示一个字符
    str_a = "hello世界"
    
    str_b = u_str_a.encode("gbk")  # 把字符串编码成GBK字符串
    #str_b = u_str_a.decode("gbk")  # 错误,
    #str_b = u_str_b.decode("gbk")  #这样写法的意义不大
    
    #print dir(u_str_a)
    #print dir(str_a)
    
    #print str_b
    
    print str_a
    #str_a.encode("gbk")      # 出错，str_a实际上还是一个utf8编码，强制转换成gbk编码会出错
                            # 这种写法相当于str_a.decode("sys_codec").encode("gbk") ,sys_codec是"gbk"
    temp_a=str_a.decode("utf8")    # 转换成了unicode编码
    print type(temp_a)
    temp_b=temp_a.encode("gbk")    # 乱码
    
    print temp_b    
    

    
    # 在Python里，字符编码就分成Unicode编码和其他编码两大类
    # 编码指尖的转换都是以Unicode为中间媒介。Unicode更像是一个字符集了
    # 而非字符编码了
    
    
    pass

def func3():
    dict_a = {}
    dict_a["name"]=u"周凡"
    print dict_a["name"]
    print repr(dict_a["name"])
    print str(dict_a)
    print repr(dict_a)
    
    #encodeedjson = json.dumps(dict_a, encoding="utf8")
    encodeedjson = json.dumps(dict_a, ensure_ascii=False)
    print type(encodeedjson), encodeedjson
    
    try:
        jsonfile = open("test.json","w")
        #jsonfile.write(encodeedjson)
        jsonfile.close()
    except:
        print "error"

def func4():
    str_a="周凡"
    print len(str_a)    # 结果是6,也就是字符串编码的长度
        
if __name__ == "__main__":
    #func1()
    #func2()
    func3()
    #func4()
