#encoding:utf8
import sys

def func1(filename):
    def bytes2val(data):
        return data[1]*256+data[0];
    print 'fn:', filename
    data=[]
    with open(filename, 'rb') as fo:
        data=fo.read()
    #
    data=map(lambda x:ord(x), data)
    num=bytes2val(data[0:2])
    
    sum=2+num*2
    for i in xrange(num-1):
        pos = 2+i*2;
        size=bytes2val(data[pos:pos + 2])
        #print 's:', size
        sum+=size

    print 'size:', len(data), num, hex(sum), sum
    sec=data[sum+3:]
    #print 'sec:', sec
    #return 
    #sec=data[0x147a:]
    #sec=map(lambda x:ord(x), sec)
    basic_size=sec[1]
    basic_data=sec[0:basic_size+2]
    pos = basic_size + 2
    sensor_rtn_size=sec[pos+1]
    sensor_rtn = sec[pos:pos + sensor_rtn_size + 2]
    pos += sensor_rtn_size + 2
    
    pump_rtn_size=sec[pos+1]
    pump_rtn = sec[pos:pos + pump_rtn_size + 2]
    pos += pump_rtn_size + 2
    
    
    print 'sensor rtn:'
    for i in xrange(len(sensor_rtn) / 16 + 1):
        print ' '.join(map(lambda x: '%02X' % x, sensor_rtn[i * 16:(i + 1) * 16]))

    # pump_misc_size=sec[pos+1]
    # pump_misc=sec[pos:pos+pump_misc_size+2]
    # print 'srs:', basic_size, sensor_rtn_size, pump_rtn_size, pump_misc_size
    print 'pump rtn:'
    for i in xrange(len(pump_rtn) / 16 + 1):
        print ' '.join(map(lambda x: '%02X' % x, pump_rtn[i * 16:(i + 1) * 16]))
    
    #print 'pump misc:'
    #for i in xrange(len(pump_misc) / 16 + 1):
    #    print ' '.join(map(lambda x: '%02X' % x, pump_misc[i * 16:(i + 1) * 16]))
    
    #str_sec=map(lambda x:'%02x'% ord(x), sec)
    #print 'sec[0]:', basic_data[0:4], sensor_rtn[0:4], pump_rtn[0:4],pump_misc[0:4]

def func2():
    a='0b000001 10023883 7d060002 b5725106 01d33de1 01033133 99002000 003e4491 058305c3 2ae50100 00000002 004c0000 00000001 03004c00 883ae101 14000500 00000000 00000000 042f0000 00597251 06240019 0005291a 000144e8 03930300 00006800 10000000 00d3e708 08b47600 10000000 00370000 00'
    b=a.strip().replace(' ','')
    print 'b:', b
    def hex2bin(x):
        r=[]
        n=len(x)
        for i in xrange(n/2):
           r.append(int(x[i*2:(i+1)*2], 16))
        return r
    c=hex2bin(b)
    print 'c:', c[0:3]
    d=c[3:]
    print 'd:',d[0:3]
    
    def split_data(d):
        pos=0
        a=[]
        while pos<len(d):
            s=d[pos+1]
            a.append(d[pos:pos+s+2])
            pos += 2+s
        return a
    e=split_data(d)
    print 'e:', e
    f=e[-1]
    print 'f:', f, len(f)
    g=' '.join(map(lambda x:'%02X'%x, f))
    print 'g:', g
    print 'g.1:', f[5:5+34]
    print 'g.2:', f[39:]
    
def func3():
    #a=[11, 0, 0, 1, 16, 2, -74, 105, 20, 6, 1, 2, 65, 113, 81, 6, 1, -91, -89, -111, 6, 3, 49, 51, -115, 0, 32, 0, 0, -82, 21, 26, 5, -104, 5, -93, 35, -109, 6, 0, 0, 0, 0, 115, 0, 15, 1, 0, 0, 0, 0, 1, 116, 0, 15, 1, 88, -90, -111, 6, 70, 0, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 45, 0, 0, 0, 65, 113, 81, 6, 106, 0, 15, 1, -119, 6, 28, 0, 49, 0, 64, 1, 64, 1, 0, 32, 72, 10, 9, 8, 46, 0, 110, 0, 0, 0, 44, 1, 20, 0, 64, 1, 0, 0, 97, 3, 0, 0]
    a=[11, 0, 0, 1, 16, 2, -74, 105, 20, 6, 1, 2, 65, 113, 81, 6, 1, 64, -7, -110, 6, 3, 67, 51, -115, 0, 32, 0, 0, -124, 13, 26, 5, -104, 5, -93, 35, -109, 6, 0, 0, 0, 0, -79, 0, 15, 1, 0, 0, 0, 0, 1, -78, 0, 15, 1, -40, -9, -110, 6, 70, 0, 5, 0, 0, 0, 0, 0, 3, 18, -80, 0, 15, 1, -104, 12, 28, 0, 90, 0, 90, 0, 50, 0, 30, 0, 40, 0, 0, 0, 4, 45, 110, 0, 0, 65, 113, 81, 6, -80, 0, 15, 1, -104, 12, 28, 0, 51, 0, 90, 0, 90, 0, 50, 0, 30, 0, 40, 0, 17, 0, 115, 0, 0, 0, 110, 0, 30, 0, -126, 0, 0, 0, 97, 3, 0, 0]
    a=map(lambda x:256+x if x<0 else x, a)
    def split_data(d):
        pos=0
        a=[]
        while pos<len(d):
            s=d[pos+1]
            a.append(d[pos:pos+s+2])
            pos += 2+s
        return a
    e=split_data(a[3:])
    #print 'e:', e
    f=e[-2]
    #print 'f:', f, len(f)
    g=' '.join(map(lambda x:'%02X'%x, f))
    print 'g:', g
    #print g[46:]
    print ' '.join(map(lambda x:'%02X'%x, f[47:]))
    f=e[-1]
    print ' '.join(map(lambda x:'%02X'%x, f))
    #print 'g.1:', f[5:5+34]
    #print 'g.2:', f[39:]
    
    
if __name__=='__main__':
    #func1(sys.argv[1])
    #func2()
    func3()