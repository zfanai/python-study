#!/usr/bin/env python
# -*- coding: gbk -*-

' Simple ORM using metaclass '

__author__ = 'Michael Liao'

class Field(object):
    def __init__(self, name, column_type):
        self.name = name
        self.column_type = column_type
    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__, self.name)

class StringField(Field):
    def __init__(self, name):
        super(StringField, self).__init__(name, 'varchar(100)')

class IntegerField(Field):
    def __init__(self, name):
        super(IntegerField, self).__init__(name, 'bigint')

class ModelMetaclass(type):

    def __new__(cls, name, bases, attrs):
        print 'ModelMetaclass:name:', name, bases #, attrs
        if name=='Model':
            return type.__new__(cls, name, bases, attrs)
        print('Found model: %s' % name)
        mappings = dict()
        print 'attrs:', attrs
        for k, v in attrs.iteritems():
            if isinstance(v, Field):
                print('Found mapping: %s ==> %s' % (k, v))
                mappings[k] = v
        for k in mappings.iterkeys():
            attrs.pop(k)
        print 'attrs:', attrs    
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)

# 类和类型是两个不同方面的概念， 类是类型的一个实例， 类型也是一种类。
# 所有的对象都是由type(类名， 父类的元组（可以为空）， 包含属性的字典（名称和值）)
# type是内建的类型， object是内建的类。 如果父类是type, 得到的是一个类， 也就是说type函数得到的是一个类
# 但是如果父类是type, 这个类是类型类， 它的实例也是类， type它其实不是类型， 它也是一个类， 只不过属于类型类
# 类型类的实例也是类， 这个是类型类和普通类的区别。
# 默认情况下， 用class声明一个类，就是用type类型类来创建一个类， 但是如果指定了__metaclass__属性， 可以指定创建这个类的类型类
# 这个类型类的__new__函数返回的就是这个类。
class Model(dict):
#class Model(object):
    x__metaclass__ = ModelMetaclass

    def __init__(self, **kw):
        print 'kw:', kw
        super(Model, self).__init__(**kw)

    def __getattr__(self, key):
        try:
            print '__getattr__:key:', key
            return self[key]
        except KeyError:
            raise AttributeError(r"'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        print '__setattr__:', key, value
        self[key] = value

    def save(self):
        fields = []
        params = []
        args = []
        for k, v in self.__mappings__.iteritems():
            fields.append(v.name)
            params.append('?')
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join(params))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

# testing code:
# 本来User定义了类属性。但是通过定义了__metaclass__属性，去掉了类的属性
# 所以访问类的属性User.id就会保错。
class User(Model):
    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

print '======================='


'''
因为User是字典的子类， 实例化时候，传递的参数会以字典的形式保存起来。
而在定义表的时候， 会把什么的属性当成映射信息保存起来。
'''

def func0():
    # 也就是说User类， 表面上定义了id属性， 属性类型也是一份类， 然后实例化类的时候传了id参数， 但是这个id的值不是传给了定义的id属性。
    # 实例有id属性， 类保存了类和相应属性的映射关系。
    u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd', l=4)
    print u.id
    #print 'mappings:', u.__mappings__['id']
    
    # 
    ##print User.id
    #print u.id
    #u.save()
    #u=User()
    #u.id=1234

def func1():
    pass
    print type(dict), dict
    class Dog(dict):
        a=2
        def __init__(self, **kw):
            #self.a=a
            super(Dog,self).__init__(**kw)
            
    d=Dog(a=3)
    print d['a'], d.a

# d['color'] 和 d.color访问的目标是不一样的。
def func2():
    class Dog(object):
        def __getitem__(self, name):
            print 'name:', name
    d=Dog()
    print d['color']

if __name__=='__main__':
    func2()