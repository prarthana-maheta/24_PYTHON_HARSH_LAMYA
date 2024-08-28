# list --- mutable [] iterable ordered
# string --- immutable '' iterable ordered 
# tuple --- immutable () iterable ordered 

# list v/s tuple 

# tu = (1,2,3,4)

# tech
# li = list(tu)
# li[0]=12

# print(tuple(li))

# # pack-unpack 

# # red,yellow = ('apple','banana','orange')

# # print(red,yellow)


# t1 = ['happy'],['sad']

# # # 
# print(t1)
# print(type(t1))

# list1 =[1,2,3,5]
# list2 =[5,6,7,8]

# print(list1/list2)

# a=b
# c=a.copy()


# Write a Python program to replace the last value of tuples in a list.
# s =[(10, 20, 40), (40, 50, 60), (70, 80, 90)]
# Expected Output: [(10, 20, 100), (40, 50, 100), (70, 80, 100)]

# [1,2,3,4,5,6,7]
# o=[]
# for i in s:
#     l = list(i)
#     l[-1]=100
#     o.append(tuple(l))
# print(o)

# Write a  Python program to sort a tuple by its float element.
# Sample data: [('item1', '12.20'), ('item2', '15.10'), ('item3', '24.5')]
# Expected Output: [('item3', '24.5'), ('item2', '15.10'), ('item1', '12.20')]

# for i in range(len(s)):
#     print(s[i])
#     for j in range(i+1,len(s)):
#         print(s[i+1])

# window techniue
# nav method


# Write a  Python program to remove an empty tuple(s) from a list of tuples.
# Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

list1 = [1,2,3,4,5]

# for i in list1:
# if 2 in list1:
#     print("2 se bada hai")
# print("------")
# else:
#     print("2 se chota hai")

# print("Yes") if 2 in list1 else None

# print(ans)

# ans = [f"{i} 2 se bada hai" for i in list1  if i>2 ]

# list[]

# ans = [f"{i} 2 se bada hai" if i>2 else f"{i} 2 se chota hai" for i in list1]
# ans = [f"{i} 2 se bada hai" if i>2 else list for i in range(len(list1))]
# print(ans)