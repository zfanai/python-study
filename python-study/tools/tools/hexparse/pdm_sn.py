#encoding:gbk
import sys
import re
import os
import ConfigParser

def hex2data(hex_str):
    size=len(hex_str)
    data=[]
    for i in xrange(size/2):
        data.append(int(hex_str[i*2:(i+1)*2], 16))
    return data

# 大端：高低高低
# 小端：高高低低
def bytes2int(data, big_endian=False):
    res=0
    if big_endian:
        data=data[::-1]
    for i in xrange(len(data)):
        if i>=1:res<<=8
        res+=data[i]
    return res

def val2bytes(val, big_endian=False, **args):
    rqn=args.get('rqn')
    data=[]
    while val:
        data.append(val&0xff)
        val>>=8
    #
    if rqn and rqn>len(data):
        data += [0]*(rqn-len(data))
    if big_endian:return data
    else:return data[::-1]

def data2hex(data):
    return ''.join(map(lambda x:'%02X'%x, data))
    
    
class HexParser(object):
    
    def __init__(self, file_path=None):
        self.addr_mask=[]
        if not file_path:return 
        # 
        with open(file_path) as fo:
            self.hex_lines=fo.readlines()
            print 'hex_lines:', len(self.hex_lines)
        
        self.raw_parse()
        #self.make_hex('sde.hex')
        
    def hex_crc(self, data):
        val=sum(data)
        return (0x100-(val&0xff)) & 0xff
        
    def make_hex(self, filename):
        hex_lines=[]
        
        debug_count=0
        
        for block in self.bin_data: 
           if 'flag' in block:
               if 1==block['flag']:
                   crc_range=[0]+val2bytes(0)+[1]
                   #print 'crc_range:', len(crc_range)
                   hex_line=''.join([
                        ':',
                        '00',
                        '0000',
                        '01',
                        #data2hex(val2bytes(start_addr)),
                        data2hex(val2bytes(self.hex_crc(crc_range), rqn=1))])
                   hex_lines.append(hex_line)
               elif 5==block['flag']:
                   data=block['data']
                   crc_range=[len(data)]+val2bytes(0)+[5]+data
                   #print 'crc_range:', len(crc_range)
                   hex_line=''.join([
                        ':',
                        data2hex([len(data)]),
                        '0000',
                        '05',
                        data2hex(data),
                        data2hex(val2bytes(self.hex_crc(crc_range), rqn=1))])
                   hex_lines.append(hex_line)
               
           else:
               
               # 长度， 偏移， 类型， 数据， 校验
               #data=item['data']
               start_addr=block['start_addr']>>16
               #print 'start_addr:', hex(start_addr)
               if block['start_addr'] in self.addr_mask:continue
               
               #
               crc_range=[2]+val2bytes(0)+[4]+val2bytes(start_addr)
               #print 'crc_range:', len(crc_range)
               hex_line=''.join([
                    ':',
                    '02',
                    '0000',
                    '04',
                    data2hex(val2bytes(start_addr)),
                    data2hex(val2bytes(self.hex_crc(crc_range), rqn=1))
                                 ])
               #print 'hex_line:', len(hex_line), hex_line
               hex_lines.append(hex_line)
               
               for item in block['sec']:
                   data=item['data']
                   #
                   data_size=len(data)
                   data_index=0
                   while data_size:
                       if data_size>16:
                           num=16
                       else:
                           num=data_size
                       data_size -= num
                       
                       # 
                       crc_range=[num]+val2bytes(data_index+item['offset'])+[0]+data[data_index:data_index+num]
                       #
                       hex_line=''.join([
                        ':',
                        data2hex([num]),
                        data2hex(val2bytes(data_index+item['offset'], rqn=2)),
                        '00',
                        data2hex(data[data_index:data_index+num]),
                        data2hex(val2bytes(self.hex_crc(crc_range), rqn=1))
                                     ])
                       #
                       #print 'hex_line:', len(hex_line)
                       if debug_count<20:
                           #print 'hex_line:', data_index, num, data[data_index:data_index+num]
                           debug_count += 1
                           
                       #
                       data_index += num
                       hex_lines.append(hex_line)
        # 
        #for item in hex_lines:
        #    print 'hex_'
        
        print 'line num:', len(hex_lines)
        
        #               
        with open(filename, 'w') as fo:
            fo.write('\n'.join(hex_lines))
            #for line in hex_lines:
            #    fo.write(line)
                
                   
    
    def raw_parse(self):
        result=map(lambda x:[
                  bytes2int(hex2data(x[1:3])),
                  bytes2int(hex2data(x[3:7])),
                  bytes2int(hex2data(x[7:9])),
                  hex2data(x[9:9+ bytes2int(hex2data(x[1:3]))*2]),
                  bytes2int(hex2data(x[-3:-1]))
                      ], self.hex_lines)  
        #print 'raw_parse:1:', result[0:4]
        #for item in result[0:4]:
        #    print 'parse result:1:', item
        bin_data=[]
        addr_oft=0
        
        debug_count=0
        debug_count1=0
        debug_count2=0
        #flag=-1
        #for row in result:
        cur_flag=-1    
        for i in xrange(len(result)):
            row=result[i]
            size,oft,flag,data,crc=row[:]
            # 
            if cur_flag != flag:
                cur_flag=flag
                #print 'cur_flag:', i,flag, row
                
            #
            if 4==flag:
                #if bin_data:
                addr_oft=bytes2int(data)<<16;
                bin_data.append(                    
                        {
                           'sec':[],
                           'start_addr':addr_oft
                        })
            # 数据记录
            elif 0==flag:
                last_block=bin_data[-1]
                #last_block=bin_data[-1]['sec']
                
                if not last_block['sec']:
                    last_block['sec'].append({
                            'start_addr':last_block['start_addr'],
                            'end_addr':last_block['start_addr']+size,
                            'offset':oft,
                            'data':data})
                else:
                    last_sec=last_block['sec'][-1]
                    
                    #
                    if debug_count<30 and last_sec:
                        #print 'new sec:1:', i, hex(oft), hex(size)
                        #print 'new sec:2:', hex(last_sec['start_addr']), hex(last_sec['end_addr']), hex(len(last_sec['data']))
                        #print 'new sec:3:', hex(len(last_sec['data'])+last_sec['offset']), hex(oft)
                        debug_count+=1
                    
                    # 
                    if oft==len(last_sec['data'])+last_sec['offset']:
                        last_sec['end_addr'] += size
                        last_sec['data'] += data
                    else:
                        #if debug_count1<20:
                        #    print 'last_block sec append:', i , row
                        #    debug_count1 += 1
                        last_block['sec'].append({
                            'start_addr':last_block['start_addr']+oft,
                            'end_addr':last_block['start_addr']+oft,
                            'offset':oft,
                            'data':data
                                           })
                        
                        last_sec=last_block['sec'][-1]
                        if debug_count1<20:
                            #print 'new sec:4:', i, hex(last_sec['start_addr']), hex(last_sec['end_addr']), hex(len(data)), hex(oft)
                            debug_count1+=1
                
                #if debug_count<20:
                #    #print 'oft:', oft, hex(last_bindata['end_addr']), i, row
                #    debug_count += 1
            elif 5==flag:
                bin_data.append({
                    'flag':5,
                    'data':data })
            elif 1==flag:
                bin_data.append({
                    'flag':1})
        # 
        print 'result:', len(bin_data)
        for item in bin_data:
            if 'flag' in item:
                pass
                #print 'item:',
            else:
                sec_list=item['sec']
                #print 'sec_list:', len(sec_list)
                for sec in sec_list:
                    pass
                    #print 'item:', hex(sec['start_addr']), hex(sec['end_addr']), hex(sec['offset']), hex(len(sec['data']))
        self.bin_data=bin_data
        return bin_data
    
    def find_pattern(self, pattern):
        for i in xrange(len(self.bin_data)):
            block=self.bin_data[i]
            if 'flag' in block:continue
            for j in xrange(len(block['sec'])):
                sec=block['sec'][j]
                #if re.search(pattern, sec['data']):
                pos=''.join(map(lambda x:chr(x), sec['data'])).find(pattern)
                if -1!=pos:return[i,j,sec['start_addr']+sec['offset']+pos,pos]
        return None
    
    def set_addr_mask(self, mask):
        self.addr_mask=mask
    
    def modify_data(self, addr, data):
        for block in self.bin_data:
            if 'flag' in block:continue
            for sec in block['sec']:
                start_addr=sec['start_addr']
                end_addr=sec['end_addr']
                #
                if addr>=start_addr and addr<end_addr:
                    rest_size=end_addr-addr
                    pos=addr-start_addr
                    if rest_size>=len(data):
                        for i in xrange(len(data)):
                            sec['data'][pos+i]=data[i]
                    else:
                        return self.modify_data(end_addr, data[len(data)-rest_size:])
    
    def read_data(self, addr, size):
        res=[]
        for block in self.bin_data:
            if 'flag' in block:continue
            for sec in block['sec']:
                start_addr=sec['start_addr']
                end_addr=sec['end_addr']
                #
                if addr>=start_addr and addr<end_addr:
                    rest_size=end_addr-addr
                    pos=addr-start_addr
                    if rest_size>=size:
                        return sec['data'][pos:pos+size]
                    else:
                        res=sec['data'][pos:pos+res_size]
                        return res+self.read_data(end_addr, size-rest_size)
    def set_bin_data(self, bin_data):
        self.bin_data=bin_data
    
    def merge_bin_data(self, bin_data):
        #self.bin_data+=bin_data
        data_part=filter(lambda x:'flag' not in x, self.bin_data)
        flag_part=filter(lambda x:('flag' in x) and (x['flag']!=5), self.bin_data)
        to_merge_data=filter(lambda x:'flag' not in x, bin_data)
        self.bin_data=data_part+to_merge_data+flag_part

