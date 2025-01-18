#Python variables
x = 4
y = "hello"
print(x, y)
x = ", world!"
print(y+x)
a=str(4)
b=float(4)
c=int(4)
print(a, c, b)
print(type(a), type(b), type(c))
z = 'hello'
if (z == y):
    print("String variables can be declared either by using single or double quotes")
Y = "good bye"
if (y != Y):
    print("Y does not overwrite y")   
#Variable names    
asd = "1"
as_d = "1"
_as_d = "1"
aSd = "1"
ASD = "1"
asd2 = "1"
#can not begin with number, must not contain space or "-" symbol
varName = "a" #camel case
VarName = "a" #pascal case
var_name = "a" #snake case
print("=====================")
#Assign multiple variables
x, y, z = "x", "y", "z"
print(x, y, z)
x = y = z = "hi"
print(x, y, z)
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x, y, z)
print("=====================")

#Output variables
a = 100
b = 200
print(a + b)
a = "100"
b = "200"
print(a + b)
print("=====================")

#Global variables
x = "Hello "
def helloWorld():
    print(x +"World!")
helloWorld()
def helloThere():
    global y
    y = "there!"
    print(x + y)
helloThere()
def howAreYou():
    global x, y
    x, y = "How are ", "you?"
howAreYou()
print(x + y)
