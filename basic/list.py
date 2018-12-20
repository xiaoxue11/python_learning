# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 13:59:47 2018

@author: 29132
"""
# [list]
print(list('Hello'))

#索引
Weekday=['Monday','Tusday','Wednesday','Thursday','Friday']
print(Weekday[0])
print(Weekday[-4])
#slice
print(Weekday[0:4])
print(Weekday[-5:-2])
#count
x=[1,1,2,3,4,1,1]
print(x.count(1))
#sort
print(x.sort())
print(x)
#sorted
y=[2,4,1,5,6,3,0]
m=y[:]
m.sort()
n=sorted(y)
print(m)
print(n)
print(y)
#extend
a=[1,2,3]
b=[4,5,6]
a.extend(b)
print(a)
#index
print(a.index(4))
#reverse
a.reverse()
print(a)

#分片赋值
name=list('Perl')
name[1:]=list('ython')
print(name)

fruits=['apple','banana']
#append
fruits.append('cherry')
print(fruits)
#insert
fruits.insert(1,'lemon')
fruits.insert(1,'graspe')
print (fruits)
#remove
fruits.remove('graspe')
print (fruits)
#del
del fruits[0]
print (fruits)
#pop 唯一一个既能修改列表又返回元素值的列表方法
print(fruits.pop())
print(fruits)