def modify_lang(hex_file):
    print 'hex_file:', hex_file
    parser=HexParser(hex_file)
    rv=parser.find_pattern('GREEN')
    print 'find_pattern:1:', rv[0], rv[1], hex(rv[2]), hex(rv[3])
    offset=hex(rv[2]-int(sys.argv[2], 16))
    
    # 0x83E是设置里面用户名 GREEN 的偏移位置。
    offset=0x83E
    def_setting_addr=rv[2]-offset
    # 0x6F8是设置里面语言nLanguage的设置。
    lang_addr=def_setting_addr+0x6F8
    #print 'offset:', hex(offset)
    # 0x6F8
    lang_desc=[
                ['GB', 0],
                ['CN', 1],
                ['HKF', 2],
                ['FR', 3],
                ['IT', 4],
                ['ES', 5],
                ['DE', 6],
                ['TR', 7],
            ]
    print 'lang:1:', parser.read_data(lang_addr, 2)
    print 'lang:1:', parser.read_data(lang_addr-2, 2)
    print 'lang:1:', parser.read_data(lang_addr-4, 2)
    #return 0
    parser.set_addr_mask([0x8100000])
    b,e=hex_file.split('.')
    p=b.split('_')
    print 'b,e:', b, e
    #return 0
    parser.make_hex('%s_TEST.hex'%b)
    parser.set_addr_mask([])
    #return 
    for item in lang_desc:
        parser.modify_data(lang_addr, val2bytes(item[1], True, rqn=2))
        #parser.set_addr_mask([])
        #p[0]='962022'
        p[1]='%s010024'%item[0]
        parser.make_hex('%s.hex'%('_'.join(p)))

