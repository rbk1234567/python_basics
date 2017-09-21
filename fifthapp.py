a=1
b=2
c=3
tuple1 = (a, b, c)
#tuples can concatenate
print(tuple1)
print(b)
tuple1 = tuple1 + tuple1
print(tuple1)
#lists can concatenate
list1 = [a, b, c]
print(list1)
print(a)
list1 = list1 + list1
print(list1)

#sets can't concatenate
#sets are using logical operations with operators ^ & - |
set1 = {a, b, c}
set2 = {b, c}
print(set1)

print(set1^set2)
print(b)

dict1 = {"key1":"value1"}
dict1["c"] = "value" #adds an item with specified key and value to dictionary
print(dict1)
print(dict1["c"])
del dict1["c"] #deletes item with specified key
print(dict1)
print("values:", dict1.values()) #prints only values
print("keys:", dict1.keys()) #prints only keys
print("items:", dict1.items()) #prints items





