#encoding:utf8

try:
    import simplejson as json
except ImportError:
    import json
    
    
'''
json的接口是不变的，使用json的地方对底层是不关心的，
不同的底层实现可以有不同的性能
'''