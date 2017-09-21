print("local namespaces ----------------------------------------------------------------------------------------------")

a = 10  # global a

def fouter():
    a = 20  # local a

    def finner():
        a =30 # nested local a
        print(a)

    finner()
    print(a)

fouter()
print(a)

print("global namespaces ----------------------------------------------------------------------------------------------")





def Bouter():
    global b  # refers to global b
    b = 20

    def Binner():
        global b #refers to global b
        b = 30
        print(b)


    Binner()
    print(b)

b = 10  # this is global b
Bouter()

print(b)