x = int(input("Please enter an integer: "))
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

name=input('What is your name?')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello, Mr.Gumby!')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs.Gumby!')
    else:
        print('Hello, Gumby!')
else:
    print('Hello,stranger')
status='friend'if name.endswith('Gumby')else'stranger'
print(status)
#is 指向相同的对象
x=y=[1,2,3]
z=[1,2,3]
print(x==y)
print(x==z)
print(x is y)
print(x is z)
print(x is not z)
