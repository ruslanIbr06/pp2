'''
abababababba
babababa
aaaabbbbbbbbbb
abbbbbbbbbb
b
zxcczxczxczxccvbnm,mgfds
abb
abbb
abb
hello_world
hi
how are you
darth_maul
LukeSkywalker
AnakinSkywalkerDarthVader
Obiwankenobi
revenge of the sith
943949133949
77777777
asddsa
qwerty
Hello, world!
aHELLOb
snake_case_example
camelCaseExample
t_e_s_t
hello, i don't know what to do
hellOhoWaReYoUhehehe
NoSpacesInThisStringRight
'''



import re

#1 Write a Python program that matches a string that has an 'a' followed by zero or more 'b''s.

def match(filename):
    pattern = re.compile(r'^ab*$')

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):
                print(f"Matched: {line}")


if __name__ == "__main__":
    match("row.txt") #Matched: abbbbbbbbbb

#2 Write a Python program that matches a string that has an 'a' followed by two to three 'b'.

def aFollowed23b(filename):
    pattern = re.compile(r'^a{2,3}$')

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):
                print(f"Matched: {line}")
if __name__ == "__main__":
    aFollowed23b("row.txt")
'''
Matched: abb
Matched: abbb
'''

#3 Write a Python program to find sequences of lowercase letters joined with a underscore.

def lowerCase_Joined(filename):
    pattern = re.compile(r'^[a-z]+_[a-z]+$')

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):
                print(f"Matched: {line}")

if __name__ == "__main__":
    lowerCase_Joined("row.txt")
'''
Matched: hello_world
Matched: darth_maul
'''

#4 Write a Python program to find the sequences of one upper case letter followed by lower case letters.

def upperFollowedByLower(filename):
    pattern = re.compile(r'^[A-Z][a-z]+$')

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):
                print(f"Matched: {line}")
if __name__ == "__main__":
    upperFollowedByLower("row.txt")           #Matched: Obiwankenobi

#5 Write a Python program that matches a string that has an 'a' followed by anything, ending in 'b'.

def aFUNCb(filename):
    pattern = re.compile(r'^a.*b$')

    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if pattern.match(line):
                print(f"Matched: {line}")
                
if __name__ == "__main__":
    aFUNCb("row.txt")
'''
Matched: aaaabbbbbbbbbb
Matched: abbbbbbbbbb
Matched: abb
Matched: abbb
Matched: abb
Matched: aHELLOb
'''

#6 Write a Python program to replace all occurrences of space, comma, or dot with a colon.

def replace(filename):
    with open(filename, 'r') as file:
        for line in file:
            if re.search(r'[ ,.]', line):
                print(re.sub(r'[ ,.]', ':', line.strip()))

if __name__ == "__main__":
    replace("row.txt")
'''
zxcczxczxczxccvbnm:mgfds
how:are:you
revenge:of:the:sith
Hello::world!
hello::i:don't:know:what:to:do
'''

#7 Write a python program to convert snake case string to camel case string.


def snakeToCamel(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if '_' in line:
                components = line.split('_')
                print(components[0] + ''.join(x.title() for x in components[1:]))

if __name__ == "__main__":
    snakeToCamel("row.txt")

'''
helloWorld
darthMaul
snakeCaseExample
tEST
'''


#8 Write a Python program to split a string at uppercase letters.

def upperSplit(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            result = re.findall(r'[A-Z][^A-Z]*', line)
            if result:
                print(result)

if __name__ == "__main__":
    upperSplit("row.txt")

'''
['Luke', 'Skywalker']
['Anakin', 'Skywalker', 'Darth', 'Vader']
['Obiwankenobi']
['Hello, world!']
['H', 'E', 'L', 'L', 'Ob']
['Case', 'Example']
['Oho', 'Wa', 'Re', 'Yo', 'Uhehehe']
['No', 'Spaces', 'In', 'This', 'String', 'Right']
'''

#9 Write a Python program to insert spaces between words starting with capital letters.

def spacesBetweenCapitals(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if any(c.isupper() for c in line):
                result = re.sub(r'(?<!^)(?=[A-Z])', ' ', line)
                print(result)

if __name__ == "__main__":
    spacesBetweenCapitals("row.txt")

'''
Luke Skywalker
Anakin Skywalker Darth Vader
Obiwankenobi
Hello, world!
a H E L L Ob
camel Case Example
hell Oho Wa Re Yo Uhehehe
No Spaces In This String Right
'''

#10 Write a Python program to convert a given camel case string to snake case.

def camelToSnake(filename):
    with open(filename, 'r') as file:
        for line in file:
            line = line.strip()
            if any(c.isupper() for c in line):
                result = re.sub(r'(?<!^)(?=[A-Z])', '_', line).lower()
                print(result)

if __name__ == "__main__":
    camelToSnake("row.txt")
'''
luke_skywalker
anakin_skywalker_darth_vader
obiwankenobi
hello, world!
a_h_e_l_l_ob
camel_case_example
hell_oho_wa_re_yo_uhehehe
no_spaces_in_this_string_right
'''