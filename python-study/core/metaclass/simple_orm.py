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
        print 'ModelMetaclass:name:', name, bases
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
        attrs['__mappings__'] = mappings # �������Ժ��е�ӳ���ϵ
        attrs['__table__'] = name # �������������һ��
        return type.__new__(cls, name, bases, attrs)

# ���������������ͬ����ĸ�� �������͵�һ��ʵ���� ����Ҳ��һ���ࡣ
# ���еĶ�������type(������ �����Ԫ�飨����Ϊ�գ��� �������Ե��ֵ䣨���ƺ�ֵ��)
# type���ڽ������ͣ� object���ڽ����ࡣ ���������type, �õ�����һ���࣬ Ҳ����˵type�����õ�����һ����
# �������������type, ������������࣬ ����ʵ��Ҳ���࣬ type����ʵ�������ͣ� ��Ҳ��һ���࣬ ֻ��������������
# �������ʵ��Ҳ���࣬ ��������������ͨ�������
# Ĭ������£� ��class����һ���࣬������type������������һ���࣬ �������ָ����__metaclass__���ԣ� ����ָ������������������
# ����������__new__�������صľ�������ࡣ
class Model(dict):
    __metaclass__ = ModelMetaclass

    def __init__(self, **kw):
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
# ����User�����������ԡ�����ͨ��������__metaclass__���ԣ�ȥ�����������
# ���Է����������User.id�ͻᱣ��
class User(Model):
    id = IntegerField('uid')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')

u = User(id=12345, name='Michael', email='test@orm.org', password='my-pwd', l=4)
# 
#print User.id
print u.id
u.save()