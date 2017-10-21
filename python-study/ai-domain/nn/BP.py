#encoding:utf8

import numpy as np

def tanh(x):
    return np.tanh(x)

# 导数
def tanh_deriv(x):
    return 1.0 - np.tanh(x)*np.tanh(x)

def logistic(x):
    return 1/(1 + np.exp(-x))
def logistic_derivative(x):
    return logistic(x)*(1-logistic(x))
    

class NeuralNetwork:
    def __init__(self, layers, activation='tanh'):
        """
        :param layers: A list containing the number of units in each layer.
        Should be at least two values
        :param activation: The activation function to be used. Can be
        "logistic" or "tanh"
        """
        if activation == 'logistic':
            self.activation = logistic
            self.activation_deriv = logistic_derivative
        elif activation == 'tanh':
            self.activation = tanh
            self.activation_deriv = tanh_deriv

        self.weights = []
        for i in range(1, len(layers) - 1):
            w1=(2*np.random.random((layers[i - 1] + 1, layers[i] + 1))-1)
            w2=(2 * np.random.random((layers[i] + 1, layers[i + 1])) - 1)
            print 'w1:', w1, type(w1)
            print 'w2:', w2, type(w2)
            self.weights.append(w1*0.25)
            self.weights.append(w2*0.25)
        print self.weights
    
    # 拟合            
    def fit(self, X, y, learning_rate=0.2, epochs=10000):
        X = np.atleast_2d(X)
        temp = np.ones([X.shape[0], X.shape[1]+1])
        print 'fit:1:', temp
        temp[:, 0:-1] = X
        X = temp
        y = np.array(y)
        print 'fit:3:', X,y
    
        for k in range(epochs):
            i = np.random.randint(X.shape[0])
            a = [X[i]]
            
            print 'fit:4:', a
            # l表示第几层, 第0层表示输入层到隐藏层之间的权重.
            # a表示取输入样本当中的一个样本作为样本集。
            # 下面计算一遍神经网络， 输入层就是一个直接的输出功能。 
            # 第一个循环求隐藏层的输出。
            for l in range(len(self.weights)):
                a.append(self.activation(np.dot(a[l], self.weights[l])))
            print 'fit:5:', a
            # 下面求出了这个样本通过神经网络计算出来的值和训练值之间的差
            error = y[i] - a[-1]
            
            # 输出值作为反馈的输入值
            deltas = [error * self.activation_deriv(a[-1])]
            print 'fit:6:', deltas, type(error)
            
            # 先算出来的是最后一层的偏差， 
            for l in range(len(a) - 2, 0, -1):
                tv1=deltas[-1].dot(self.weights[l].T)   # 隐藏层到输出层的权重调整， 加权偏差
                tv2 = self.activation_deriv(a[l])       # 隐藏层的计算结果求导， 激活函数求导， 导数值， 也就是变化率。这个考虑
                # （接上）激活函数的影响， 而tv1是考虑权重的影响。
                print 'fit:6.1:', l, a[l], tv1, tv2
                deltas.append(tv1*tv2)
            print 'fit:7:', deltas
            
            deltas.reverse()
            print 'fit:8:', deltas
            
            # 调整权值, 调整权重， 不是直接用偏差乘以学习率来调整， 而是
            # 用偏差乘以输入值再乘以学习率来调整。
            for i in range(len(self.weights)):
                layer = np.atleast_2d(a[i])         
                delta = np.atleast_2d(deltas[i])    
                print 'fit:9:', i, layer, delta
                adjust=learning_rate * layer.T.dot(delta)
                print 'fit:10:', adjust
                self.weights[i] += adjust
    # 预测
    def predict(self, x):
        x = np.array(x)
        temp = np.ones(x.shape[0] + 1)
        temp[0:-1] = x
        a = temp
        for l in range(0, len(self.weights)):
            a = self.activation(np.dot(a, self.weights[l]))
        return a


            