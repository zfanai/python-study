'''
Created on 2011-12-14
@author: Peter
'''
import Person
import json
 
p = Person.Person('Peter',22)
 
def object2dict(obj):
    #convert object to a dict
    d = {}
    d['__class__'] = obj.__class__.__name__
    d['__module__'] = obj.__module__
    #print obj.__dict__
    #print dir(obj)
    d.update(obj.__dict__)
    return d
 
def dict2object(d):
    #convert dict to object
    if'__class__' in d:
        class_name = d.pop('__class__')
        module_name = d.pop('__module__')
        module = __import__(module_name)
        class_ = getattr(module,class_name)
        args = dict((key.encode('ascii'), value) for key, value in d.items()) #get args
        inst = class_(**args) #create new instance
    else:
        inst = d
    return inst
 
d = object2dict(p)
print d
#{'age': 22, '__module__': 'Person', '__class__': 'Person', 'name': 'Peter'}
 
o = dict2object(d)
print type(o),o
#<class 'Person.Person'> Person Object name : Peter , age : 22
 
dump = json.dumps(p,default=object2dict)
print dump
#{"age": 22, "__module__": "Person", "__class__": "Person", "name": "Peter"}
 
load = json.loads(dump,object_hook = dict2object)
print load
#Person Object name : Peter , age : 22