#!usr/bin/env python
# -*- coding: utf-8 -*

"""
__all__属性只在采用from pkg import * ， 这种导入方式时，才有意义。
相当于__all__属性指定了在采用这种导入方式时，哪些包的属性导入。
在作用上，下面两句的功能是不同的。
__all__ = ["module1"]   # 指定from allattr import * 时导入的属性
#
from . import module1   # 为当前包导入新的属性

"""

print __name__


#__all__ = ["module1", "module2"]

__all__ = ["attr1", "attr1"]

#from . import module2
#print module2.name

#import module1
