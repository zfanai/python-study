#encoding:utf8

import os
import struct
import numpy as np

# 加载数据， 数据的返回值，返回一个元组， 第一个元素是头像数据。
def load_mnist(path, kind='train'):
    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte'
                               % kind)
    #f=open(labels_path)
    #return 
    #print 'labels_path:', labels_path
    with open(labels_path, 'rb') as lbpath:
        magic, n = struct.unpack('>II',
                                 lbpath.read(8))
        labels = np.fromfile(lbpath,
                             dtype=np.uint8)

    with open(images_path, 'rb') as imgpath:
        magic, num, rows, cols = struct.unpack('>IIII',
                                               imgpath.read(16))
        images = np.fromfile(imgpath,
                             dtype=np.uint8).reshape(len(labels), 784)

    return images, labels

import matplotlib.pyplot as plt

def func2(X_train, y_train):
    fig, ax = plt.subplots(
        nrows=2,
        ncols=5,
        sharex=True,
        sharey=True, )
    
    ax = ax.flatten()
    for i in range(10):
        img = X_train[y_train == i][0].reshape(28, 28)
        ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    
    ax[0].set_xticks([])
    ax[0].set_yticks([])
    plt.tight_layout()
    plt.show()

if __name__=='__main__':
    a=load_mnist(r'C:\Users\zhoufan\Projects\Python\mnist-data')
    print 'm:', a, type(a)
    print 'm:1:', a[0][0], len(a[0][0])
    func2(a[0], a[1])