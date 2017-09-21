print("WHILE loop ----------------------------------------------------------------------------------------------------")
# simple while loop

target = 10
counter = 3

while counter<=target:
    print(counter)
    counter = counter + 1



print("WHILE loop fibbonachi ----------------------------------------------------------------------------------------------------")
target = 12
counter = 0
previous = 0
actual = 1

while counter<=target:
    print(previous)
    sum = previous + actual
    previous = actual
    actual = sum
    counter += 1    # += operator increases counter by 1 (counter = counter + 1)

print("WHILE loop Armstrong number ----------------------------------------------------------------------------------------------------")

number = 155  #example 153, 670
digits = len(str(number))
sum = 0
counter = 0
while counter<digits:
    sum += int(str(number)[counter])**digits
    counter += 1
    print("sum = ", sum)
if sum == number:
    print("%s is an Armstrong number" % number)
else:
    print("%s is not an Armstrong number" % number)
