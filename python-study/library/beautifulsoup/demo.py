#encoding:gbk
from bs4 import BeautifulSoup

def func1():
    fo=open('3.html')
    origi=fo.read(-1)
    origi=origi.replace('\n', '')
    soup=BeautifulSoup(origi, 'html.parser', from_encoding='gbk')
    print soup.original_encoding
    #print soup.body.div
    #data=str(soup.body.div)
    #print soup.table.tbody.tr.td
    t=soup.body.table.tbody.tr.td
    c=t.encode('gbk')
    print len(c), type(c)
    with open('out.txt', 'w') as fo:
        fo.write(c)
    #
    print 'find children'
    for c in t.children:
        print c.name
    print len(t.contents)
    

def func2():
    soup=BeautifulSoup(open('test.html'), 'html.parser', from_encoding='gbk')
    print soup.original_encoding
    t=soup.body.div
    print type(t)
    c=t.encode('gbk')
    print type(c),c
    with open('out.txt', 'w') as fo:
        fo.write(c)
    
def func3():
    soup=BeautifulSoup(open('3.1.html'), 'html.parser', from_encoding='gbk')
    print soup.original_encoding
    t=soup.div
    print type(t)
    c=t.encode('gbk')
    print type(c),c
    with open('out.txt', 'w') as fo:
        fo.write(c)
            
if __name__=='__main__':
    func1()