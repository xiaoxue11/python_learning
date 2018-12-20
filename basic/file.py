# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 18:07:10 2018

@author: 29132
"""
#文件不存在，无法读入，报FileNotFoundError
#f=open('somefile.txt','r')
#print(f.read())
#f.close()
#写入文件，不存在文件，创建并写入
f=open('somefile.txt','w')
f.write('Hello, ')
f.write('World!')
f.close
#读取已经存在的文件
f=open('somefile.txt','r')
print(f.read())
f.close()
#独占模式下，somefile 文件已存在，引发FileExistsError
#f=open('somefile.txt','x')
#写入模式下，同一个文件，写入新的内容，原来的内容被删除
f=open('somefile.txt','w')
f.write('I love my family!')
f.close()
f=open('somefile.txt','r')
print(f.read())
f.close()
#需要在文件末尾继续写入，用附件模式
f=open('somefile.txt','a')
f.write(' Hello, world!')
f.close()
f=open('somefile.txt','r')
print(f.read())
f.close()
#对文件同时写读操作,文件内容被修改,不用关闭文件即可直接读
f=open('somefile.txt','w+')
f.write('Baby can get it! This book is so interesting that my daughter loves it.')
import os
f.seek(0,os.SEEK_SET)
print(f.read())
f.close()
#对文件同时读写操作,原来的文件内容存在，新写入的在最后
f=open('somefile.txt','r+')
print(f.read())
f.write('This is a book.')
f.close()
f=open('somefile.txt','r')
print(f.read())
f.close()
#读取行,readline读取一行，
f=open('testfile.txt','r')
print(f.readline())
f.close()
#readlines读取所有行，并以列表[]方式返回
f=open('testfile.txt','r')
print(f.readlines())
f.close()
#写入几行
f=open('testfile1.txt','w')
f.writelines(['Baby can get it! \n', 'This book is so interesting that my daughter loves it.'])
f.close()
#关闭文件
#with open('testfile1.txt') as testfile1:
#===================example====================================================
#read string
with open('somefile.txt','r') as f:
    char=f.read(1)
    while char:
        print('The string is: ',char)
        char=f.read(1)
with open('somefile.txt','r') as f:
    for char in f.read():
        print(char)
        
with open('somefile.txt','r') as f:
    for line in f.readlines():
        print(line)
