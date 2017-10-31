#encoding:utf8

import cPickle
data = range(5)
cPickle.dump(data, open("data.pkl","wb")) 