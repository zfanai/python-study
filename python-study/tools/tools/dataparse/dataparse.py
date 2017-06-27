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

if __name__=='__main__':
    func1(sys.argv[1])