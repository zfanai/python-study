#encoding:utf8

a=None

# 一种逻辑的三种写法， 写法1最简洁优雅。
# 写法1
b = a or (1,2)
# 写法2
b= a if a else (1,2)
# 写法3
if a:b=1
else:b=(1,2)

# 优雅代码的写法。
#path = u'%s|%s' % (
#    self.map.host_matching and self.server_name or self.subdomain,
#    path_info and '/%s' % path_info.lstrip('/')
#)


for i in a or (1,2):
    print 'val:', i