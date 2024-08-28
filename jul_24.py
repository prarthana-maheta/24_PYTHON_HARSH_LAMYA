# str1 = 'hello' -- plain text

# security methos od string 

# text --------encrypt--------decrypt-----text
# plain text ------ cipher text --------- plain text
# sender --- me 
# msg = 'Hello harsh dont share this message to lamya'
# print(msg)

# msg1=msg.encode('utf-16')
# print(msg1)
# print(msg1.decode('utf-8'))
# harsh
# receiver --harch
# SHA-256
# SHA-512
# MD5
# MD3



# maniplulation method

# str1= "hello,harsh,how,are,you?"
# out="hello**harsh**how**are**you?"

# str2=str1.split()

# print(str2)
# print('**'.join(str2))
# print(' '.join('123'))


# ans =(input("enter number")), input("enter 2")
# print(ans)
# print(type(ans))

# array does not support

# list = []
# mutable , iterable, ordered, can support multiple data type, no fix size

# li = [12,'123',12.4,['apple',2,3,4]]


# print(li[2:])

# adding elements in list 
str1 = str()
li =[]
li2 = list()
print(li2, str1)

# append() add single elements at a time, at last 

# extend() add multiple elemets at a time, at last

# insert() add single element at specify place

li2.append('R')
li2.append('O')

li2.extend('YAL')
li2.insert(1,'o')
li2[1]='o'
print(li2)

li2.insert(-2,'a')

print(li2)


# deletion methods

# 4- delete

# pop()

# li1 = [1,2,3,4,5]
# l=[]
# x=li1.pop(2)
# # l.append(x)
# print(l)


# # li1.remove(0)
# print(li1)

# # li1.clear()

# print(li1[1:3])
# del li1[1:3]
# print(li1)


# funstions

# aggregaryion functions
# print('1'+1)
# li = [1,2,3,4,5,6,7,8,9]
# print(max(li))
# print(min(li))
# print(sum(li))

li1 = ['apple','Apple','B','Z','z']
# print(max(li))
# print(min(li))
# print(sum(li))

# print(li.count('apple'))

li2 = li1
li3 = li.copy()

li2.append('Royal')
li1.append("Harsh")
li3.append('lamya')
print(li1)
print(li2)
print(li3)