class stringManipulation:
    def __init__(self):
        self.string = ""   
    def getString(self): 
        self.string = input("Enter your string: ")    
    def printString(self):
        print(self.string.upper())






class Shape:
    def area(self):
        return 0

    
class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length ** 2


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width




class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"Point coordinates are: ({self.x}, {self.y})")
    def move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
    def dist(self, other_point):
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount):
        self.balance += amount
        print(f"You have deposited {amount}. Balance: {self.balance}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            print(f"Error! You tried to withdraw {amount}, your current balance: {self.balance}")
        else:
            self.balance -= amount
            print(f"You have withdrawn {amount}. Balance: {self.balance}")


def isPrime(n):
    if n < 2:
        return False
    else:
        for i in range(2, n):
            if n % i == 0:
                return False
            else:
                return True


a = stringManipulation()
a.getString()
a.printString() 
#outputs entered string in upper register, input: "qwerty", output: "QWERTY"
shape = Shape()
print("Shape area:", shape.area())# Shape area: 0
square = Square(6)
print("Square area:", square.area())#Square area: 36
rectangle = Rectangle(9, 7)
print("Rectangle area:", rectangle.area())#Rectangle area: 63


point1 = Point(4, 6) #Point coordinates are: (4, 6)
point1.show()
point1.move(9, 7) #Point coordinates are: (9, 7)
point1.show()
point2 = Point(15, 12)
print("Distance between points:", point1.dist(point2))  #Distance between points: 7.810249675906654


account = Account("Ruslan", 1000)
print(f"Owner: {account.owner}, Balance: {account.balance}")
account.deposit(500)
account.withdraw(300)
account.withdraw(2000)
'''
Owner: Ruslan, Balance: 1000
You have deposited 500. Balance: 1500
You have withdrawn 300. Balance: 1200
Error! You tried to withdraw 2000, your current balance: 1200
'''
numbers = [10, 3, 7, 11]
primeNumbers = list(filter(lambda x: isPrime(x), numbers))
print("Prime numbers", primeNumbers)#Prime numbers [3, 7, 11]
