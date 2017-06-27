#encoding:gbk

def trace(obj):
    print "trace:",obj

# 调用read函数是，是把文件已字节的方式读出，有一个需要注意的地方是，
# 如果文件的打开方式没有加b标志，那么在读文件的时候会把\r\n字符合并成一个字符\n
# 所以有可能如果文件的大小是26字节，但是包含一个\r\n组合，那么读出来的数据的大小是25字节
# 但是，如果文件是以加了b标志打开的方式，那么reand读回来就是完全的文件的二进制内容。
# 
# readline和readlines读回来的都是str类型的串

def test_func1():
    pass
    fp=open("test.txt", "r")
    #data=fp.read(-1)
    #data=fp.readline(-1)
    data=fp.readlines(-1)
    trace(["data size:", len(data)])
    trace(["data:", data])
    
    # 下面是一个全角的空格符，但是它的长度是2
    find="　"
    trace(["find size:", len(find)])
    trace(["find :", find])
    
    #
    buf=data[0].replace(find, " ")
    trace(["buf:", buf])
    
    #print data[0]
    fp.close()

if __name__=="__main__":
    test_func1()