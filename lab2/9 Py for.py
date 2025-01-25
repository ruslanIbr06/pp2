nums = [1, 3, 4, 5, 9, 4, 2, 4, -1]
for num in nums:
    print(num)
'''
1
3
4
5
9
4
2
4
-1
'''
for symbol in "Hello, world!":
    print(symbol)
'''
H
e
l
l
o
,
 
w
o
r
l
d
!
'''
for num in nums:
    print(num)
    if num == 4:
        continue
    if num == 9:
        break
'''
1
3
4
5
9
'''
for x in range(2, 9):
    print(x)
'''
2
3
4
5
6
7
8
'''
for x in range(1, 50, 12):
    print(x)
else:
    print('Done!')
'''
1
13
25
37
49
Done!
'''
names = ['Vlad', 'Ivan', 'Sergey']
surnames = ['Ivanov', 'Sergeev', 'Evtushenko']
for name in names:
    for surname in surnames:
        print(name, surname)
'''
Vlad Ivanov
Vlad Sergeev
Vlad Evtushenko
Ivan Ivanov
Ivan Sergeev
Ivan Evtushenko
Sergey Ivanov
Sergey Sergeev
Sergey Evtushenko
'''
for x in [0, 1, 2]:
  pass #put in the pass statement to avoid getting an error if want to loop with no content
