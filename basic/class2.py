# -*- coding: utf-8 -*-
"""
Created on Sat Nov  3 21:57:38 2018

@author: 29132
"""

class FooBar():
    def __init__(self,value=42):
        self.somevar=value
#herit
class A:
    def hello(self):
        print("Hello,I'm A.")
class B(A):
    pass

class Bird:
    def __init__(self):
        self.hungry=True
    def eat(self):
        if self.hungry:
            print('Aaaaa')
            self.hungry=False
        else:
            print('No,thanks!')

class SongBird(Bird):
    def __init__(self):
        super().__init__()#对超类调用关联
        self.sound='Squawk!'
    def sing(self):
        print(self.sound)

#基本序列和映射协议
def check_index(key):
    if not isinstance(key,int):raise TypeError
    if key<0: raise IndexError
class ArithmeticSequence:
    def __init__(self,start=0,step=1):
        self.start=start
        self.step=step
        self.changed={}
    def __getitem__(self,key):
        check_index(key)
        try:#修改过，返回修改的值
            return self.changed[key]
        except KeyError:#KeyError是指列表中没有这个键值，未作过修改
            return self.start+key*self.step
    def __setitem__(self,key,value):
        check_index(key)
        self.changed[key]=value

#list,dict和str派生
class CounterList(list):
    def __init__(self,*args):
        super().__init__(*args)
        self.counter=0
    def __getitem__(self,index):
        self.counter+=1
        return super(CounterList,self).__getitem__(index)
#iter 迭代器
class TestIterator:
    value=0
    def __next__(self):
        self.value+=1;
        if self.value>10:raise StopIteration
        return self.value
    def __iter__(self):
        return self
#生成器
nested=[[1,2],[3,4],[5]]
def flatten(nested):
    for sublist in nested:
        for element in sublist:
            yield element
print(sum(i**2 for i in range(10)))
    




    
