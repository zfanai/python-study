#encoding:gbk

def trace(obj):
    print "trace:",obj

# ����read�����ǣ��ǰ��ļ����ֽڵķ�ʽ��������һ����Ҫע��ĵط��ǣ�
# ����ļ��Ĵ򿪷�ʽû�м�b��־����ô�ڶ��ļ���ʱ����\r\n�ַ��ϲ���һ���ַ�\n
# �����п�������ļ��Ĵ�С��26�ֽڣ����ǰ���һ��\r\n��ϣ���ô�����������ݵĴ�С��25�ֽ�
# ���ǣ�����ļ����Լ���b��־�򿪵ķ�ʽ����ôreand������������ȫ���ļ��Ķ��������ݡ�
# 
# readline��readlines�������Ķ���str���͵Ĵ�

def test_func1():
    pass
    fp=open("test.txt", "r")
    #data=fp.read(-1)
    #data=fp.readline(-1)
    data=fp.readlines(-1)
    trace(["data size:", len(data)])
    trace(["data:", data])
    
    # ������һ��ȫ�ǵĿո�����������ĳ�����2
    find="��"
    trace(["find size:", len(find)])
    trace(["find :", find])
    
    #
    buf=data[0].replace(find, " ")
    trace(["buf:", buf])
    
    #print data[0]
    fp.close()

if __name__=="__main__":
    test_func1()