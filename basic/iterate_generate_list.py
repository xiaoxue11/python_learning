# -*- coding: utf-8 -*-
"""
Created on Tue Nov  6 14:53:36 2018

@author: 29132
"""

#迭代器:iter()获取迭代器对象，next获取容器中的下一个元素
#python中next变成了__next__,so the using method is next(it) not it.next()
li=[1,2,3]
it=iter(li)
print(it)
print(next(it))
print(next(it))
print(next(it))
#print(next(it))
#列表，元组，字典，集合，str都可以给for循环直接调用，这个有iterable
from collections import Iterable
print(isinstance([],Iterable))
print(isinstance((),Iterable))
print(isinstance({},Iterable))
print(isinstance('abc',Iterable))
#generator
L=[x*x for x in range(10)]#list,use[]
print(L)
L=(x*x for x in range(10))#generator,use ()
for i in L:
    print(i)
#如果一个函数定义中包含yield关键字，那么这个函数就不再是一个普通函数，而是一个generator：
#generator和函数的执行流程不一样。
#函数是顺序执行，遇到return语句或者最后一行函数语句就返回。
#generator的函数，在每次调用next()的时候执行，遇到yield语句返回，
#再次执行时从上次返回的yield语句处继续执行。
def f():
    print('first step!')
    yield 1
    print('second step!')
    yield 2
    print('third step!')
    yield 3    
a=f()
print(next(a))
print(next(a))
print(next(a))
#iterator
from collections import Iterator
print(isinstance([],Iterator))
print(isinstance((),Iterator))
print(isinstance({},Iterator))
print(isinstance('abc',Iterator))
print(isinstance((x*x for x in range(10)),Iterator))
print(isinstance(iter([]),Iterator))



        
        




