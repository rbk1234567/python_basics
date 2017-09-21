print("class in python -----------------------------------------------------------------------------------------------")

class Car1:
    name = "car with 4x4"

    def printname(self):
        print(self.name)


a = Car1() # creation of new Car class object (instatination)

a.printname() # use class method printname


print("class in python (with constructor) -----------------------------------------------------------------------------------------------")

class Car2:

    def __init__(self,name):  # constructor, self must be first argument
        self.name = name


    def printname(self):
        print(self.name)


a = Car2("really fast car") # creation of new Car class object and initialization of its values by constructor (instatination)

a.printname() # use class method printname

print("class in python (with constructor and default value) -----------------------------------------------------------------------------------------------")
# constructor can pass default values but rules as with functions default attributes apply

class Car3:

    def __init__(self,company,model,color = "red"):  # constructor, self must be first argument
        self.company = company
        self.model = model
        self.color = color


    def printcardata(self):
        print(self.company,self.model,self.color,sep="-")


a = Car3("BMW","M3") # creation of new Car class object and initialization of its values by constructor (instatination)
b = Car3("FIAT","500","black")

a.printcardata() # use class method printname
b.printcardata()

a.__setattr__("company","AUDI") # setter (mutator)

print(a.__getattribute__("company")) # getter (accessor)

#a.__delattr__("company") #deletes attribute company but generate error when method using it is called

a.printcardata()

del b # deletes instance of Car3 (to garbage collector)
