word=['cat','window','watermelon']
for i in word:
    print(i,len(i))
for w in word[:]:
    print(w)
    if len(w)<10:
        word.insert(0,w)
        print(word)
#dict 迭代
d={'x':1,'y':2,'z':3}
#默认迭代key
for key in d:
    print(key,' corresponds to ',d[key])
#iterate value
for value in d.values():
    print('corresponds to ',value)
#key and value both    
for key,value in d.items():
    print(key,' corresponds to ',value)

names=['anna','beth','george','damon']
ages=[12,45,32,102]
for i in range(len(names)):
    print(names[i],'is',ages[i],'years old')
print(list(zip(names,ages)))
for name,age in zip(names,ages):
    print(name,'is',age,'years old')
letters=['a','b','c','d','e','f']
for num,letter in enumerate(letters):
    print(letter,'is',num+1)

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []).append(girl)
print(letterGirls)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
