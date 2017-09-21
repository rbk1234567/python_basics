print("functions in python -------------------------------------------------------------------------------------------")
# declaration begins with def keyword and end with :
# documentation can be included below function name with """simple documentation here""" and accessed with ___doc___ property
# function can get multiple atributes
# atributes can be passed by order or by keyword (order attributes must be placed before those with keyword)
# attributes can have default values (attributes with default values must be placed after those without default values)

def car_function(company,model,color="silver"):
    """this function prints car properties
    default color is silver"""
    print("company: "+company+" model: "+model+" color: "+color )


car_function("FORD","Fiesta","black")
car_function("FIAT","Bravo") # default color will be used

print('"{}"'.format(car_function.__doc__)) # print function documentation text

print("functions in python (attributes order) -------------------------------------------------------------------------------------------")
#attributes are passed by order to print function
def car_function2(company,model,color):
    print(company,model,color,sep="-")

car_function2("AUDI","A1","red")
#car_function2("AUDI",color="silver","A1") # ordered attribute (model A1) can't be placed after those called by keyword
car_function2(color="blue",company="AUDI",model="A3") # this will work. values are fit by keyword even if the order is different
car_function2("AUDI",color="red",model="A6") #this will work. order value is before keywords values

print("functions in python (attributes order) -------------------------------------------------------------------------------------------")
#attributes are passed by order to print function

#def car_function3(company,model="A1",color): # this wont work. attribute with default value before this without
def car_function3(company,color,model="M5"): #this will work
    print(company,model,color,sep="-")

car_function3("BMW","blue","X3")
car_function3(model="X5",company="BMW",color="white")
car_function3("BMW",color="orange")
car_function3(color="yellow",company="BMW")

print("functions in python (non-fixed number of attributes *args) -------------------------------------------------------------------------------------------")
# it is possible to pass non-fixed number of attributes by using * before attribute name

def car_function4(model,company,*color):  # display colors list
    print(company, model, color, sep=">>")

car_function4("Astra","OPEL","red","blue","black")

def car_function5(model,company,*color):  # display every color from color attributes list
    print(company,model,sep="-")
    for color in color:
        print(color)

car_function5("Mokka","OPEL","white","blue","gray")

print("functions in python (non-fixed number of attributes **kwargs) -------------------------------------------------------------------------------------------")

def car_function6(company,model,color,**owner):
    for key in owner:
        print(company, model, color, owner[key],sep="/")


car_function6("HYUNDAI","i10","red",owner1="John",owner2="Joe",owner3="Jack")

print("functions in python (non-fixed number of attributes list of attributes) -------------------------------------------------------------------------------------------")

def car_function7(company,model,owners):

    for i in range(len(owners)):
        print(company,model,owners[i][1],owners[i][0],sep="-")

car_function7("DACIA","Sandero",[["Mary","red"],["Ann","blue"],["Helen","white"]])

print("functions in python (non-fixed number of attributes list of attributes) -------------------------------------------------------------------------------------------")
# in this example **kwarg is dictionary part. keywords passed to function are used to get corresponding values

def car_function8(company,model,**ownerdata):
    for key in ownerdata:
        print(company,model,ownerdata[key],sep="//")


dict1 = dict({"John":"red","Mike":"black","Joel":"white"})
car_function8("JEEP","Cherokee",Mike=dict1.get("Mike"),John=dict1.get("John"),Joel=dict1.get("Joel"))

print("functions in python (non-fixed number of attributes used on call not in declaration **kwarg) -------------------------------------------------------------------------------------------")
# it is possible to use *arg and **kwarg

def car_function9(company1,company2,company3):
    print(company1)
    print(company2)
    print(company3)

company = {"company1":"FIAT","company2":"RENAULT","company3":"CITROEN"}
car_function9(**company)

print("functions in python (passing lists and variable scope) -------------------------------------------------------------------------------------------")

def add_to_list(listvar):
    mylist.append(listvar)
    print("function list: "+str(mylist))

mylist = [1,2,3]
add_to_list(["a","b"])
print("outside list: "+str(mylist))

print("functions in python (passing lists and variable scope) -------------------------------------------------------------------------------------------")

def show_list(mylist):
    mylist=[1,2]
    print("inside:"+str(mylist))

mylist=["a","b","c"]
show_list(mylist)
print("outside: "+str(mylist))

print("anonymous functions -------------------------------------------------------------------------------------------")
# anonymous functions are functions without name with one statement only. They are declared with lambda keyword


value = lambda x: x^2 # function work when assigning value to variable
print("lambda function output: ",value(4))

print("anonymous functions as attribute -------------------------------------------------------------------------------------------")
# in this example filter uses labda function to check weather list value can be divided by 3


list1 = [1,3,5,8,9]
print(list(filter(lambda y:y%3==0,list1)))

print("anonymous functions as attribute -------------------------------------------------------------------------------------------")
# in this example map uses labda function to do operation on list value

list1 = [1,3,5,8,9]
print(list(map(lambda y:y % 3,list1)))

print("function bind -------------------------------------------------------------------------------------------")
# function can be threated like object and be binded to variable name
def function():
    print("function")

a = function()
a  # it will call function()
