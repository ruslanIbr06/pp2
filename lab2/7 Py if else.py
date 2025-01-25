a = 3
b = 4
c = 2
if(a>b):
    print('a is greater than b')
else:
    print('b is greater than a')
print("A") if a > b else print("B")
if(b > a and a > c):
    print('b>a>c')
if(a>b or a >c):
    print('a > b or a > c')
a = 50
if a > 30:
  print("Above 30,")
  if a < 60:
    print("and also below 60")
  else:
    print("but not below 60")
'''
b is greater than a
B
b>a>c
a > b or a > c
Above 30,
and also below 60
'''