def gen_version():
    config_path=sys.argv[1]
    print 'config_path:', config_path
    cf=ConfigParser.ConfigParser()
    cf.read(config_path)
    boot_path=cf.get('common', 'boot_path')
    app_path=cf.get('common', 'app_path')
    trace_enable=cf.get('common', 'trace_enable')
    purpose=cf.get('common', 'purpose')
    dest_dir_base=cf.get('common', 'dest_dir_base')
    version_code=cf.get('common', 'version_code')
    version=cf.get('common', 'version')
    whole_sw_code=cf.get('common', 'whole_sw_code')
    app_sw_code=cf.get('common', 'app_sw_code')
    print 'boot_path:', boot_path
    print 'app_path:', app_path
    boot_parser=HexParser(boot_path)
    app_parser=HexParser(app_path)
    merge_parser=HexParser()
    merge_parser.set_bin_data(boot_parser.bin_data)
    merge_parser.merge_bin_data(app_parser.bin_data)
    #merge_parser.make_hex('sdf.hex')
    # 检查目录是否存在，如果不存在，需要创建目录
    version_path=os.path.join(dest_dir_base, version)
    print 'version_path:', version_path
    if not os.path.exists(version_path):
        os.makedirs(version_path)
        
    # 查找语言设置的位置
    rv=app_parser.find_pattern('GREEN')
    #print 'find_pattern:1:', rv[0], rv[1], hex(rv[2]), hex(rv[3])
    #offset=hex(rv[2]-int(sys.argv[2], 16))
    
    # 0x83E是设置里面用户名 GREEN 的偏移位置。
    offset=0x83E
    def_setting_addr=rv[2]-offset
    # 0x6F8是设置里面语言nLanguage的设置。
    lang_addr=def_setting_addr+0x6F8
    lang_desc=[
                ['GB', 0],
                ['CN', 1],
                ['HKF', 2],
                ['FR', 3],
                ['IT', 4],
                ['ES', 5],
                ['DE', 6],
                ['TR', 7],
            ]
    if trace_enable=='no' and purpose=='product':    
        for item in lang_desc:
            app_parser.modify_data(lang_addr, val2bytes(item[1], True, rqn=2))
            hex_path=os.path.join(version_path, '%s_%s%s.hex'%(app_sw_code, item[0], version_code))
            app_parser.make_hex(hex_path)
            
            #parser.set_addr_mask([])
            #p[0]='962022'
            #p[1]='%s010024'%item[0]
            merge_parser.set_bin_data(boot_parser.bin_data)
            merge_parser.merge_bin_data(app_parser.bin_data)
            
            hex_path=os.path.join(version_path, '%s_%s%s.hex'%(whole_sw_code, item[0], version_code))
            merge_parser.make_hex(hex_path)
    elif trace_enable=='yes' and purpose=='test':
        # 
        hex_path=os.path.join(version_path, 'fm011_boot.hex')
        boot_parser.make_hex(hex_path)
        # 
        hex_path=os.path.join(version_path, 'fm011_app_test.hex')
        app_parser.make_hex(hex_path)
        app_parser.set_addr_mask([0x8100000])
        hex_path=os.path.join(version_path, 'fm011_app_test_nolaunch.hex')
        app_parser.make_hex(hex_path)


