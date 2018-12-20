# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 09:20:37 2018

@author: 29132
"""

import sys
sys.path.append('E:\python\practice')
import hello
#重新加载
import importlib
hello=importlib.reload(hello)
    
#dir:查明模块包含哪些东西，列出对象的所有属性
import class2
contend=dir(class2)
print(contend)
#no if __name__=='__main__':main():
#如果模块是运行的，则代码块被运行；如果模块是被导入的，则代码块不被运行
from hello2 import PI
def Cal_circle_area(r):
    return PI*(r**2)
def main():
    print('The area of the circle is:',Cal_circle_area(2))    
main()
#add if __name__=='__main__':main()
from hello import I
def Cal_circle_circum(r):
    return I*2*r
def main():
    print('The area of the circle is:',Cal_circle_area(3))    
main()




