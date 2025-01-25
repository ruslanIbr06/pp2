x = 0
while x < 6:
    print(x)
    x += 1
'''
0
1
2
3
4
5
'''
x = 0
while x < 100:
    print(x)
    if x == 12:
        break
    x += 2
'''
0
2
4
6
8
10
12
'''
x = 0
while x < 10:
    x += 1
    if x == 3:
        continue
    print(x)
'''
1
2
4
5
6
7
8
9
10
'''
x = 0
while x<10:
    print('x is less than 10 and equals to', x)
    x += 1
else:
    print('x is no longer less than 10')
'''
x is less than 10 and equals to 0
x is less than 10 and equals to 1
x is less than 10 and equals to 2
x is less than 10 and equals to 3
x is less than 10 and equals to 4
x is less than 10 and equals to 5
x is less than 10 and equals to 6
x is less than 10 and equals to 7
x is less than 10 and equals to 8
x is less than 10 and equals to 9
x is no longer less than 10
'''