def modify_pdm_sn():
    config_path=sys.argv[1]
    print 'config_path:', config_path
    cf=ConfigParser.ConfigParser()
    cf.read(config_path)
    boot_path=cf.get('common', 'boot_path')
    print boot_path
    pdm_sn=cf.get('common', 'sn')
    print pdm_sn
    boot_parser=HexParser(boot_path)
    d=boot_parser.read_data(0x800BFFC, 4)
    print 'd', d
    pdm_sn=pdm_sn.split(',')
    for sn in map(lambda x:int(x), pdm_sn):
        print 'sn:', sn, type(sn), val2bytes(sn, big_endian=True)
        boot_parser.modify_data(0x800BFFC, val2bytes(sn, big_endian=True))
        boot_parser.make_hex('boot_%s.hex'%sn)
        
    #boot_parser.modify_data(0x800BFFC, data)

def list_sec():
    config_path=sys.argv[1]
    print 'config_path:', config_path
    cf=ConfigParser.ConfigParser()
    cf.read(config_path)
    app_path=cf.get('common', 'app_path')
    print 'app_path:', app_path
    app_parser=HexParser(app_path)
    #print app_parser.bin_data
    for item in app_parser.bin_data:
        for k,v in item.items():
            if 'sec'==k:
                for s in v:
                    #for m,n in s.items():
                    #    print 
                    print hex(s['start_addr']), hex(s['end_addr'])
    
if __name__=='__main__':
    #modify_lang(sys.argv[1])
    #gen_version()
    list_sec()
