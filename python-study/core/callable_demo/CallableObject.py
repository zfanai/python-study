#!/usr/bin/env python
#coding=utf-8


class MyClass():
    def __call__(self, x, y):
        return x + y
    
def main():
    obj = MyClass()
    print obj(1, 2)

if __name__ == '__main__':
    main()        