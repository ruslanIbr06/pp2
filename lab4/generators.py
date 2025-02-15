#1 Create a generator that generates the squares of numbers up to some number
N = int(input("Enter value of N: "))
squares = (i ** 2 for i in range(N + 1))
print(f"Squares of numbers up to {N}:", list(squares))
'''
Enter value of N: 5
Squares of numbers up to 5: [0, 1, 4, 9, 16, 25]
'''
#2 Write a program using generator to print the even numbers between 0 and n in comma separated form where n is input from console
n = int(input("Enter value of n: "))
evenNums = (str(i) for i in range(0, n+1, 2))
print(f'Even numbers from 0 to {n}:', ", ".join(evenNums))
'''
Enter value of n: 10
Even numbers from 0 to 10: 0, 2, 4, 6, 8, 10
'''

#3 Define a function with a generator which can iterate the numbers, which are divisible by 3 and 4, between a given range 0 and n.
def divisibleBy3And4(n):
    for i in range(n+1):
        if i % 3 == 0 & i % 4 == 0:
            yield i

n = int(input("Enter the value of n: "))
print(f'Numbers that are divisible by 3 and 4 between 0 and {n}: {list(divisibleBy3And4(n))}')
'''
Enter value of n: 30
Numbers that are divisible by 3 and 4 between 0 and 30: [0, 3, 6, 9, 12, 15, 18, 21, 24, 27, 30]
'''

#4 Implement a generator called squares to yield the square of all numbers from (a) to (b). Test it with a "for" loop and print each of the yielded values.

a = int(input("Enter value of a: "))
b = int(input("Enter value of b: "))

squares = (i**2 for i in range(a,b+1))
print(f'Squares of numbers from {a} to {b}: {list(squares)}')
'''
Enter value of a: 1
Enter value of b: 10
Squares of numbers from 1 to 10: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''

#5 Implement a generator that returns all numbers from (n) down to 0.
n = int(input("Enter the value of n: "))
output = (i for i in range(n, -1, -1))
print(f"Numbers from {n} to 0: {list(output)}")
'''
Enter the value of n: 10
Numbers from 10 to 0: [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
'''