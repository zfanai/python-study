#encoding:gbk

import json

class Debug(object):
    def trace(self, msg):
        print 'trace:', msg
debug=Debug()

def fun1():
    json_str = r'{"bg框架":8.4, "a":null}'
    #json_str = u'{"bg框架":8.4, "a":null}'
    #json_str = r'{"bg":8.4}'
    debug.trace(['type(json_str):', type(json_str)])
    
    json_obj = json.loads(json_str, encoding="gbk")
    
    debug.trace([ 'json_obj, type(json_obj):', json_obj, type(json_obj)])
    
    dict_obj={"bg":8.3}
    debug.trace([ 'dict_obj:', dict_obj])
    
    #return

if __name__ == "__main__":
    debug.trace(["start..."]) 
    fun1()
    