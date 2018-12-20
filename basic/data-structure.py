#(Tuple) and 元组
letters=(1,2,3,5,6)
print(letters[0])
print(letters)
print(tuple('abc'))

#{set}
a_set={1,2,3,4}
a_set.add(5)
a_set.discard(3)
print(a_set)

#many cycle
num_list=[6,7,4,2,1,5,3]
print(sorted(num_list))
print(sorted(num_list,reverse=True))
for a,b in zip(num_list,sorted(num_list)):
    print(b,'is',a)

#list comprehension
b=[i for i in range(1,11)]
print(b)
a=[n for n in range(1,10) if n%2==0]
print(a)
z=[letter.lower() for letter in 'ABCDEFGHIJKLMN']
print(z)
d={i:i+1 for i in range(4)}
print(d)
g={i:j for i,j in zip('abcde',range(1,6))}
print(g)

