#encoding:utf8

import uuid

################################################################################
# uuid1()——基于时间戳
#     由MAC地址、当前时间戳、随机数生成。可以保证全球范围内的唯一性，
#     但MAC的使用同时带来安全性问题，局域网中可以使用IP来代替MAC
################################################################################
def uuid1_test():
    pass
    uuid_obj_1_1 = uuid.uuid1()
    print uuid_obj_1_1
    print str(uuid_obj_1_1)
    print type(uuid_obj_1_1.hex), uuid_obj_1_1.hex
    print type(uuid_obj_1_1.int), uuid_obj_1_1.int
    #print type(uuid_obj_1_1.bytes), uuid_obj_1_1.bytes
    
    uuid_obj_1_2 = uuid.uuid1()
    print uuid_obj_1_2

################################################################################
# uuid3()——基于名字的MD5散列值
#  通过计算名字和命名空间的MD5散列值得到，保证了同一命名空间中不同名字的唯一性，
#  和不同命名空间的唯一性，但同一命名空间的同一名字生成相同的uuid。
################################################################################                    
def uuid3_test():
    name = "test_name"
    namespace = "test_namespace"
    
    uuid_obj_1_1 = uuid.uuid1()
    #uuid_obj_3_1 = uuid.uuid3("123","123")
    #uuid_obj_3_1 = uuid.uuid3(namespace, name)
    print type(uuid.NAMESPACE_DNS)
    #uuid_obj_3_1 = uuid.uuid3(uuid.NAMESPACE_DNS, name) 
    uuid_obj_3_1 = uuid.uuid3(uuid_obj_1_1, name)
    print type(uuid_obj_3_1)
    
    #uuid_obj_3_2 = uuid.uuid3("123","23")
    #print uuid_obj_3_2
    
################################################################################
# uuid4()——基于随机数
#     由伪随机数得到，有一定的重复概率，该概率可以计算出来。
################################################################################                    
def uuid4_test():    
    uuid_obj_4_1 = uuid.uuid4()
    print uuid_obj_4_1

################################################################################
# uuid5()——基于名字的SHA-1散列值
#    算法与uuid3相同，不同的是使用 Secure Hash Algorithm 1 算法出来。
################################################################################                    
def uuid5_test(): 
    name = "test_name"   
    uuid_obj_5_1 = uuid.uuid5(uuid.NAMESPACE_DNS, name)
    print uuid_obj_5_1
    
    uuid_obj_5_2 = uuid.uuid5(uuid.NAMESPACE_DNS, name)
    print uuid_obj_5_2
        
if __name__ == "__main__":
    pass
    uuid1_test()
    #uuid3_test()
    #uuid4_test()
    #uuid5_test()
    
    
    