print("casting types---------------------------------------------------------------------------------------------------------")
float1 = 3.1415
integer1 = 4
string_text = "hello"
string_number = "2.71"
list1 = [1, 2, 3]
list2 = [[1, 2], [3, 4]]
tuple1 = ("a", "b", "c")
set1 = {41, 88, 25}
dictionary1 = {"key1":"value1", "key2":"value2"}

print(float1)
print(integer1)
print(string_text)
print(string_number)
print(list1)
print(tuple1)
print(set1)
print(dictionary1)

print("-----------------------------------------------------------------------------------------------------------------------")

print("float to int", int(float1))
print("float to string", str(float1))
print("int to float",  float(integer1))

print("string to float", float(string_number)) #this work
#print(int(string_number))  #this will throw error because string_number has fraction sign and int type is non fraction type

print("string to list", list(string_text)) #convert string to list 
print("tuple to list", list(tuple1)) #convert tuple to list
print("set to list", list(set1))
print("dictionary to list (lossy convertion)",  list(dictionary1)) #conert dictionary to list. Part of data will be lost. Only keys are converted
print("list to tuple", tuple(list1))
print("set to tuple", tuple(set1))
print("dictionary to tuple (lossy convertion", tuple(dictionary1))
#print("list to dictionary", dict(list1)) #this wont work until list contain paired values
print("list to dictionary", dict(list2)) #this works but list must contain minimum 2 paired values like [[x1,y1],[x2,y2],...[xn,yn]






