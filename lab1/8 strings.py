#Python strings
print("PYTHON STRINGS")
print("'Hello'", '"World!"')
x = "xyz"
print(x)
a = """The quick
brown fox jumps
over the lazy
dog"""
print(a)
print(" ")
b = '''Съешь ещё
этих мягких французских булок, да выпей же
чаю'''
print(b)
x = "hello, how are you?"
print(x[0]+x[13]+x[3]+x[2]+x[8])
for i in x:
    print(i)
print("The sentence", '"', x, '"', "consists of", len(x), "symbols")
if("you" in x):
    print('The word "you" is in', '"', x, '"')
    
if("bus" not in x):
    print('The word "bus" is not in', '"', x, '"')
print("============================================================")

#Slicing strings
print("SLICING STRINGS")
x = "Hello, World!"
print(x[1:3])
print(x[:5])
print(x[7:])
print(x[-6:-1])
print("======")

#Modify strings
print("MODIFY STRINGS")
print(x.upper())
print(x.lower())
x = "  hi    hello   !   "
print(x.strip())
x = "Bello, World!"
print(x)
print(x.replace("B", "H"))
print(x.split(","))
print("====================")

#Concatenate strings
print("CONCATENATE STRINGS")
a = "Hello, "
b = "World!"
c = a+b 
print(c)
c = a+b + " How are you?"
print(c)
print("===========================")

#Format strings
print("FORMAT STRINGS")
name, age = "Ruslan", 18
output = f"My name is {name}, I am {age}"
print(output)
price = 9.9992312312312
txt = f"The price is {price:.3f} dollars"
print(txt)
txt = f"The price is {4*9} dollars"
print(txt)
print("===========================")

#Escape characters
print("ESCAPE CHARACTERS")
txt = "How to write \"Hello, World!\" in Python?"
print(txt)
print(" ")
txt = "How to write \nHello, World!\nin Python?"
print(txt)
print("===========================")

#String methods
print('STRING METHODS')
x = "Hi! How are you?"
print(x)
print(x.find("are"))
print(x.count('H'))
print(x.index('you'))
print(x.islower())
print(x.isnumeric())
print(x.isascii())


# :)
