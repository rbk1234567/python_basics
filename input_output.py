#output formating examples
print("Hello {}, how are you?".format("John"))
print("Hello {1}, have you seen {0} today?".format("John", "Mike"))
print("Hello {0}, have you seen {1} today?".format("John", "Mike"))
print("Hello {john}, have you seen {mike} today?".format(john="John",mike="Mike"))

PI=3.1415
print("%3.2f" %PI)

number = float(input("enter number: ")) #input(OPTIONAL TEXT MESSAGE) gets input value from standard input
print("number: "+str(number), type(number))

input1 = input("entry: ")
number = eval("input1")

print("number "+str(number), type(number))


#using separator and end for strings
text1 = "hello"
text2 = "world"
print('foo', 'bar', sep="***")

