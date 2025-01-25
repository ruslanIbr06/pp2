dicti = {


    "name" : 'Donald',
    "surname" : 'Trump',
    "gender" : 'male',
    "age" : 18,
    "age" : 78,
    'president' : True,
    'order' : [45, 47]


}
print(dicti)
print(dicti['name'])
print(len(dicti))
print(type(dicti))
dct = dict(name = 'Ruslan', surname = 'Ibrayev', age = 18, country = 'Kazakhstan')
print(dct)
'''
{'name': 'Donald', 'surname': 'Trump', 'gender': 'male', 'age': 78, 'president': True, 'order': [45, 47]}
Donald
6
<class 'dict'>
{'name': 'Ruslan', 'surname': 'Ibrayev', 'age': 18, 'country': 'Kazakhstan'}
'''
x = dct.keys()
print(x)
dct['gender'] = 'male'
print(x)

x = dct.values()
print(x)
dct["name"] = 'Ruslan Ruslan'
print(x)

x = dct.items()#returns as tuple
print(x)
dct['name'] = 'Ruslan'
print(x)
if 'name' in dct:
    print('name is in dct')
'''
dict_keys(['name', 'surname', 'age', 'country'])
dict_keys(['name', 'surname', 'age', 'country', 'gender'])
dict_values(['Ruslan', 'Ibrayev', 18, 'Kazakhstan', 'male'])
dict_values(['Ruslan Ruslan', 'Ibrayev', 18, 'Kazakhstan', 'male'])
dict_items([('name', 'Ruslan Ruslan'), ('surname', 'Ibrayev'), ('age', 18), ('country', 'Kazakhstan'), ('gender', 'male')])
dict_items([('name', 'Ruslan'), ('surname', 'Ibrayev'), ('age', 18), ('country', 'Kazakhstan'), ('gender', 'male')])
name is in dct
'''

dct.update({'name' : 'Ruslan Ruslan'})
dct.update({'eyeColor' : 'brown'})
print(dct)#{'name': 'Ruslan Ruslan', 'surname': 'Ibrayev', 'age': 18, 'country': 'Kazakhstan', 'gender': 'male', 'eyeColor': 'brown'}
dct.pop('eyeColor')
print(dct)#{'name': 'Ruslan Ruslan', 'surname': 'Ibrayev', 'age': 18, 'country': 'Kazakhstan', 'gender': 'male'}
dct.popitem()
print(dct)#{'name': 'Ruslan Ruslan', 'surname': 'Ibrayev', 'age': 18, 'country': 'Kazakhstan'}
del dct['country']
print(dct)#{'name': 'Ruslan Ruslan', 'surname': 'Ibrayev', 'age': 18}
print(' ')
for x in dct:
    print(x)
'''
name
surname
age
'''
for x in dct:
    print(dct[x])
'''
Ruslan Ruslan
Ibrayev
18
'''
for x in dct.values():
    print(x)
'''
Ruslan Ruslan
Ibrayev
18
'''
for x in dct.keys():
    print(x)
'''
name
surname
age
'''
for x, y in dct.items():
    print(x, y)
'''
name Ruslan Ruslan
surname Ibrayev
age 18
'''
new = dct.copy()
print(new)
new = dict(dct)
print(new)
#{'name': 'Ruslan Ruslan', 'surname': 'Ibrayev', 'age': 18}
#{'name': 'Ruslan Ruslan', 'surname': 'Ibrayev', 'age': 18}


carDataBase = {

'car1' : {
    'model' : 'Toyota',
    'date' : '2008',
    'price' : '5.000.000tg'
    },

'car2' : {
    'model' : 'BMW',
    'date' : '2020',
    'price' : '37.000.000tg'
    },

'car3' : {
    'model' : 'Mitsubishi',
    'date' : '2013',
    'price' : '6.340.000tg'
    }

}
print(carDataBase)
print(carDataBase["car2"]['price'])
for x, obj in carDataBase.items():
    print(x)
    for y in obj:
        print(y + ':' + obj[y])
