lst = ['hello', 'hi', 'privet']
print(lst)
print(len(lst))
lst1 = [1, 2, 3.3, False, "l", "Hello, World!"]
print(lst1, len(lst1))
print(type(lst1))
print(' ')
'''
['hello', 'hi', 'privet']
3
[1, 2, 3.3, False, 'l', 'Hello, World!'] 6
<class 'list'>
'''
print(lst[0])
lst[2] = 'greetings'
print(lst)
print(lst[-2])
lst.append('hellohiprivet')
lst.append('dobriy den')
print(lst[1:3], lst[:3])
print(lst, len(lst))
print(lst[-4:-1])
if 'hi' in lst:
    print('hi is in lst')
print(' ')
'''
hello
['hello', 'hi', 'greetings']
hi
['hi', 'greetings'] ['hello', 'hi', 'greetings']
['hello', 'hi', 'greetings', 'hellohiprivet', 'dobriy den'] 5
['hi', 'greetings', 'hellohiprivet']
hi is in lst
'''
lst[1:4] = ["hola", "nihao", "zdravstvuite"]
print(lst)
lst.insert(2, 'hallo')
print(lst)
print(' ')
'''
['hello', 'hola', 'nihao', 'zdravstvuite', 'dobriy den']
['hello', 'hola', 'hallo', 'nihao', 'zdravstvuite', 'dobriy den']
'''
list1 = ['Hello, ']
tuple1 = ('World!')
list1.extend(tuple1)
print(list1) #['Hello, ', 'W', 'o', 'r', 'l', 'd', '!']
print(' ')
lst.remove('hello')
print(lst)
lst.pop(1)
print(lst)
lst.pop()
print(lst)
del lst[-1]
print(lst)
list1.clear()
print(list1)
print(' ')
'''
['hola', 'hallo', 'nihao', 'zdravstvuite', 'dobriy den']
['hola', 'nihao', 'zdravstvuite', 'dobriy den']
['hola', 'nihao', 'zdravstvuite']
['hola', 'nihao']
[]
'''
for x in lst:
    print(x)
for i in range(len(lst)):
    print(lst[i])
i = 0
while i < len(lst):
    print(lst[i])
    i += 1
[print(x) for x in lst]
print(' ')
'''
hola
nihao
hola
nihao
hola
nihao
hola
nihao
'''
new = []
for x in lst:
    if "h" in x:
        new.append(x)
print(new)
new = [x for x in lst if "h" in x]
print(new)
new = [x for x in lst if x != "hola"]
print(new)
print(' ')
'''
['hola', 'nihao']
['hola', 'nihao']
['nihao']
'''
greetings = ['hi', 'hello', 'hola', 'hallo', 'hej', 'privet']
greetings.sort()
print(greetings)
nums = [1, 2, 125, -1231, 99, 123, 33, 99, 47, 56]
nums.sort()
print(nums)
nums.sort(reverse = True)
print(nums)
greetings.sort(reverse = True)
print(greetings)
greetings[0] = "Hi"
greetings[2] = "Hallo"
greetings.sort()
print(greetings)
greetings.reverse()
print(greetings)
print(' ')
'''
['hallo', 'hej', 'hello', 'hi', 'hola', 'privet']
[-1231, 1, 2, 33, 47, 56, 99, 99, 123, 125]
[125, 123, 99, 99, 56, 47, 33, 2, 1, -1231]
['privet', 'hola', 'hi', 'hello', 'hej', 'hallo']
['Hallo', 'Hi', 'hallo', 'hej', 'hello', 'hola']
['hola', 'hello', 'hej', 'hallo', 'Hi', 'Hallo']
'''
x = greetings.copy()
print(x)
x = list(greetings)
print(x)
x = greetings[:]
print(x)
print(' ')
'''
['hola', 'hello', 'hej', 'hallo', 'Hi', 'Hallo']
['hola', 'hello', 'hej', 'hallo', 'Hi', 'Hallo']
['hola', 'hello', 'hej', 'hallo', 'Hi', 'Hallo']
'''
x = ['a', 'b', 'c', 'd']
y = [1, 2, 3, 4, 5, 6, 7, 8]
z = x + y
print(z)
for j in x:
    y.append(j)
print(y)
x.extend(y)
print(x)
print(x.index('a'))
print(' ')

'''
['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 7, 8]
[1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd']
['a', 'b', 'c', 'd', 1, 2, 3, 4, 5, 6, 7, 8, 'a', 'b', 'c', 'd']
0
'''

