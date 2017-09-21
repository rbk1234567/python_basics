#example of variables declaration, type based on syntax used
number1 = 10
number2 = 20
float1 = 3.1415
string1 = "the PI value: "
separatorline = "------------------------------------------------------------"


#example of printing string in quotes ----------------------------------------------------------------------------------------------------------------------------------------
print('"' + "A" + '"') #concatenate with '"'
print('"{}"'.format("A")) #using formatpattern.format(input string to format)
print(separatorline)

# example of getting ANSI code from letter and vice-versa ----------------------------------------------------------------------------------------------------------------------------------------
print(ord('c'))
print(chr(99))
print(separatorline)

#example of printing empty string ----------------------------------------------------------------------------------------------------------------------------------------
print("")
#example of bad call for empty string
print()
print(separatorline)

#example of concatenation and printing variables values. str() to cast to string ----------------------------------------------------------------------------------------------------------------------------------------
#using %s format sign automatically cast to string
print("value1: %s and value2: %s" % (number1,number2))
print("value1: " + str(number1) + " and value2: " + str(number2))

print("value1: %s and %s = %s" % (number1, string1,  float1))
print("value1: " + str(number1) + " " + string1 + str(float1))
print(separatorline)

#example of slicing strings ----------------------------------------------------------------------------------------------------------------------------------------
longstringtoslice = "0123456789"
print(longstringtoslice.__len__()) #ilość znaków
print(longstringtoslice[0])
print(longstringtoslice[2:]) #from 2 index letter including
print(longstringtoslice[2::]) #same as [2:]
print(longstringtoslice[:2]) #to 2 index letter not including

print(longstringtoslice[::2]) #every [::n] number from 0 index including
print(longstringtoslice[2:5]) #from first index inluding to second index not including

print(longstringtoslice[0:18:1]) #from first index (included) to second index (not included) every third value, second index can be over string lenght
print(longstringtoslice[1:9:2]) #from first index (included) to second index (not included) every third value
print(longstringtoslice[0:9:3]) #from first index (included) to second index (not included) every third value

print(longstringtoslice[:-2]) #from 0 to index = (string lenght - input value) not included
print(longstringtoslice[-2]) #index = (string lenght - input value)
print(separatorline)

#examples of other operations on strings ----------------------------------------------------------------------------------------------------------------------------------------
stringvalue = "0123456789"
stringvalue2 = "Encyclopedia"
print(stringvalue.find("45")) #returns index of searched substring beggining or -1 if not found
print(stringvalue2.lower()) #returns lowercase version of input
print(stringvalue2.count("c")) #returns number of input substring occurencies
print(stringvalue2.replace("c", "u")) #replaces one substring with another
print(stringvalue2.split("c")) #returns substrings sliced in indexes with input value. number of result substrings = string count value + 1
print(separatorline)

#example of list of strings concatenation
listofstrings = ["A", "B",  "C"]
print(" here you can put joining string ".join(listofstrings))






