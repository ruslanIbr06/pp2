s = {'black', 'white', 'blue', 'green', 'green', 'blue', True, 0, False, 1, 34}
print(s)
print(len(s))
print(type(s))
for el in s:
    print(el)
print("white" in s)
print('KBTU' not in s)
s.add('KBTU')
x = ['idea', 'play', 'sea', 'USA']
s.update(x)
print(s)
s.remove('idea')
print(s)
s.discard('green')
print(s)
y = s.pop()
print(y)
x.clear()
print(x)
'''
{0, True, 34, 'blue', 'green', 'white', 'black'}
7
<class 'set'>
0
True
34
blue
green
white
black
True
True
{0, True, 'sea', 'idea', 'white', 'black', 34, 'blue', 'USA', 'KBTU', 'green', 'play'}
{0, True, 'sea', 'white', 'black', 34, 'blue', 'USA', 'KBTU', 'green', 'play'}
{0, True, 'sea', 'white', 'black', 34, 'blue', 'USA', 'KBTU', 'play'}
0
[]
'''
set1 = {12, 3, 8, 9, 42, 4, 2}
set2 = {'a', 'ab', 'abc'}
set4 = {3213, 444, 999, 222}
set3 = set1.union(set2)
set3 = set1 | set2
print(set3)
output = set2.union(set1, set4, set3) # output = set2 | set1 | set4 | set3
set1.update(set2)
print(set1)
x = output.intersection(set1)
print(x)
a = set1 & set2
print(a)
set1.intersection_update(set2)#Keep the items that exist in both set1, and set2:
print(set1)
set1 = {12, 3, 8, 9, 42, 4, 2}
set2 = {'a', 'ab', 'abc'}
set3 = set1.difference(set2) # set3 = set1-set2 Keep all items from set1 that are not in set2:
print(set3)
set3 = set1.difference_update(set2)#Use the difference_update() method to keep the items that are not present in both sets SYMBOL IS ^
print(set3)

'''
[]
{2, 3, 4, 'a', 8, 9, 42, 12, 'abc', 'ab'}
{2, 3, 4, 'a', 8, 9, 42, 12, 'abc', 'ab'}
{2, 3, 4, 'a', 8, 9, 42, 12, 'abc', 'ab'}
{'abc', 'a', 'ab'}
{'abc', 'a', 'ab'}
{2, 3, 4, 8, 9, 42, 12}
None
'''
