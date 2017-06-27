#encoding:utf8

class SenHisParser(object):
    SECTOR_SIZE=0x2000
    
    def parse(self):
        with open('sen_his.bin', 'rb') as fo:
            data=fo.read()
        print 'data size:', hex(len(data))
        sector_data=[]
        for i in xrange(3):
            sector_data.append( data[ (i*self.SECTOR_SIZE): ((i+1)*self.SECTOR_SIZE) ])
        print map(lambda x:'%02x'%ord(x), sector_data[0][0:10])
        print map(lambda x:'%02x'%ord(x), sector_data[1][0:10])
        print map(lambda x:'%02x'%ord(x), sector_data[2][0:10])

if '__main__'==__name__:
    parser=SenHisParser()
    parser.parse()