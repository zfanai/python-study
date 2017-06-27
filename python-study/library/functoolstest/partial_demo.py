#encoding:gbk

from functools import partial
 
def mod( n, m ):
  return n % m
 
mod_by_100 = partial( mod, 100 )
mod_by_100_7 = partial( mod, 100 ,7)
 
print mod( 100, 7 )  # 2
print mod_by_100( 7 )  # 2
print mod_by_100_7(  )  # 2