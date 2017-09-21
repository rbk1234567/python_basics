print("list in python----------------------------------------------------------------------------------------------------------------")
#list type in python declared with []
item = ["A", "B", 2.71];
list = [1, 2, 3, "hello",  3.1415,  item]  #list mebmers can be of any type. It can be a list too.
print(list[5]) #print list member from given index
print(list[5][2]) #to acces nested list item

#example of list mutability
print(list)
list[0] = "changed 1 to this text"
print(list)


print("nested list in python----------------------------------------------------------------------------------------------------------------")
#examples of list nesting and accessing to nested list values
deeplist1 = ["a", "b", "c"]
deeplist2 = ["d", "e", "f"]
sublist1 = [1, 2, 3, deeplist1]
sublist2 = [4, 5, 6, deeplist2]
mainlist = [sublist1,  sublist2]
print(mainlist)
print(mainlist[0][2])
print(mainlist[0][3][2])

print("tuple type in python----------------------------------------------------------------------------------------------------------------")
#tuple type in python (immutable list) declared with ()
tuple = (1, 2, 3, "end")
# tuple[0] = "beggining" #this will generate error. cant change tuple values
print(tuple[0]) #can acess value for reading

print("set type in python----------------------------------------------------------------------------------------------------------------")
#set type in python declared with {}. Set is not ordered and cannot acces values by index. Set delete duplicated values when created.
set = {1, 2, 4, 2, "abc", 5, 3, "abc"}
print(set)

print("dictionary type in python----------------------------------------------------------------------------------------------------------------")
#dictionary type in python declared with {1:value:key:2} Bond between key and value. Value can be accessed by key only.
dictionary = {1:"val1","key1":2, "key3":3}
print(dictionary[1]) #acces to a value by key, key and value can be of any type.
# print (dictionary[2]) #this will generate error because 2 is a value here not a key
dictionary[1] = "value1"
print(dictionary[1]) #dictionaries are mutable
print(dictionary.get(1)) # get value by key

print("mebership in lists (in keyword) ---------------------------------------------------------------------------------------------------------------")
# use keyword in to check weather list contains specified value
print(1 in deeplist1) #false
print(1 in sublist1) #true
print("a" in sublist1) #false (looking in top list)
print("a" in sublist1[3]) #true (looking in sublist)






