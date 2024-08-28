# string, list, tuple, dict 

# set and , frozen set 

# t1 =(1,2,3)
# s1 ='123'

# set does not allow duplicate values 
# only has unique values 
# un-indexed
# un-ordered
# unchangeable   
# iterable


# frozen set --- immutable

set1 = {100,10,200,30,4,3,2,1}
# set2 = set()

# set1[2]='apple'
# print(set1)
# print(type(set2))

# functions
# print(len(set1))
# print(min(set1))
# print(max(set1))

# print(set(sorted(set1)))

# methods

# set1 = {100,10,200,30,4,3,2,1}
# set1.add('str1')
# set1.add('str2')

# set1.update(['str3','str4'])

# set1.remove('str1')
# print(set1)

# set2 = {'Apple',True,1,'Royal',False,0,None,-1,2,4,0,}
# print(set2)

set1={1,2,3,4,5}
set2={4,5,6,7,8,9}

# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set2.difference(set1))
# set2.difference_update(set1)
# set2.intersection_update(set1)
print(set2.symmetric_difference(set1))
set2.symmetric_difference_update(set1)
print(set2)

# Write a Python program to find all the unique words and count the frequency
# of occurrence from a given list of strings. Use Python set data type.

l1=['Red', 'Green', 'Red', 'Blue', 'Red', 'Red', 'Green']
# {'Red': 4, 'Blue': 1, 'Green': 2}

s1=set(l1)
d1={}

for i in s1:
    d1[i] = l1.count(i)

print(d1)



