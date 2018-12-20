# -*- coding: utf-8 -*-
"""
Created on Fri Nov  2 16:11:41 2018

@author: 29132
"""

print('\t\napple\t\ncherry\t\norange')
print('\n\tapple\n\tcherry\n\torange')
school_name='Northwestern University'
student_name='sophia'
message=school_name+student_name
print(message)
message=school_name+' '+student_name
print(message)
print("I'm very well.Thank you so much!")
print('He said:"I feel sorry to hear that message."')
print('I\'m very well.Thank you so much!')
print("He said:\"I feel sorry to hear that message.\"")
message=' I love my daughter '
print(message.title())
print(message.lower())
print(message.upper())
print(message.rstrip())
print(message.lstrip())
print(message.strip())
print(message.replace('daughter','husband'))
#%s部分称为转换说明符，标记了需要插入转换值的位置，s的值会被格式化为字符串
message="Hello,%s,%s enought for ya?"
values=('world','hot')
print(message%values)
print('Hello,{} {} enought for ya'.format('world','hot'))
#find
title='I love my daughter'
print(title.find('my'))
#format
print("{0}, {1} and {2}".format("first", "second", "third"))

#字符串格式设置
width=int(input('Please enter width: '))
price_width=10
item_width=width-price_width
header_fmt='{{:{}}}{{:>{}}}'.format(item_width,price_width)
fmt='{{:{}}}{{:>{}.2f}}'.format(item_width,price_width)
print('='*width)
print(header_fmt.format('Item','Price'))
print('-' * width)
print(fmt.format('Apples',0.4))
print(fmt.format('Pears',0.5))
print(fmt.format('Cantaloupes',1.92))
print(fmt.format('Dried Apricots(16 oz.)',8))
print(fmt.format('Prunes(4 lbs.)',12))
print('='*width)

#join
seq=['1','2','3']
sep='+'
temp=sep.join(seq)
print(temp)
print(eval(temp))
#split
a='1+2+3+4+5'.split('+')
print(a)










