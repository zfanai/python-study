#encoding:gbk
import ConfigParser 

def func1():  
    cf = ConfigParser.ConfigParser() 
      
    #read config
    cf.read("test.conf") 
      
    # return all section
    secs = cf.sections() 
    print 'sections:', secs 
      
    opts = cf.options("sec_a")
    print 'options:', opts 
      
    kvs = cf.items("sec_a") 
    print 'sec_a:', kvs 
      
    #read by type
    str_val = cf.get("sec_a", "a_key1") 
    int_val = cf.getint("sec_a", "a_key2") 
      
    print "value for sec_a's a_key1:", str_val 
    print "value for sec_a's a_key2:", int_val 
      
    #write config
    #update value
    cf.set("sec_b", "b_key3", "new-$r") 
    #set a new value
    cf.set("sec_b", "b_newkey", "new-value") 
    #create a new section
    cf.add_section('a_new_section') 
    cf.set('a_new_section', 'new_key', 'new_value') 
      
    #write back to configure file
    cf.write(open("test.conf", "w"))

'''
Python的ConfigParser Module中定义了3个类对INI文件进行操作。分别是RawConfigParser、ConfigParser、SafeConfigParser。RawCnfigParser是最基础的INI文件读取类，ConfigParser、SafeConfigParser支持对%(value)s变量的解析。 
'''
def func2():
    cf = ConfigParser.RawConfigParser() 
 
    print "use RawConfigParser() read"
    cf.read("test2.conf") 
    print cf.get("portal", "url") 
     
    print "use RawConfigParser() write"
    cf.set("portal", "url2", "%(host)s:%(port)s") 
    print cf.get("portal", "url2") 

def func3():
    cf = ConfigParser.ConfigParser() 
     
    print "use ConfigParser() read"
    cf.read("test2.conf") 
    print cf.get("portal", "url") 
     
    print "use ConfigParser() write"
    cf.set("portal", "url2", "%(host)s:%(port)s") 
    print cf.get("portal", "url2")     

def func4():
    cf = ConfigParser.SafeConfigParser() 
     
    print "use SafeConfigParser() read"
    cf.read("test2.conf") 
    print cf.get("portal", "url") 
     
    print "use SateConfigParser() write"
    cf.set("portal", "url2", "%(host)s:%(port)s") 
    print cf.get("portal", "url2") 
    
# 
if __name__ == '__main__':
    func4()