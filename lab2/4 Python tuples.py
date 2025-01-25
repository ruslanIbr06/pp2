tpl = (1, "cat", True, "window", "wire", "cat")
print(tpl)#(1, 'cat', True, 'window', 'wire', 'cat')
print(len(tpl))#6
print(type(tpl))#<class 'tuple'>
print(' ')

print(tpl[-2])
print(tpl[:4])
print(tpl[-3: -1])
print(tpl[2:])
if 'cat' in tpl:
    print('cat is in tuple')
'''
wire
(1, 'cat', True, 'window')
('window', 'wire')
(True, 'window', 'wire', 'cat')
cat is in tuple
'''
x = tpl
y = list(x)
y[3] = 'hour'
y.append('bus')
y.remove('cat')
x = tuple(y)
print(x)
x += ("sign", )
print(x)
print(' ')
'''
wire
(1, 'cat', True, 'window')
('window', 'wire')
(True, 'window', 'wire', 'cat')
cat is in tuple
(1, True, 'hour', 'wire', 'cat', 'bus')
(1, True, 'hour', 'wire', 'cat', 'bus', 'sign')
'''
cars = ('Toyota', "Mitsubishi", "Tesla", "Mercedes", "BMW")
(car1, car2, car3, car4, car5) = cars
print(car1, car4, car2, car5, car3, car3, car3)
(car1, car2, *othercars) = cars
print(othercars, car1, car2)
print(' ')
'''
Toyota Mercedes Mitsubishi BMW Tesla Tesla Tesla
['Tesla', 'Mercedes', 'BMW'] Toyota Mitsubishi
'''
for car in cars:
    print(car)
for i in range(len(cars)):
    print(cars[i])
i = 0
while i < len(cars):
    print(cars[i])
    i += 1
print(' ')
'''
Toyota
Mitsubishi
Tesla
Mercedes
BMW
Toyota
Mitsubishi
Tesla
Mercedes
BMW
Toyota
Mitsubishi
Tesla
Mercedes
BMW
'''
colors = ('blue', 'red', 'yellow', 'black', 'white')
output = cars + colors
output2 = cars * 2
print(output)
print(output2)
print(' ')
'''
('Toyota', 'Mitsubishi', 'Tesla', 'Mercedes', 'BMW', 'blue', 'red', 'yellow', 'black', 'white')
('Toyota', 'Mitsubishi', 'Tesla', 'Mercedes', 'BMW', 'Toyota', 'Mitsubishi', 'Tesla', 'Mercedes', 'BMW')
'''
x = (1, 3,4 ,4,1351,45,12,51,12544, 4 ,4 ,4 ,4 )
outp = x.count(4)
print(outp) #6
