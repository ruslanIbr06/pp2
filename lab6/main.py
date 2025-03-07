#1 Write a Python program with builtin function to multiply all the numbers in a list
import math

def multiplyList(nums):
    return math.prod(nums)

nums = [2, 3, 7, 9, 213, -3]
result = multiplyList(nums)
print(result)#-241542

#2 Write a Python program with builtin function that accepts a string and calculate the number of upper case letters and lower case letters
def count(s):
    upper = sum(map(str.isupper, s))
    lower = sum(map(str.islower, s))

    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)



text = "Hello hoW arE yOU TODAY?"
count(text)
#Uppercase letters: 10
#Lowercase letters: 9

#3 Write a Python program with builtin function that checks whether a passed string is palindrome or not
def isPalindrome(s):
    return s == s[::-1]

text = "madam"
if isPalindrome(text):
    print(f'The word {text} is a palindrome.')
else:
    print(f'THe word {text} is not a palindrome.')
    #The word madam is a palindrome.

#4 Write a Python program with builtin function that returns True if all elements of the tuple are true.

def allTrue(tup):
    return all(tup)

t1 = (True, 1, "hi")
t2 = (True, 0, "hi")

print(allTrue(t1))# True
print(allTrue(t2))# False
