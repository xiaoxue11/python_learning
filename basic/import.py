# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 10:35:08 2018

@author: 29132
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 09:20:37 2018

@author: 29132
"""

import sys
sys.path.append('E:\python\test')
import hello
import importlib
hello=importlib.reload(hello)

#methods to reference module
from class2 import Bird
xique=Bird()
xique.__init__()
print(xique.hungry)
xique.eat()
print(xique.hungry)
xique.eat()
#only import Bird class,so check_index is not defined
#print(check_index(1))
#NameError: name 'check_index' is not defined

import class2
xique=class2.Bird()
xique.__init__()
print(xique.hungry)
xique.eat()
print(xique.hungry)
xique.eat()
#import all,so know chch_index
print(class2.check_index(2))


from class2 import *
xique=Bird()
xique.__init__()
print(xique.hungry)
xique.eat()
print(xique.hungry)
xique.eat()
print(check_index(2))





