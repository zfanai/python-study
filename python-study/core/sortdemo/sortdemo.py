#encoding:utf8
import operator

a=[
    
    ('jane', 'B', 12),
    ('dave', 'A', 15),
('dave', 'B', 10), 
('dave1', 'A', 10), 
]

f=operator.itemgetter(1)
# 定义了一个函数f


a=sorted(a, key=lambda x:(x[2], -x[1]))
print a
#a=sorted(a, key=operator.itemgetter(1))
#print a
