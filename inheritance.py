print("inheritance --------------------------------------------------------------------------------------------------")
# class(other class) syntax for inheritance

class car1:
    def __init__(self,company):
        self.company = company



class car2(car1):
    def __init__(self,company,color):
        super(car2,self).__init__(company)
        self.color = color

fiat = car1("FIAT")
bmw = car2("BMW","red")

print(fiat.__getattribute__("company"))
print(bmw.__getattribute__("company"),bmw.__getattribute__("color"),sep="-")

print("inheritance --------------------------------------------------------------------------------------------------")
# class(other class) syntax for inheritance

class car1:
    def __init__(self,company):
        self.company = company



class car2(car1):
    def __init__(self,company,color):
        car1.__init__(self,company)
        #super(car1,self)
        #self.company = company
        #super(car2,self).__init__(company)
        self.color = color

fiat = car1("FIAT")
bmw = car2("BMW","red")

print(fiat.__getattribute__("company"))
print(bmw.__getattribute__("company"),bmw.__getattribute__("color"),sep="-")

print("inheritance --------------------------------------------------------------------------------------------------")

class Ngon:
    def __init__(self,sides):
        self.sides = sides

    def getSides(self):
        return self.__getattribute__("sides")

    def setSides(self,sides):
        self.__setattr__("sides",sides)

    def printSides(self):
        print("the number of sides of "'"{}"'" is: {}".format(self.__class__.__name__,self.getSides()))

class Square(Ngon):
    def __init__(self,sidelenght):
        super(Ngon,self)  #use constructor of Ngon class to create an instance of Square
        self.sides = 4 #initialize sides value for Square class
        self.sidelenght = sidelenght #initialize sidelenght value for Square class

    def getArea(self):
        return self.sidelenght**2

ngon1 = Ngon(7)
ngon1.printSides()
ngon1.setSides(5)
ngon1.printSides()

square1 = Square(5)
square1.printSides()
print("area: ",square1.getArea())

print(isinstance(square1,Square)) #is square1 an instance of Square class?
print(issubclass(Square,Ngon))  #is Square a subclass of Ngon?


print("inheritance --------------------------------------------------------------------------------------------------")

class Aman:
    def __init__(self): #create instance of Aman class
        self.itself = "a man" #initialize itself value for that class



class Awoman(Aman):
    def __init__(self):
        #Aman.__init__(self)  #usage of other class constructor can be declared like that but its better to use super()
        #super(Aman,self)  #use constructor of Aman class and pass self(an instance of Awoman class to initialize)
        #self.itself = "a woman" #assign string value to Awoman itself property
        super().__init__()
        self.itself = "a woman"
man1 = Aman()
woman1 = Awoman()
print("class: ",man1.__class__.__name__,"value: ",man1.itself)
print("class: ",woman1.__class__.__name__,"value: ",woman1.itself)

print("inheritance accessing attributes --------------------------------------------------------------------------------------------------")

class Mammal(object):
    def __init__(self):
        self.definition = "its a mammal!"
    def printdefinition(self):
        print("defintion of {} is {}".format(self.__class__.__name__,self.definition))

class Monkey(Mammal):
    def __init__(self):
        super().__init__()
        self.property = "climbing trees"

class Dog(Mammal):
    def __init__(self):
        super().__init__()
        self.property = "have great smell"

monkey = Monkey()
dog = Dog()
mammal = Mammal()

mammal.printdefinition()
monkey.printdefinition()
dog.printdefinition()

print(Mammal.__dict__) # print class attributes
print(mammal.__dict__) # print instance attributes

print(dog.__dict__["definition"])  # access to attribute by __dict__ attributes table
print("Is a {d1} instance of a {d2}? {a1} , is {s1} subclass of {s2}? {a2}".format(d1 = "dog", d2 = "Dog", s1 = "Dog", s2 = "Mammal", a1 = isinstance(dog,Dog),a2 = issubclass(Dog,Mammal)))
print("Is a {d1} instance of a {d2}? {a1} , is {s1} subclass of {s2}? {a2}".format(d1 = "dog", d2 = "Monkey", s1 = "Dog", s2 = "Monkey", a1 = isinstance(dog,Monkey),a2 = issubclass(Dog,Monkey)))




