import random
x, y, z = 1, 1.0, 1j
print(type(x), type(y), type(z))

x, y, z = 1, 21313123123213, -312312312312
print(type(x), type(y), type(z))

x, y, z = 131231231.9, -1.0, -32323232.0
print(type(x), type(y), type(z))

x, y, z = 11e5, -9.0e2, 23E4
print(type(x), type(y), type(z))

x, y, z = 2+91j, 3j, -99j
print(type(x), type(y), type(z))

x, y, z = 3, 3.3, 3j
a, b, c = float(x), int(y), complex(x)
print(a, b, c)
print(type(a), type(b), type(c))
print("The random number is:", random.randrange(1, 1000))
