def gramsToOunces(grams):
    ounces = 28.3495231 * grams
    print(f'{grams} grams is {ounces} ounces')
gramsToOunces(5)#5 grams is 141.7476155 ounces
gramsToOunces(6)#6 grams is 170.0971386 ounces

def fahrenheitToCelsius(F):
    C = (5/9)*(F-32)
    print(f'{F} degrees Fahrenheit is {C} degrees Celsius')
fahrenheitToCelsius(60)#60 degrees Fahrenheit is 15.555555555555557 degrees Celsius
fahrenheitToCelsius(50)#50 degrees Fahrenheit is 10.0 degrees Celsius
fahrenheitToCelsius(32)#32 degrees Fahrenheit is 0.0 degrees Celsius

def solve(numheads, numlegs):
    rab = 0#1h 4l
    chic = 0#1h 2l
    clegs = numheads * 2 #70
    rlegs = numlegs-clegs #94 - 70 = 24
    rab = rlegs//4 * 2
    chic = numheads - rab
    print(f'There are {rab} rabbits and {chic} chickens in the farm')
    
    """ANOTHER SOLUTION
    chickens = 0
    chickens += numlegs//4               # 94//4 = 23 - amount of chickens | 23 * 2 = 46
    rabbits = numheads - chickens        #35-23 = 12 - amount of rabbits | 12 * 4 = 48 | 48+46 = 94 
    print(f'There are {rabbits} rabbits and {chickens} chickens in the farm')
    """
    
solve(35, 94)#There are 12 rabbits and 23 chickens in the farm


def isPrime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def outputPrimes(nums):
    output = []
    for num in nums:
        if(isPrime(num) == True):
            output.append(num)
    print(output)

x = "2 3 5 9 12 7 97 101"
inpuT = []
for i in x.split(" "):
    inpuT.append(int(i))
outputPrimes(inpuT)#[2, 3, 5, 7, 97, 101]

def reverseSentence(sentence):
    words = sentence.split()
    words.reverse()
    newSentence = " ".join(words)
    print(newSentence)
sentence = "I don't know"
reverseSentence(sentence)#know don't I

def has33(nums):
    result = "False"
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1]==3:
            result = "True"#or return
    print(result)
nums = [1, 2, 3, 3, 9, 0]
has33(nums)#True
nums = [1, 2, 3, 4, 9, 0]
has33(nums)#False
nums = [3, 3, 2, 3, 9, 0]
has33(nums)#True

def jamesBond(nums):
    result = "False"
    for i in range(len(nums)-2):
        if nums[i] == 0 and nums[i-1] == 0 and nums[i-2] == 7:
            result = "True"
    print(result)
nums = [0, 0, 9, 0, 0, 7]
jamesBond(nums)#True
nums = [0, 0, 2, 0, 0, 3]
jamesBond(nums)#False
nums = [0, 7, 9, 0, 7, 7]
jamesBond(nums)#False

def sphereVolume(R):
    V = (4/3) * 3.1415 * (R**3)
    print(f'Volume of a sphere with radius {R} is {V}')
sphereVolume(2)#Volume of a sphere with radius 2 is 33.50933333333333
sphereVolume(5)#Volume of a sphere with radius 5 is 523.5833333333333
sphereVolume(9)#Volume of a sphere with radius 9 is 3053.5379999999996
sphereVolume(4)#Volume of a sphere with radius 4 is 268.07466666666664
sphereVolume(7)#Volume of a sphere with radius 7 is 1436.7126666666666

def uniqueElements(nums):
    unique = []
    for num in nums:
        if num not in unique:
            unique.append(num)
    print(unique)
nums = [1, 2, 3, 4, 4, 4, 9, 2, 1]
uniqueElements(nums)#[1, 2, 3, 4, 9]
nums = [2, 2, 3, 4, 7, 4, 9, 2, 1]
uniqueElements(nums)#[2, 3, 4, 7, 9, 1]
nums = [10, 2, 3, 44, 4, 40, 9, 2, 10]
uniqueElements(nums)#[10, 2, 3, 44, 4, 40, 9]

def isPalindrome(phrase):
    a = ''.join(phrase.split()).lower()
    if a == a[::-1]:
        print(f'"{phrase}" is a palindrome')
    else:
        print(f'"{phrase}" is not a palindrome')
isPalindrome("abba")
isPalindrome("madam")
isPalindrome("mother")


def histogram(x):
    for num in x:
        print('*' * num)
histogram([1, 2, 3])
'''
*
**
***
'''
histogram([2, 2, 3])
'''
**
**
***
'''
histogram([4, 2, 3])
'''
****
**
***
'''

import random
attempts = 0
num = random.randint(1,20)
print("Hello! What is your name?")
username = input()
print(f'Well, {username}, I am thinking of a number between 1 and 20.')
print("Take a guess.")
guess = int(input())
while True:
    
    if guess < num:
        print("Your guess is too low.")
        print("Take a guess.")
        attempts += 1
        guess = int(input())
        
    if guess > num:
        print("Your guess is too high.")
        print("Take a guess.")
        guess = int(input())
        attempts += 1
        
    if guess == num:
        attempts += 1
        print(f'Good job, {username}! You guessed my number in {attempts} guesses!')
        break
'''
my program: Hello! What is your name?
user:       Ruslan
my program: Well, Ruslan, I am thinking of a number between 1 and 20.
my program: Take a guess.
user:       15
my program: Your guess is too low.
my program: Take a guess.
user:       17
my program: Your guess is too low.
my program: Take a guess.
user:       18
my program: Your guess is too low.
my program: Take a guess.
user:       19
my program: Good job, Ruslan! You guessed my number in 4 guesses!
'''
