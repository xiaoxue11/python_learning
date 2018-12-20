a,b=0,1
while a<1000:
    print(a,end=',')
    a,b=b,a+b

name=''
while not name.strip():
    name=input('Please enter your name: ')
print('Hello,{}!'.format(name))

