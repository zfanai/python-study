#encoding:gbk

'''
     import tempfile
     
     ������Ӧ�ó�����Ҫһ����ʱ�ļ����洢���ݣ�
      ������Ҫͬ������������ô��TemporaryFile
     ����������ʱ�ļ�����õ�ѡ��������Ӧ�ó���
     ���޷��ҵ��������ļ��ģ���Ϊ����û������
     �ļ�ϵͳ�������������������ʱ�ļ����رպ�
     ���Զ�ɾ����
'''
import os
import tempfile

def make_file():
     '''������ʱ�ļ���������������Ҫ�ֶ��Ƴ�
         os.remove(file)
     '''
     file_name = 'c:\\tmp\\test.%s.txt' % os.getpid()
     temp = open(file_name, 'w+b')
     try:
         print('temp : {}'.format(temp))
         print('temp.name : {}'.format(temp.name))
         temp.write(b'hello, I\'m Hongten')
         temp.seek(0)
         print('#' * 50)
         print('content : {}'.format(temp.read()))
     finally:
         temp.close()
         #os.remove(file_name)
 
def make_temp_file():
     '''������ʱ�ļ����ڹرյ�ʱ��ϵͳ���Զ�����ļ�'''
     temp = tempfile.TemporaryFile()
     try:
         print('temp : {}'.format(temp))
         print('temp.name : {}'.format(temp.name))
         temp.write(b'hello, I\'m Hongten')
         temp.seek(0)
         print('#' * 50)
         print('content : {}'.format(temp.read()))
     finally:
         temp.close()  #then the system will automatically cleans up the file
 
def test_func2():
     make_file()
     print('#' * 50)
     make_temp_file()

def test_func1():
    pass
    

if __name__=="__main__":
    pass
    test_func1()