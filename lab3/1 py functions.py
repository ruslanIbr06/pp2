def myFunction(name):
    print("Hello, " + name)
myFunction("Ruslan")
#Hello, Ruslan
name = "World!"
myFunction(name)
#Hello, World!
def createSentence(word1, word2):
    print(word1 + " " + word2)
word1 = "Good"
word2 = 'morning!'
createSentence(word1, word2)
#Good morning!
def toBuyList(*list):
    print('You should buy ' + list[0])
toBuyList('apples', 'milk', 'eggs')
#You should buy apples
def carList(car1, car2, car3):
    print('He bought ' + car1)
carList(car1 = 'Toyota', car2 = 'Mitsubishi', car3 = 'BMW')
#He bought Toyota
def nameSurname(**person):
    print('His name is ' + person['name'])
nameSurname(name = 'Luke', surname = 'Skywalker')
#His name is Luke
def multiplyBySix(x, /):
    print(x * 6)
multiplyBySix(10)#60
multiplyBySix(6)#36
multiplyBySix(2)#12
def printX(*, x):
    print(x)
printX(x = 10)#10
printX(x = 100)#100
printX(x = 1000)#1000
def sumNums(a, b, /, *, c, d):
    print(a+b+c+d)
sumNums(10, 35, c=50, d=30)#125
def someFunction(x):
    if(x>5):
        output = x + someFunction(x-1)
        print(output)
    else:
        output = 0
    return output
someFunction(20)
'''
6
13
21
30
40
51
63
76
90
105
121
138
156
175
195
'''

