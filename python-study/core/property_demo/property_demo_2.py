#encoding:gbk

"""
property�޸ķ����÷���
1.
"""



class C:
    """
            �õ��Ǿ�ʽ��
    """
    def __init__(self): 
        self.__x=None 
        
    #1.���ڽ��ܵ�һ��ʹ�����Եķ����� 
    #�ڸ����ж��������������ֱ�������ֵ��ȡֵ��ɾ���������˴����Ҳ�����������뿴ʾ���� 
    def getx(self): 
        return self.__x 
    
    def setx(self,value): 
        self.__x=value 
    
    def delx(self): 
        del self.__x 
    
    # ������һ������    
    x=property(getx,setx,delx,'') 


def test_func1():
    pass
    c=C()
    c.x=100
    y=c.x
    print y
    del c.x

def test_func2():
    pass

    
if __name__ == '__main__':
    test_func1()
    #test_func2()


