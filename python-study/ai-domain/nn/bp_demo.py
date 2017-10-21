#encoding:utf8

from BP2 import NeuralNetwork
import numpy as np

# 输入是2维的向量， 但是其实输入层有3个单元（3个结点）。
nn = NeuralNetwork([2,2,1], 'tanh')
x = np.array([[0,0], [0,1], [1,0], [1,1]])
y = np.array([1,0,0,1])
nn.fit(x,y,0.1,10000)
print 'weights:', nn.weights
for i in [[0,0], [0,1], [1,0], [1,1]]:
    print(i, nn.predict(i))