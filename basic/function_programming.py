# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 14:21:43 2018

@author: 29132
"""
#变量名可以指向函数，函数名就是变量
from math import sqrt
print(sqrt(4)) 
f=sqrt
print(f(4))
def add(a,b,f):
    return f(a)+f(b)
a=add(3,-4,abs)
print(a)
#map:将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。
r=map(str,[1,2,3,4,5,6])
print(r)
print(next(r))
#example
r=map(str.title,['adam','LISA','barT'])
print(next(r))
print(next(r))
print(next(r))
#reduce:把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数;
#reduce把结果继续和序列的下一个元素做累积计算
from functools import reduce
def mul(x,y):
    return x*y
r=reduce(mul,[1,3,5,7,9])
print(r)
