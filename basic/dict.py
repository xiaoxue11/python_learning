# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 17:38:22 2018

@author: 29132
"""

#{dictionary}
#dict function
items=[('name','Gumy'),('age',42)]
print(dict(items))
#if key and value repeat,only show one
a={'key':123,'key':123}#
print(a)
#basic grammar:{'key1':value1,'key2':value2}
Company={'BIDU':'Baidu',
             'SINA':'Sina',
             'YOKU':'Youku'
}
#basic manipulate:
#add new item:name['key']=value
Company['ALI']='Alibaba'
print(Company)
#len(d)
print(len(Company))
print(Company['BIDU'])
#modify
Company['YOKU']='Youtobe'
print(Company)
#del
del Company['YOKU']
print(Company)
#updata
Company.update({'FB':'Facebook','HW':'Huawei'})
print(Company)
#copy and deepcopy
from copy import deepcopy
x={'name':'zhangxue','age':30,'skill':['c','python']}
y=x.copy()
z=deepcopy(x)
y['skill'].remove('c')
print(x)
print(y)
print(z)
#clear
m=x
x.clear()
print(x)
print(m)
#fromkeys
p={}.fromkeys(['name','age'])
print(p)
q=dict.fromkeys(['name','age'])
print(q)
p1=dict.fromkeys(['name','age'],'unknown')
print(p1)
#items
x={'username':'admin','machines':['foo','bar','baz']}
y=x.items()
print(list(y))
print(len(y))
#get
d={}
print(d.get('name'))
print(d.get('name','NA'))
d['name']='Eric'
print(d.get('name'))
#pop
d={'x':1,'y':2}
d.pop('x')
print(d)
#setdefault
d={}
print(d.setdefault('name'))
d={'name':'zhangxue'}
print(d.setdefault('name'))
#format_map
phonebook={'Beth':'1234','Alice':'3456','Cecil':'5678'}
p="Cecil's phone number is {Cecil}.".format_map(phonebook)
print(p)

#example
people={'Alice':{'phone':'2341','addr':'Foo drive 23'},
        'Beth':{'phone':'9102','addr':'Bar street 42'},
        'Cecil':{'phone':'3158','addr':'Baz avenue 90'},
}
labels={'phone':'phone number','addr':'address'}
name=input('Name: ')
request=input('Phone number(p)or address(a)?:')
key = request 
if request=='p':key='phone'
if request=='a':key='addr'
#get提供默认值
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
if name in people:
    print("{}'s {} is {}.".format(name,label,result))
else:
    print('There is no person called this name.')




