#!/usr/bin/env python
# -*- coding: gbk -*-

import pymongo
import datetime


def get_db():
    # ��������
    #client = pymongo.MongoClient(host="localhost", port=27017)
    #db = client['example']
    client = pymongo.MongoClient(host="192.168.40.202", port=27017)
    db = client['onetrum']
    #���� db = client.example
    return db


def get_collection(db):
    # ѡ�񼯺ϣ�mongo��collection��database������ʱ�����ģ�
    #coll = db['informations']
    #print 'db.collection_names:', db.collection_names()

    coll = db['user']
    print 'db.collection_names:', db.collection_names()
    
    return coll


def insert_one_doc(db):
    # ����һ��document
    coll = db['informations']
    information = {"name": "quyang", "age": "25"}
    information_id = coll.insert(information)
    print information_id


def insert_multi_docs(db):
    # ��������documents,����һ������
    coll = db['informations']
    information = [{"name": "xiaoming", "age": "25"}, {"name": "xiaoqiang", "age": "24"}]
    information_id = coll.insert(information)
    print information_id


def get_one_doc(db):
    # �оͷ���һ����û�оͷ���None
    coll = db['informations']
    print coll.find_one()  # ���ص�һ����¼
    print coll.find_one({"name": "quyang"})
    print coll.find_one({"name": "none"})


def get_one_by_id(db):
    # ͨ��objectid������һ��doc
    coll = db['informations']
    obj = coll.find_one()
    obj_id = obj["_id"]
    print "_id ΪObjectId���ͣ�obj_id:" + str(obj_id)

    print coll.find_one({"_id": obj_id})
    # ��Ҫע�������obj_id��һ�����󣬲���һ��str��ʹ��str������Ϊ_id��ֵ�޷��ҵ���¼
    print "_id Ϊstr���� "
    print coll.find_one({"_id": str(obj_id)})
    # ����ͨ��ObjectId������strת��ObjectId����
    from bson.objectid import ObjectId

    print "_id ת����ObjectId����"
    print coll.find_one({"_id": ObjectId(str(obj_id))})


def get_many_docs(db):
    # mongo���ṩ�˹��˲��ҵķ���������ͨ����������ɸѡ����ȡ���ݼ��������Զ����ݽ��м���������ȴ���
    coll = db['informations']
    #ASCENDING = 1 ����;DESCENDING = -1����;default is ASCENDING
    for item in coll.find().sort("age", pymongo.DESCENDING):
        print item

    count = coll.count()
    print "�������������� %s��" % int(count)

    #������ѯ
    count = coll.find({"name":"quyang"}).count()
    print "quyang: %s"%count

def clear_all_datas(db):
    #���һ�������е���������
    db["informations"].remove()

def func1():
    db = get_db()
    my_collection = get_collection(db)
    post = {"author": "Mike", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
            "date": datetime.datetime.utcnow()}
    # �����¼
    my_collection.insert(post)
    insert_one_doc(db)
    # ������ѯ
    print my_collection.find_one({"x": "10"})
    # ��ѯ�������е�����
    for iii in my_collection.find():
        print iii
    print my_collection.count()
    my_collection.update({"author": "Mike"},
                         {"author": "quyang", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"],
                          "date": datetime.datetime.utcnow()})
    for jjj in my_collection.find():
        print jjj
    get_one_doc(db)
    get_one_by_id(db)
    get_many_docs(db)

def func2():
    db = get_db()
    user_colle = get_collection(db)
    print user_colle.count()
    print user_colle.find_one()

if __name__ == '__main__':
    # clear_all_datas(db)
    #func1()
    func2()