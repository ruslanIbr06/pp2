class myClass:
    x = 10
a = myClass()
print(a.x)#10


class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello, my name is " + self.name)

p1 = Person("Ruslan", 18)
p1.myfunc()
#Hello, my name is Ruslan
