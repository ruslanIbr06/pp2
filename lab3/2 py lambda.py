a = lambda x : x + 25
print(a(10))
#35
a = lambda x, y, z : (x + y) * z
print(a(1, 5, 6))
#36
def func(n):
    return lambda a : a * n
x = func(4)
print(x(15))
#60
y = func(5)
print(y(10))
#50
