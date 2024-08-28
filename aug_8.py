# dictionary 

# str, list, tuple 

# dictionary is a key value pair -- item 

dict1 = {
    'Black':'Mercedes',
    'apple':'RED',
    'fruit':'Orange',
    # (1,2j,3j):'Berry'
}

# key - immutable, unique , cannot be duplicate 
# value - mutable , can be duplicate

# key should have value, value should have key 

# print(dict1)

# keys

# print(dict1['apple'])
# print(dict1.get('Apple',dict1.get('apple')))
# if dict1.get('apple'):
#     print("True")
# else:
#     print("false")

# print(dict1.keys())
# a = dict1.keys()
# for i in dict1.keys():
#     print(i)

# print(dict1.values())

# print(dict1.items())

# for k,v in dict1.items():
#     print(k,v)
# for i in dict1:
#     print(dict1[i])


dict1={}

dict1['one']=1
# dict1['two']=2

six='eight'

dict1.update({'three':3,'four':4,'four':5,8:8},six=6)
dict1['two']=200
print(dict1)


dict1={
    1:10,
    2:20,
    3:30,
    4:40,
    5:50
}

# Write a Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}


# Write a Python program to create a dictionary from a string.
# Note: Track the count of the letters from the string.
# Sample string : 'w3resource'
# Expected output: {'w': 1, '3': 1, 'r': 2, 'e': 2, 's': 1, 'o': 1, 'u': 1, 'c': 1}
out={}
s='w3resource'
for i in s:
    out[i]=out.get(i,0)+1
print(out)


# Write a Python program to get the top three items in a shop.
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3







































shop_items={'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}


# # Initialize an empty list to hold the top three items
top_three_items = []

# # Iterate through the items in the dictionary
for item, value in shop_items.items():
    # If the list has fewer than 3 items, add the current item
    if len(top_three_items) < 3:
        top_three_items.append((item, value))
        print(top_three_items)
    else:
        # Find the item with the smallest value in the top three list
        min_index = 0
        for i in range(1, len(top_three_items)):
            if top_three_items[i][1] < top_three_items[min_index][1]:
                min_index = i
        # If the current item has a larger value than the smallest in the top three list, replace it
        if value > top_three_items[min_index][1]:
            top_three_items[min_index] = (item, value)
print(top_three_items)

# Sorting the list by value in descending order
for i in range(len(top_three_items)):
    for j in range(i + 1, len(top_three_items)):
        if top_three_items[i][1] < top_three_items[j][1]:
            top_three_items[i], top_three_items[j] = top_three_items[j], top_three_items[i]

# # Print the expected output
for item, value in top_three_items:
    print(f"{item} {value}")


shop_items = {'item1': 45.50, 'item2': 35, 'item3': 41.30, 'item4': 55, 'item5': 24}

# Sort the items based on their values in descending order and get the top three items
sorted_items = sorted(shop_items.items(), key=lambda item: item[1], reverse=True)[:3]

# Print the expected output
for item, value in sorted_items:
    print(f"{item} {value}")