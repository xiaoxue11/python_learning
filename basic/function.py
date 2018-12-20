import math 
def aa():
    return 'something'
def fahrenheit_convet(C):
    fahrenheit=C*9/5+32
    print (fahrenheit)
def weight_convert(g):
    weight=g/1000
    return weight;
def triangle_side(a,b):
    third_side=math.sqrt(a*a+b*b)
    return 'The right triangle third side\'s length is '+str(third_side)
def invest(amount,rate,time):
    print('principal amount: '+str(amount))
    for i in range(1,time+1):
        print('year '+str(i)+' : '+str(amount*(1+rate)**i))
def even(num):
    for i in range(1,num):
        if(i%2==0):
            print(i)
def fibs(num):
    result=[0,1]
    for i in range(num-2):
        result.append(result[-2]+result[-1])
    return result

def change(n):
    n[0]='Mr.Gumby'
names=['Mrs.Entity','Mrs.Thing']
change(names[:])
print(names)

def init(data):
    data['first']={}
    data['middle']={}
    data['last']={}
def lookup(data,label,name):
    return data[label].get(name)
def store(data,full_name):
    names=full_name.split()
    if len(names)==2: names.insert(1,'')
    labels='first','middle','last'
    for label,name in zip(labels,names):
        people=lookup(data,label,name)
        if people:
            people.append(full_name)
        else:
            data[label][name]=[full_name]

