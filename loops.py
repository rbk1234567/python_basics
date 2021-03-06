print("if condition ---------------------------------------------------------------------------------------------------------------")

x = 2
y = 3
if x>y:
    print("x is bigger")
elif x==y:
    print("x and y are equal")
else:
    print("y is bigger")



print("if condition with empty statement (pass keyword) ---------------------------------------------------------------------------------------------------------------")

if x>y:
    print("x is bigger")
elif x==y:
    print("x and y are equal")
else:
    pass   #pass keyword is a must for empty statement in loop

print("objects values comparison ---------------------------------------------------------------------------------------------------------------")
# to check are objects have same values use: ==


val1 = 3.14
val2 = 3.14
str1 = "abc"
str2 = "abc"
list1 = [1,2,3]
list2 = [1,2,3]

if val1 == val2:
    print("val1-val2, true, same value")
else:
    print("val1-val2, false, not same value")

if str1 == str2:
    print("str1-str2, true, same value")
else:
    print("str1-str2, false, not same value")

if list1 == list2:
    print("list1-list2, true, same value")
else:
    print("list1-list2, false, not same value")

print("objects comparison---------------------------------------------------------------------------------------------------------------")
# to check weather objects are pointing same place in memory use keywords: is, is not
# primitive types share same memory but lists, tuples, sets and dictionaries not. They are initialized as new objects

val1 = 3.14
val2 = 3.14
str1 = "abc"
str2 = "abc"
list1 = (1,2,3)
list2 = (1,2,3)

if val1 is val2:
    print("val1-val2, true, same object")
else:
    print("val1-val2, false, not same object")

if str1 is str2:
    print("str1-str2, true, same object")
else:
    print("str1-str2, false, not same object")

if list1 is list2:
    print("list1-list2, true, same object")
else:
    print("list1-list2, false, not same object")

print("comparison of different types ---------------------------------------------------------------------------------------------------------------")
# can't compare two different type objects values without type casting. this will always return false


list1 = [1,2]
set1 = {1,2}
tuple1 = (1,2)
dict1 = {"key1":1,"key2":2}

if list1 == set1:
    print("list1 and set1 have same values")
else:
    print("list1 and set1 haven't got same values")
if list1 == tuple1:
    print("list1 and tuple1 have same values")
else:
    print("list1 and tuple1 haven't got same values")
if list1 == dict1.values():
    print("list1 and dict1 have same values")
else:
    print("list1 and dict1 haven't got same values")

# comparison with type casting

if list1 == list(set1):
    print("list1 and set1 have same values %s" % list(set1))
else:
    print("list1 and set1 haven't got same values")

if list1 == list(dict1.values()):
    print("list1 and dict1 have same values %s" % list(dict1.values()))
else:
    print("list1 and dict1 haven't got same values")

print("FOR loop ---------------------------------------------------------------------------------------------------------------")
# in this example prints every second number within specified range. Range function atributes are (start,end,stepsize) or (end, stepsize) or (end)

startvalue = int(input("enter start value:"))
endvalue = int(input("enter end value:"))

for value in range(startvalue,endvalue,2):
    print(value)
print(list(range(startvalue,endvalue,2))) #displays list of values generated by range function

print("FOR loop over list ---------------------------------------------------------------------------------------------------------------")
# iteration through the list. gets list lenght and use it as range

list1 = ["a","b","c","d"]

for i in range(list1.__len__()): #use of list lenght atribute
    print(list1[i])
for i in range(len(list1)): #use len() function to get list lenght
    print(list1[i])
else:                           # optional else statement to do something after all loop iterations passed
    print("no more to print")

print("FOR loop over list break ---------------------------------------------------------------------------------------------------------------")

list1 = [1,2,3,4]

for i in range(len(list1)):
    if list1[i]>2:
        break
    elif list1[i]==2:
        print("equal to 2")
    else:
        print("lower than 2")
else:
    print("end of loop") # loop never reach this line due to break after list value is grater than 2


print("FOR loop over list continue ---------------------------------------------------------------------------------------------------------------")
# use continue to go back to top of for loop. It will ignore printing "o" in this example but loop will continue for rest of letters
string1 = "Aloha!"

for i in range(len(string1)):
    if string1[i]=="o":
        continue
    print(string1[i])

print("---------------------------------------------------------------------------------------------------------------")


